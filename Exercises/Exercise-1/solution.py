"""
Exercise 1: Downloading Files

Objective: Download a file from an HTTP source, unzip it, and store it locally.

TODO: Complete the following function to:
1. Download the zip file from the URL
2. Save it locally
3. Extract the contents
4. Verify extraction was successful
"""

import os
import zipfile
from pathlib import Path
from typing import List
import requests
from tqdm import tqdm


class FileDownloader:
    """Helper class to download and extract files."""
    
    def __init__(self, output_dir: str = "downloads"):
        """
        Initialize the downloader.
        
        Args:
            output_dir: Directory where downloaded files will be saved
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download_file(self, url: str, filename: str = None) -> Path:
        """
        Download a file from the given URL.
        
        TODO: Implement this method to:
        - Handle the HTTP request
        - Show download progress using tqdm
        - Save the file to self.output_dir
        - Return the path to the downloaded file
        - Handle errors gracefully
        
        Args:
            url: URL of the file to download
            filename: Optional custom filename (uses URL basename if not provided)
            
        Returns:
            Path to the downloaded file
        """
        # TODO: Implement file download with progress bar
        raise NotImplementedError("download_file method not implemented")
    
    def extract_zip(self, zip_path: Path, extract_to: Path = None) -> List[str]:
        """
        Extract a zip file to the specified directory.
        
        TODO: Implement this method to:
        - Open the zip file
        - Extract all contents
        - Handle potential errors (corrupted zip, permissions, etc.)
        - Return list of extracted file names
        
        Args:
            zip_path: Path to the zip file
            extract_to: Directory to extract to (defaults to self.output_dir)
            
        Returns:
            List of extracted file paths
        """
        # TODO: Implement zip extraction
        raise NotImplementedError("extract_zip method not implemented")
    
    def list_extracted_files(self) -> List[str]:
        """
        List all files in the output directory.
        
        TODO: Implement this method to:
        - Recursively find all files in self.output_dir
        - Exclude the zip file itself
        - Return sorted list of file paths
        
        Returns:
            List of file paths relative to output_dir
        """
        # TODO: Implement file listing
        raise NotImplementedError("list_extracted_files method not implemented")


def main():
    """Main function to run the download exercise."""
    
    # Sample data URL - using a public test file
    # This is a small test file for demonstration
    download_url = "https://www.w3schools.com/python/files.zip"
    
    print("=" * 60)
    print("Exercise 1: Downloading and Extracting Files")
    print("=" * 60)
    
    # TODO: Implement the main logic:
    # 1. Create a FileDownloader instance
    # 2. Download the file from the URL
    # 3. Extract the zip file
    # 4. List and display all extracted files
    # 5. Print a success message with file count
    
    try:
        # Initialize downloader
        downloader = FileDownloader(output_dir="downloads")
        
        # TODO: Download the file
        print(f"\nDownloading from: {download_url}")
        # zip_path = downloader.download_file(download_url)
        # print(f"✓ Downloaded to: {zip_path}")
        
        # TODO: Extract the zip file
        # print("\nExtracting files...")
        # extracted_files = downloader.extract_zip(zip_path)
        # print(f"✓ Extracted {len(extracted_files)} files")
        
        # TODO: List extracted files
        # print("\nExtracted files:")
        # all_files = downloader.list_extracted_files()
        # for file in all_files:
        #     print(f"  - {file}")
        
        # print("\n" + "=" * 60)
        # print(f"Success! Downloaded and extracted {len(all_files)} files")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the three methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
