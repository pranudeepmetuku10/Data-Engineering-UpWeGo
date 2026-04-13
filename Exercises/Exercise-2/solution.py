"""
Exercise 2: Web Scraping + Downloading + Pandas

Objective: Scrape a website, download data files, and process them with Pandas.

TODO: Complete the following functions to:
1. Scrape a website to find download links
2. Download multiple CSV/JSON files
3. Load and process data with Pandas
4. Aggregate and save results
"""

import os
import json
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class WebScraper:
    """Helper class for web scraping and data collection."""
    
    def __init__(self, data_dir: str = "data", output_dir: str = "output"):
        """
        Initialize the scraper.
        
        Args:
            data_dir: Directory for downloaded files
            output_dir: Directory for output files
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def scrape_links(self, url: str, selector: str = "a") -> List[Tuple[str, str]]:
        """
        Scrape a webpage for links.
        
        TODO: Implement this method to:
        - Fetch the HTML from the URL
        - Parse it with BeautifulSoup
        - Extract links using the given selector
        - Filter for data file links (csv, json, xlsx)
        - Convert relative URLs to absolute URLs
        - Return list of (link_text, link_url) tuples
        
        Args:
            url: URL of the webpage to scrape
            selector: CSS selector for finding links
            
        Returns:
            List of (link_text, link_url) tuples
        """
        # TODO: Implement web scraping
        raise NotImplementedError("scrape_links method not implemented")
    
    def download_files(self, links: List[Tuple[str, str]]) -> List[Path]:
        """
        Download multiple files from the provided URLs.
        
        TODO: Implement this method to:
        - Iterate through the links
        - Download each file with progress indication
        - Save files to self.data_dir
        - Handle HTTP errors gracefully
        - Return list of downloaded file paths
        
        Args:
            links: List of (link_text, link_url) tuples
            
        Returns:
            List of Path objects for downloaded files
        """
        # TODO: Implement file downloading
        raise NotImplementedError("download_files method not implemented")
    
    def load_data_files(self, file_paths: List[Path]) -> List[pd.DataFrame]:
        """
        Load data from CSV and JSON files into DataFrames.
        
        TODO: Implement this method to:
        - Determine file type (.csv, .json, etc.)
        - Load files using appropriate Pandas functions
        - Handle different file formats
        - Return list of DataFrames
        - Skip files that fail to load
        
        Args:
            file_paths: List of Path objects
            
        Returns:
            List of loaded pandas DataFrames
        """
        # TODO: Implement data loading
        raise NotImplementedError("load_data_files method not implemented")
    
    def aggregate_data(self, dataframes: List[pd.DataFrame], 
                      groupby_column: str = None) -> pd.DataFrame:
        """
        Aggregate data from multiple DataFrames.
        
        TODO: Implement this method to:
        - Combine multiple DataFrames using concat or merge
        - Handle duplicate columns
        - Perform aggregations (sum, count, mean) if groupby_column provided
        - Clean data (remove nulls, handle inconsistencies)
        - Return combined and aggregated DataFrame
        
        Args:
            dataframes: List of DataFrames to combine
            groupby_column: Optional column to group by
            
        Returns:
            Aggregated DataFrame
        """
        # TODO: Implement data aggregation
        raise NotImplementedError("aggregate_data method not implemented")
    
    def save_results(self, df: pd.DataFrame, filename: str = "aggregated_data.csv"):
        """
        Save the results to a CSV file.
        
        TODO: Implement this method to:
        - Create output directory if needed
        - Save DataFrame to CSV
        - Print summary statistics
        - Return the path to saved file
        
        Args:
            df: DataFrame to save
            filename: Output filename
            
        Returns:
            Path to saved file
        """
        # TODO: Implement results saving
        raise NotImplementedError("save_results method not implemented")


def main():
    """Main function to run the web scraping exercise."""
    
    # Example URL - you can replace this with any website containing data links
    # For testing, we'll use a simpler approach with public data
    scrape_url = "https://data.world/datasets/most-starred-github-repos"
    
    print("=" * 60)
    print("Exercise 2: Web Scraping + Downloading + Pandas")
    print("=" * 60)
    
    try:
        scraper = WebScraper()
        
        # TODO: Implement the main workflow:
        # 1. Scrape links from the website
        # print(f"\nScraping: {scrape_url}")
        # links = scraper.scrape_links(scrape_url)
        # print(f"✓ Found {len(links)} download links")
        
        # 2. Download the files
        # print("\nDownloading files...")
        # downloaded_files = scraper.download_files(links)
        # print(f"✓ Downloaded {len(downloaded_files)} files")
        
        # 3. Load the data
        # print("\nLoading data files...")
        # dataframes = scraper.load_data_files(downloaded_files)
        # print(f"✓ Loaded {len(dataframes)} DataFrames")
        
        # 4. Aggregate the data
        # print("\nAggregating data...")
        # combined_df = scraper.aggregate_data(dataframes)
        # print(f"✓ Combined {len(combined_df)} rows")
        
        # 5. Save results
        # print("\nSaving results...")
        # output_path = scraper.save_results(combined_df)
        # print(f"✓ Saved to: {output_path}")
        
        # print("\n" + "=" * 60)
        # print("Success! Data pipeline completed")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the five methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
