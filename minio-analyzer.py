import streamlit as st
from minio import Minio
from collections import defaultdict
import pandas as pd

st.set_page_config(page_title="MinIO Duplicate Analyzer", layout="wide")

st.title("🔍 MinIO Duplicate File Analyzer")

with st.sidebar:
    st.header("Connection Settings")
    endpoint = st.text_input("MinIO Endpoint", value="")
    access_key = st.text_input("Access Key", value="")
    secret_key = st.text_input("Secret Key", value="", type="password")
    bucket_name = st.text_input("Bucket Name", value="")
    analyze_button = st.button("Analyze")

if analyze_button:
    try:
        client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)
        
        file_hashes = defaultdict(list)
        total_bucket_size_bytes = 0
        total_bucket_objects = 0
        
        with st.spinner('Processing...'):
            objects = client.list_objects(bucket_name, recursive=True)
            
            for obj in objects:
                total_bucket_objects += 1
                total_bucket_size_bytes += obj.size
                file_hashes[obj.etag].append({
                    "name": obj.object_name,
                    "size": obj.size
                })

        total_waste_bytes = 0
        total_duplicates_count = 0
        duplicate_groups = []

        for etag, files in file_hashes.items():
            if len(files) > 1:
                count = len(files)
                unit_size = files[0]['size']
                total_duplicates_count += (count - 1)
                total_waste_bytes += unit_size * (count - 1)
                
                duplicate_groups.append({
                    "ETag": etag,
                    "Count": count,
                    "Size (GB)": f"{unit_size / (1024**3):.10f}",
                    "Files": [f['name'] for f in files]
                })

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Object Count", total_bucket_objects)
        col2.metric("Total Bucket Size", f"{total_bucket_size_bytes / (1024**3):.4f} GB")
        col3.metric("Duplicate Object Count", total_duplicates_count)
        col4.metric("Duplicate Data Size", f"{total_waste_bytes / (1024**3):.4f} GB")

        st.divider()

        st.subheader(f"📁 Dublicate Files Details. Bucket Name: {bucket_name}")
        
        if duplicate_groups:
            for group in duplicate_groups:
                with st.expander(f"🔑 ETag: {group['ETag']} | {group['Count']} Files | {group['Size (GB)']} GB"):
                    st.write("**File List:**")
                    for idx, name in enumerate(group['Files'], 1):
                        st.text(f"  {idx}. {name}")
        else:
            st.success("No duplicate files found!")

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Click the button to start analysis.")
