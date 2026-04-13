"""
Exercise 3: Boto3 AWS + S3 + Python

Objective: Use Boto3 to interact with AWS S3 for downloading and uploading data.

TODO: Complete the following functions to:
1. Connect to AWS S3
2. List and filter S3 objects
3. Download files from S3
4. Process downloaded data
5. Upload results back to S3
"""

from pathlib import Path
from typing import List, Dict
import boto3
from botocore.exceptions import ClientError
import pandas as pd
from tqdm import tqdm


class S3DataManager:
    """Helper class to manage S3 operations."""
    
    def __init__(self, bucket_name: str, region_name: str = "us-east-1",
                 local_dir: str = "s3_data", output_dir: str = "output"):
        """
        Initialize S3 manager.
        
        Args:
            bucket_name: Name of the S3 bucket
            region_name: AWS region
            local_dir: Local directory for downloads
            output_dir: Directory for processed output
        """
        self.bucket_name = bucket_name
        self.region_name = region_name
        self.local_dir = Path(local_dir)
        self.output_dir = Path(output_dir)
        self.local_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # TODO: Initialize S3 client
        # self.s3_client = None
    
    def connect_s3(self) -> None:
        """
        Connect to AWS S3.
        
        TODO: Implement this method to:
        - Create a Boto3 S3 client
        - Test the connection
        - Handle authentication errors
        - Store client reference
        """
        # TODO: Implement S3 connection
        raise NotImplementedError("connect_s3 method not implemented")
    
    def list_objects(self, prefix: str = "", file_type: str = None) -> List[Dict]:
        """
        List objects in the S3 bucket.
        
        TODO: Implement this method to:
        - Use list_objects_v2 to list bucket contents
        - Filter by prefix if provided
        - Filter by file type (extension) if provided
        - Handle pagination
        - Return list of object metadata dicts
        
        Args:
            prefix: Optional prefix to filter objects
            file_type: Optional file extension to filter (.csv, .json, etc.)
            
        Returns:
            List of object information dicts
        """
        # TODO: Implement object listing
        raise NotImplementedError("list_objects method not implemented")
    
    def download_files(self, objects: List[Dict]) -> List[Path]:
        """
        Download multiple files from S3.
        
        TODO: Implement this method to:
        - Iterate through objects
        - Download each file using download_file or get_object
        - Show progress with tqdm
        - Handle download errors gracefully
        - Return list of local file paths
        
        Args:
            objects: List of object metadata dicts
            
        Returns:
            List of local file paths
        """
        # TODO: Implement file downloading
        raise NotImplementedError("download_files method not implemented")
    
    def process_files(self, file_paths: List[Path]) -> pd.DataFrame:
        """
        Process downloaded files.
        
        TODO: Implement this method to:
        - Load files into DataFrames (CSV, JSON, etc.)
        - Combine multiple files
        - Perform basic cleaning/transformation
        - Return combined DataFrame
        
        Args:
            file_paths: List of local file paths
            
        Returns:
            Combined and processed DataFrame
        """
        # TODO: Implement file processing
        raise NotImplementedError("process_files method not implemented")
    
    def upload_results(self, dataframe: pd.DataFrame, 
                      filename: str = "results.csv") -> bool:
        """
        Upload processed results back to S3.
        
        TODO: Implement this method to:
        - Save DataFrame locally
        - Upload to S3 using put_object
        - Handle upload errors
        - Return success status
        
        Args:
            dataframe: DataFrame to upload
            filename: S3 filename
            
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement results upload
        raise NotImplementedError("upload_results method not implemented")


def main():
    """Main function to run the S3 exercise."""
    
    # Configuration
    bucket_name = "upwego-data-engineering"  # Replace with your bucket
    region_name = "us-east-1"
    
    print("=" * 60)
    print("Exercise 3: Boto3 AWS + S3 + Python")
    print("=" * 60)
    
    # Note: This exercise requires AWS credentials configured
    # You can set them via environment variables or AWS credentials file
    
    try:
        # TODO: Implement the main workflow:
        
        # 1. Create S3 manager
        # manager = S3DataManager(bucket_name, region_name)
        # print(f"\nConnecting to S3 bucket: {bucket_name}")
        # manager.connect_s3()
        # print("✓ Connected to S3")
        
        # 2. List objects in S3
        # print("\nListing S3 objects...")
        # objects = manager.list_objects(prefix="data/", file_type=".csv")
        # print(f"✓ Found {len(objects)} objects")
        
        # 3. Download files from S3
        # print("\nDownloading files from S3...")
        # local_files = manager.download_files(objects)
        # print(f"✓ Downloaded {len(local_files)} files")
        
        # 4. Process the files
        # print("\nProcessing downloaded data...")
        # df = manager.process_files(local_files)
        # print(f"✓ Processed {len(df)} rows")
        
        # 5. Upload results back to S3
        # print("\nUploading results to S3...")
        # if manager.upload_results(df):
        #     print("✓ Results uploaded successfully")
        
        # print("\n" + "=" * 60)
        # print("Success! S3 operations completed")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the five methods above")
        print("\nNote: This exercise requires AWS credentials.")
        print("Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.")
        
    except ClientError as e:
        print(f"\n✗ AWS Error: {e}")
        raise
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
