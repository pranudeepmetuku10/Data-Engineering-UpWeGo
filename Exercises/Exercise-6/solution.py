"""
Exercise 6: Ingestion and Aggregation with PySpark

Objective: Use PySpark to load, process, and aggregate distributed data.

TODO: Complete the following functions to:
1. Initialize Spark Session
2. Load data from multiple formats
3. Perform data transformations
4. Execute aggregations
5. Write results to multiple formats
"""

from pathlib import Path
from typing import List, Dict
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
import pandas as pd


class SparkDataProcessor:
    """Helper class for PySpark data processing."""
    
    def __init__(self, app_name: str = "Exercise6", output_dir: str = "results"):
        """
        Initialize Spark session.
        
        TODO: Implement this method to:
        - Create SparkSession
        - Set configuration for local mode
        - Configure logging
        - Store session and output directory
        
        Args:
            app_name: Application name
            output_dir: Directory for output files
        """
        self.app_name = app_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.spark = None
        # TODO: Initialize SparkSession
    
    def load_csv(self, file_path: str) -> DataFrame:
        """
        Load CSV file into Spark DataFrame.
        
        TODO: Implement this method to:
        - Read CSV with inferSchema=True
        - Handle headers
        - Return Spark DataFrame
        
        Args:
            file_path: Path to CSV file
            
        Returns:
            Spark DataFrame
        """
        # TODO: Implement CSV loading
        raise NotImplementedError("load_csv method not implemented")
    
    def load_parquet(self, file_path: str) -> DataFrame:
        """
        Load Parquet file into Spark DataFrame.
        
        TODO: Implement this method to:
        - Read Parquet file
        - Handle schema
        - Return DataFrame
        
        Args:
            file_path: Path to Parquet file
            
        Returns:
            Spark DataFrame
        """
        # TODO: Implement Parquet loading
        raise NotImplementedError("load_parquet method not implemented")
    
    def aggregate_data(self, df: DataFrame, groupby_cols: List[str],
                      agg_dict: Dict[str, str]) -> DataFrame:
        """
        Perform aggregation on DataFrame.
        
        TODO: Implement this method to:
        - Use groupBy with list of columns
        - Apply aggregations (sum, count, avg, etc.)
        - Return aggregated DataFrame
        
        Args:
            df: Spark DataFrame
            groupby_cols: Columns to group by
            agg_dict: Dict of {column: aggregation_function}
                     Example: {"amount": "sum", "id": "count"}
            
        Returns:
            Aggregated DataFrame
        """
        # TODO: Implement aggregation logic
        raise NotImplementedError("aggregate_data method not implemented")
    
    def join_dataframes(self, left_df: DataFrame, right_df: DataFrame,
                       join_col: str, join_type: str = "inner") -> DataFrame:
        """
        Join two DataFrames.
        
        TODO: Implement this method to:
        - Perform join on specified column
        - Support inner, left, right, outer joins
        - Return joined DataFrame
        
        Args:
            left_df: Left DataFrame
            right_df: Right DataFrame
            join_col: Column name to join on
            join_type: Type of join (inner, left, right, outer)
            
        Returns:
            Joined DataFrame
        """
        # TODO: Implement join logic
        raise NotImplementedError("join_dataframes method not implemented")
    
    def write_csv(self, df: DataFrame, filename: str) -> str:
        """
        Write DataFrame to CSV.
        
        TODO: Implement this method to:
        - Convert to single file if small
        - Write to CSV format
        - Return output path
        
        Args:
            df: DataFrame to write
            filename: Output filename
            
        Returns:
            Path to output file
        """
        # TODO: Implement CSV writing
        raise NotImplementedError("write_csv method not implemented")
    
    def write_parquet(self, df: DataFrame, filename: str) -> str:
        """
        Write DataFrame to Parquet.
        
        TODO: Implement this method to:
        - Write to Parquet format
        - Use compression
        - Return output path
        
        Args:
            df: DataFrame to write
            filename: Output filename
            
        Returns:
            Path to output file
        """
        # TODO: Implement Parquet writing
        raise NotImplementedError("write_parquet method not implemented")
    
    def close(self):
        """Stop Spark session."""
        if self.spark:
            self.spark.stop()


def create_sample_data():
    """Create sample data files for the exercise."""
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Sample orders data
    import pandas as pd
    orders_data = {
        'order_id': range(1, 101),
        'customer_id': [i % 20 for i in range(100)],
        'amount': [100 + i * 5 for i in range(100)],
        'date': ['2024-01-' + f"{(i % 28) + 1:02d}" for i in range(100)]
    }
    pd.DataFrame(orders_data).to_csv(sample_dir / 'orders.csv', index=False)
    
    # Sample products data
    products_data = {
        'product_id': range(1, 21),
        'category': ['Electronics'] * 7 + ['Books'] * 7 + ['Clothing'] * 6,
        'price': [100, 200, 150, 300, 50, 75, 125, 20, 15, 25, 30, 18, 40, 60, 80, 90, 110, 140, 160, 180]
    }
    pd.DataFrame(products_data).to_csv(sample_dir / 'products.csv', index=False)
    
    print("✓ Sample data created")


def main():
    """Main function to run PySpark exercise."""
    
    print("=" * 60)
    print("Exercise 6: Ingestion and Aggregation with PySpark")
    print("=" * 60)
    
    processor = None
    try:
        # Create sample data
        if not Path("sample_data").exists():
            print("\nCreating sample data...")
            create_sample_data()
        
        # TODO: Implement the main workflow:
        
        # processor = SparkDataProcessor()
        # print("\nLoading data files...")
        # orders_df = processor.load_csv("sample_data/orders.csv")
        # products_df = processor.load_csv("sample_data/products.csv")
        # print(f"✓ Loaded orders: {orders_df.count()} rows")
        # print(f"✓ Loaded products: {products_df.count()} rows")
        
        # print("\nPerforming aggregations...")
        # TODO: Example aggregations
        # total_sales = processor.aggregate_data(orders_df, [], {"amount": "sum"})
        # print(f"✓ Total sales: ${total_sales.collect()[0][0]}")
        
        # print("\nWriting results...")
        # TODO: Write results
        # csv_path = processor.write_csv(orders_df, "orders_output")
        # print(f"✓ Saved to: {csv_path}")
        
        # print("\n" + "=" * 60)
        # print("Success! PySpark pipeline completed")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the six methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
    finally:
        if processor:
            processor.close()


if __name__ == "__main__":
    main()
