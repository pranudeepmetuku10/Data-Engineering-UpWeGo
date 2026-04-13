"""
Exercise 4: Convert JSON to CSV + Ragged Directories

Objective: Traverse nested directories and convert JSON files to CSV format.

TODO: Complete the following functions to:
1. Find all JSON files in a directory tree
2. Load and parse JSON files
3. Handle various JSON structures
4. Convert to CSV format
5. Organize and save output files
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import pandas as pd


class JSONtoCSVConverter:
    """Helper class to convert JSON files to CSV."""
    
    def __init__(self, data_dir: str = "sample_data", output_dir: str = "csv_output"):
        """
        Initialize converter.
        
        Args:
            data_dir: Root directory containing JSON files
            output_dir: Directory for CSV output
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def find_json_files(self, directory: Path = None) -> List[Path]:
        """
        Recursively find all JSON files in a directory.
        
        TODO: Implement this method to:
        - Use Path.glob() or rglob() to find all .json files
        - Recursively traverse subdirectories
        - Return list of all JSON file paths
        - Handle permission errors gracefully
        
        Args:
            directory: Directory to search (defaults to self.data_dir)
            
        Returns:
            List of Path objects for all JSON files found
        """
        # TODO: Implement JSON file discovery
        raise NotImplementedError("find_json_files method not implemented")
    
    def load_json_file(self, file_path: Path) -> any:
        """
        Load a JSON file and handle various structures.
        
        TODO: Implement this method to:
        - Read the JSON file
        - Handle JSON parsing errors
        - Return the parsed data (dict, list, etc.)
        - Handle empty files
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Parsed JSON data
        """
        # TODO: Implement JSON loading
        raise NotImplementedError("load_json_file method not implemented")
    
    def flatten_json(self, data: any) -> pd.DataFrame:
        """
        Convert JSON data to a pandas DataFrame.
        
        TODO: Implement this method to:
        - Handle dict -> single row DataFrame
        - Handle list of dicts -> multiple rows
        - Flatten nested structures using pd.json_normalize()
        - Handle arrays by creating multiple rows
        - Return a properly formatted DataFrame
        
        Args:
            data: Parsed JSON data (dict or list)
            
        Returns:
            pandas DataFrame with flattened structure
        """
        # TODO: Implement JSON flattening
        raise NotImplementedError("flatten_json method not implemented")
    
    def convert_file(self, json_path: Path) -> Tuple[bool, int]:
        """
        Convert a single JSON file to CSV.
        
        TODO: Implement this method to:
        - Load the JSON file
        - Convert to DataFrame
        - Create output directory if needed
        - Save to CSV with same name as input
        - Return (success, row_count) tuple
        - Handle errors gracefully
        
        Args:
            json_path: Path to JSON file
            
        Returns:
            Tuple of (success: bool, row_count: int)
        """
        # TODO: Implement single file conversion
        raise NotImplementedError("convert_file method not implemented")
    
    def convert_all(self) -> Dict[str, any]:
        """
        Convert all JSON files in the directory tree.
        
        TODO: Implement this method to:
        - Find all JSON files
        - Convert each one
        - Track statistics (total files, rows, errors)
        - Preserve directory structure in output
        - Return summary statistics
        
        Returns:
            Dict with conversion results and statistics
        """
        # TODO: Implement batch conversion
        raise NotImplementedError("convert_all method not implemented")


def create_sample_data():
    """
    Create sample JSON files for testing.
    This is a helper function to generate test data.
    """
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Sample 1: List of objects at root level
    sample1 = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35},
    ]
    (sample_dir / "data1.json").write_text(json.dumps(sample1, indent=2))
    
    # Sample 2: Nested directory with different structure
    nested_dir = sample_dir / "nested"
    nested_dir.mkdir(parents=True, exist_ok=True)
    sample2 = {
        "users": [
            {"email": "alice@example.com", "status": "active"},
            {"email": "bob@example.com", "status": "inactive"},
        ]
    }
    (nested_dir / "data2.json").write_text(json.dumps(sample2, indent=2))
    
    # Sample 3: Deeply nested directory
    deep_dir = nested_dir / "deep"
    deep_dir.mkdir(parents=True, exist_ok=True)
    sample3 = [
        {"product_id": 1, "price": 9.99, "category": "electronics"},
        {"product_id": 2, "price": 19.99, "category": "books"},
    ]
    (deep_dir / "data3.json").write_text(json.dumps(sample3, indent=2))
    
    print("✓ Sample data created in sample_data/")


def main():
    """Main function to run the JSON to CSV exercise."""
    
    print("=" * 60)
    print("Exercise 4: Convert JSON to CSV + Ragged Directories")
    print("=" * 60)
    
    try:
        # Create sample data if it doesn't exist
        if not Path("sample_data").exists():
            print("\nCreating sample data...")
            create_sample_data()
        
        # Initialize converter
        converter = JSONtoCSVConverter()
        
        # TODO: Implement the main workflow:
        print("\nFinding JSON files...")
        # json_files = converter.find_json_files()
        # print(f"✓ Found {len(json_files)} JSON files")
        
        # for file in json_files:
        #     print(f"  - {file.relative_to(converter.data_dir)}")
        
        print("\nConverting JSON files to CSV...")
        # results = converter.convert_all()
        # print(f"✓ Converted {results['total_files']} files")
        # print(f"✓ Total rows processed: {results['total_rows']}")
        
        # if results['errors'] > 0:
        #     print(f"⚠ Errors: {results['errors']}")
        
        # print("\n" + "=" * 60)
        # print("Success! All JSON files converted to CSV")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the four methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
