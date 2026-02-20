# MinIO Duplicate File Analyzer

This is a Streamlit application designed to analyze duplicate files in a MinIO bucket. It helps you identify redundant data and visualize storage usage.

## Features

- **Connect to MinIO**: Easily connect to your MinIO instance using endpoint, access key, and secret key.
- **Analyze Duplicates**: Scans the specified bucket for duplicate files based on their ETag (MD5 hash).
- **Visualize Data**: Provides metrics on total object count, bucket size, duplicate count, and wasted storage space.
- **Detailed Report**: Lists duplicate file groups, showing their count, total size, and individual file names.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) (recommended)
- Python 3.9+ (if running locally without Docker)
- A running MinIO instance

## Getting Started

### Using Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nijatmansimov/MinIO-Duplicate-File-Analyzer.git
    cd MinIO-Duplicate-File-Analyzer
    ```

2.  **Build and run the application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**
    Open your browser and navigate to `http://localhost:8501`.

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nijatmansimov/MinIO-Duplicate-File-Analyzer.git
    cd MinIO-Duplicate-File-Analyzer
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run minio-analyzer.py
    ```

4.  **Access the application:**
    Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`).

## Usage

1.  **Enter Connection Details**:
    - **MinIO Endpoint**: The URL of your MinIO server (e.g., `play.min.io` or `localhost:9000`).
    - **Access Key**: Your MinIO access key.
    - **Secret Key**: Your MinIO secret key.
    - **Bucket Name**: The name of the bucket you want to analyze.

2.  **Click "Analyze"**: The application will fetch the object list and process it to find duplicates.

3.  **View Results**:
    - **Metrics**: See the overview of your bucket's storage.
    - **Duplicate Files Details**: Expand the sections to see the list of duplicate files, their count, and size.

## Requirements

- `streamlit`
- `minio`
- `pandas`
