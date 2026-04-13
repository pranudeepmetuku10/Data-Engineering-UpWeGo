"""
Exercise 5: Data Modeling for Postgres + Python

Objective: Design a database schema and ingest data into Postgres.

TODO: Complete the following functions to:
1. Connect to Postgres
2. Design and create database schema
3. Load sample data from CSV
4. Ingest data with validation
5. Perform verification queries
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple
import psycopg2
from psycopg2 import sql
import pandas as pd


class PostgresDataManager:
    """Helper class for Postgres operations."""
    
    def __init__(self, host: str = None, port: int = 5432, 
                 database: str = None, user: str = None, password: str = None):
        """
        Initialize Postgres connection parameters.
        
        Args:
            host: Database host
            port: Database port
            database: Database name
            user: Database user
            password: Database password
        """
        self.host = host or os.getenv("DB_HOST", "localhost")
        self.port = port or int(os.getenv("DB_PORT", 5432))
        self.database = database or os.getenv("DB_NAME", "exercise5_db")
        self.user = user or os.getenv("DB_USER", "upwego")
        self.password = password or os.getenv("DB_PASSWORD", "upwego123")
        self.conn = None
        self.cursor = None
    
    def connect(self) -> bool:
        """
        Connect to Postgres database.
        
        TODO: Implement this method to:
        - Create connection using psycopg2.connect()
        - Store connection and cursor
        - Test connection
        - Return True if successful
        
        Returns:
            True if connection successful
        """
        # TODO: Implement connection logic
        raise NotImplementedError("connect method not implemented")
    
    def create_schema(self) -> None:
        """
        Create the database schema with all tables.
        
        TODO: Implement this method to:
        - Create Customers table (id, name, email, city, state, country)
        - Create Categories table (id, name, description)
        - Create Products table (id, name, category_id, price, stock)
        - Create Orders table (id, customer_id, date, total)
        - Create OrderItems table (id, order_id, product_id, quantity, price)
        - Add PRIMARY KEYs and FOREIGN KEYs
        - Add NOT NULL constraints
        - Create indexes on frequently queried columns
        """
        # TODO: Implement schema creation
        raise NotImplementedError("create_schema method not implemented")
    
    def load_csv_data(self, csv_path: Path) -> pd.DataFrame:
        """
        Load data from CSV file.
        
        TODO: Implement this method to:
        - Read CSV file using pandas
        - Handle missing values
        - Perform basic validation
        - Return DataFrame
        
        Args:
            csv_path: Path to CSV file
            
        Returns:
            pandas DataFrame
        """
        # TODO: Implement CSV loading
        raise NotImplementedError("load_csv_data method not implemented")
    
    def insert_data(self, table_name: str, dataframe: pd.DataFrame) -> int:
        """
        Insert DataFrame data into a table.
        
        TODO: Implement this method to:
        - Convert DataFrame to insert statements
        - Handle duplicates
        - Insert batch of rows
        - Commit transaction
        - Return number of rows inserted
        
        Args:
            table_name: Target table name
            dataframe: Data to insert
            
        Returns:
            Number of rows successfully inserted
        """
        # TODO: Implement data insertion
        raise NotImplementedError("insert_data method not implemented")
    
    def validate_data(self) -> Dict[str, any]:
        """
        Validate the ingested data.
        
        TODO: Implement this method to:
        - Run verification queries
        - Check row counts per table
        - Check foreign key relationships
        - Check for orphaned records
        - Return validation results dict
        
        Returns:
            Dictionary with validation results
        """
        # TODO: Implement data validation
        raise NotImplementedError("validate_data method not implemented")
    
    def close(self):
        """Close database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


def create_sample_data():
    """
    Create sample CSV files for data ingestion.
    """
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Create sample CSV files
    customers_data = {
        'customer_id': [1, 2, 3, 4, 5],
        'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Wilson'],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'diana@example.com', 'eve@example.com'],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'state': ['NY', 'CA', 'IL', 'TX', 'AZ'],
        'country': ['USA', 'USA', 'USA', 'USA', 'USA']
    }
    pd.DataFrame(customers_data).to_csv(sample_dir / 'customers.csv', index=False)
    
    categories_data = {
        'category_id': [1, 2, 3, 4],
        'category_name': ['Electronics', 'Books', 'Clothing', 'Home & Garden'],
        'description': ['Electronic devices', 'Books and publications', 'Clothing and accessories', 'Home and garden items']
    }
    pd.DataFrame(categories_data).to_csv(sample_dir / 'categories.csv', index=False)
    
    products_data = {
        'product_id': [1, 2, 3, 4, 5],
        'product_name': ['Laptop', 'Python Book', 'T-Shirt', 'Plant Pot', 'Mouse'],
        'category_id': [1, 2, 3, 4, 1],
        'price': [999.99, 29.99, 19.99, 15.99, 24.99],
        'stock_quantity': [50, 200, 100, 75, 150]
    }
    pd.DataFrame(products_data).to_csv(sample_dir / 'products.csv', index=False)
    
    orders_data = {
        'order_id': [1, 2, 3, 4],
        'customer_id': [1, 2, 1, 3],
        'order_date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
        'total_amount': [1029.98, 49.98, 44.98, 999.99]
    }
    pd.DataFrame(orders_data).to_csv(sample_dir / 'orders.csv', index=False)
    
    order_items_data = {
        'order_item_id': [1, 2, 3, 4, 5],
        'order_id': [1, 1, 2, 3, 4],
        'product_id': [1, 5, 2, 2, 1],
        'quantity': [1, 1, 2, 1, 1],
        'unit_price': [999.99, 24.99, 29.99, 14.99, 999.99]
    }
    pd.DataFrame(order_items_data).to_csv(sample_dir / 'order_items.csv', index=False)
    
    print("✓ Sample CSV files created in sample_data/")


def main():
    """Main function to run the Postgres exercise."""
    
    print("=" * 60)
    print("Exercise 5: Data Modeling for Postgres + Python")
    print("=" * 60)
    
    manager = None
    try:
        # Create sample data if it doesn't exist
        if not Path("sample_data").exists():
            print("\nCreating sample data...")
            create_sample_data()
        
        # TODO: Implement the main workflow:
        
        # 1. Connect to database
        # print(f"\nConnecting to Postgres database...")
        # manager = PostgresDataManager()
        # if manager.connect():
        #     print("✓ Connected to database")
        # else:
        #     raise Exception("Failed to connect to database")
        
        # 2. Create schema
        # print("\nCreating database schema...")
        # manager.create_schema()
        # print("✓ Schema created successfully")
        
        # 3. Load and ingest data
        # print("\nLoading and ingesting data...")
        # tables = ['categories', 'customers', 'products', 'orders', 'order_items']
        # total_rows = 0
        # for table in tables:
        #     csv_file = Path("sample_data") / f"{table}.csv"
        #     if csv_file.exists():
        #         df = manager.load_csv_data(csv_file)
        #         rows_inserted = manager.insert_data(table, df)
        #         total_rows += rows_inserted
        #         print(f"✓ Loaded {table}: {rows_inserted} rows")
        
        # 4. Validate data
        # print("\nValidating data...")
        # validation = manager.validate_data()
        # for table, count in validation.items():
        #     print(f"  {table}: {count} rows")
        
        # print("\n" + "=" * 60)
        # print(f"Success! Ingested {total_rows} total rows")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the five methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
    finally:
        if manager:
            manager.close()


if __name__ == "__main__":
    main()
