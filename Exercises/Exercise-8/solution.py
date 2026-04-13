"""
Exercise 8: Using DuckDB for Analytics and Transforms

Objective: Use DuckDB for fast, efficient analytics and data transformations.

TODO: Complete the following functions to:
1. Load data from various formats (CSV, JSON, Parquet)
2. Execute SQL queries
3. Perform joins and transformations
4. Create analytical views
5. Export results
"""

from pathlib import Path
from typing import List
import duckdb
import pandas as pd


class DuckDBAnalyzer:
    """DuckDB-based data analysis and transformation."""
    
    def __init__(self, database: str = ":memory:"):
        """
        Initialize DuckDB connection.
        
        TODO: Implement to:
        - Create DuckDB connection
        - Store database reference
        
        Args:
            database: Database path (":memory:" for in-memory)
        """
        self.database = database
        self.conn = None
        # TODO: Initialize connection
    
    def load_csv(self, file_path: str, table_name: str) -> None:
        """
        Load CSV file into DuckDB table.
        
        TODO: Implement to:
        - Read CSV file using DuckDB
        - Create table from data
        - Store reference for query use
        
        Args:
            file_path: Path to CSV file
            table_name: Name for the table in DuckDB
        """
        raise NotImplementedError("load_csv not implemented")
    
    def load_parquet(self, file_path: str, table_name: str) -> None:
        """
        Load Parquet file into DuckDB table.
        
        TODO: Implement to:
        - Read Parquet file
        - Create table
        
        Args:
            file_path: Path to Parquet file
            table_name: Table name
        """
        raise NotImplementedError("load_parquet not implemented")
    
    def execute_query(self, query: str) -> pd.DataFrame:
        """
        Execute SQL query and return results.
        
        TODO: Implement to:
        - Execute SQL query
        - Convert results to DataFrame
        - Handle errors gracefully
        
        Args:
            query: SQL query string
            
        Returns:
            Results as pandas DataFrame
        """
        raise NotImplementedError("execute_query not implemented")
    
    def join_tables(self, left_table: str, right_table: str,
                   join_col: str, join_type: str = "INNER") -> pd.DataFrame:
        """
        Join two tables using SQL.
        
        TODO: Implement using SQL JOIN:
        - Perform specified join type
        - Join on specified column
        - Return results
        
        Args:
            left_table: Left table name
            right_table: Right table name
            join_col: Column to join on
            join_type: Type of join (INNER, LEFT, RIGHT, FULL)
            
        Returns:
            Joined results as DataFrame
        """
        raise NotImplementedError("join_tables not implemented")
    
    def aggregate_data(self, table_name: str, groupby_cols: List[str],
                      agg_col: str, agg_func: str) -> pd.DataFrame:
        """
        Aggregate data using GROUP BY.
        
        TODO: Implement using SQL aggregation:
        - GROUP BY the specified columns
        - Aggregate the specified column
        - Support: SUM, AVG, COUNT, MAX, MIN
        
        Args:
            table_name: Table to aggregate
            groupby_cols: Columns to group by
            agg_col: Column to aggregate
            agg_func: Aggregation function
            
        Returns:
            Aggregated results
        """
        raise NotImplementedError("aggregate_data not implemented")
    
    def create_view(self, view_name: str, query: str) -> None:
        """
        Create a view from a query.
        
        TODO: Implement to:
        - Create SQL view
        - Store for reuse
        
        Args:
            view_name: Name for the view
            query: SQL query to define the view
        """
        raise NotImplementedError("create_view not implemented")
    
    def export_results(self, table_name: str, output_path: str,
                      format: str = "csv") -> None:
        """
        Export table to file.
        
        TODO: Implement to:
        - Export to CSV, Parquet, or JSON
        - Handle multiple formats
        
        Args:
            table_name: Table to export
            output_path: Output file path
            format: Export format (csv, parquet, json)
        """
        raise NotImplementedError("export_results not implemented")
    
    def close(self):
        """Close DuckDB connection."""
        if self.conn:
            self.conn.close()


def create_sample_data():
    """Create sample data for testing."""
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Sales data
    sales_data = {
        'sale_id': range(1, 21),
        'customer_id': [i % 5 + 1 for i in range(20)],
        'product_id': [i % 10 + 1 for i in range(20)],
        'amount': [100 + i * 25 for i in range(20)],
        'date': ['2024-01-' + f"{(i % 28) + 1:02d}" for i in range(20)]
    }
    pd.DataFrame(sales_data).to_csv(sample_dir / 'sales.csv', index=False)
    
    # Customers data
    customers_data = {
        'customer_id': range(1, 6),
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
        'city': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
    }
    pd.DataFrame(customers_data).to_csv(sample_dir / 'customers.csv', index=False)
    
    print("✓ Sample data created")


def main():
    """Main function."""
    
    print("=" * 60)
    print("Exercise 8: Using DuckDB for Analytics and Transforms")
    print("=" * 60)
    
    analyzer = None
    try:
        if not Path("sample_data").exists():
            create_sample_data()
        
        # TODO: Implement the main workflow:
        # analyzer = DuckDBAnalyzer()
        # analyzer.load_csv("sample_data/sales.csv", "sales")
        # analyzer.load_csv("sample_data/customers.csv", "customers")
        
        # TODO: Run queries and show results
        
        print("\n[INCOMPLETE] TODO: Implement the seven methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
    finally:
        if analyzer:
            analyzer.close()


if __name__ == "__main__":
    main()
