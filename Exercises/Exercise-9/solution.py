"""
Exercise 9: Using Polars Lazy Computation

Objective: Use Polars for efficient data processing with lazy evaluation.

TODO: Complete the following functions to:
1. Load data using Polars
2. Use lazy evaluation
3. Chain operations efficiently
4. Perform aggregations
5. Compare eager vs lazy performance
"""

import time
from pathlib import Path
from typing import Dict, List
import polars as pl
import pandas as pd


class PolarsDataProcessor:
    """Polars-based data processing with lazy evaluation."""
    
    def __init__(self, data_dir: str = "sample_data", output_dir: str = "results"):
        """
        Initialize Polars processor.
        
        Args:
            data_dir: Directory containing data files
            output_dir: Directory for output files
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def load_lazy(self, file_path: str) -> pl.LazyFrame:
        """
        Load data using lazy evaluation.
        
        TODO: Implement to:
        - Use pl.scan_csv() for lazy loading
        - Return LazyFrame without executing
        - Handle different file formats
        
        Args:
            file_path: Path to data file
            
        Returns:
            Polars LazyFrame
        """
        raise NotImplementedError("load_lazy not implemented")
    
    def load_eager(self, file_path: str) -> pl.DataFrame:
        """
        Load data using eager evaluation.
        
        TODO: Implement to:
        - Use pl.read_csv() for immediate loading
        - Return DataFrame
        
        Args:
            file_path: Path to data file
            
        Returns:
            Polars DataFrame
        """
        raise NotImplementedError("load_eager not implemented")
    
    def lazy_aggregation(self, lf: pl.LazyFrame, groupby_col: str,
                        agg_col: str, agg_func: str) -> pl.DataFrame:
        """
        Perform aggregation using lazy evaluation.
        
        TODO: Implement using lazy API:
        - Use .lazy() if needed
        - Use .group_by() for grouping
        - Use .agg() with pl.col() and aggregation function
        - Use .collect() to execute the query
        
        Args:
            lf: LazyFrame to aggregate
            groupby_col: Column to group by
            agg_col: Column to aggregate
            agg_func: Aggregation function (sum, mean, count, etc.)
            
        Returns:
            Results as DataFrame
        """
        raise NotImplementedError("lazy_aggregation not implemented")
    
    def lazy_filter_join(self, lf1: pl.LazyFrame, lf2: pl.LazyFrame,
                        join_col: str = "id") -> pl.DataFrame:
        """
        Filter and join two lazy frames.
        
        TODO: Implement lazy join:
        - Filter data before join (pushed down in optimization)
        - Use .join() on lazy frames
        - Call .collect() once at the end
        
        Args:
            lf1: First LazyFrame
            lf2: Second LazyFrame
            join_col: Column to join on
            
        Returns:
            Joined results
        """
        raise NotImplementedError("lazy_filter_join not implemented")
    
    def compare_performance(self, file_path: str) -> Dict[str, float]:
        """
        Compare eager vs lazy evaluation performance.
        
        TODO: Implement to:
        - Time eager loading and processing
        - Time lazy loading and processing
        - Return dict with timing results
        
        Args:
            file_path: Path to data file
            
        Returns:
            Dictionary with timing metrics
        """
        raise NotImplementedError("compare_performance not implemented")
    
    def explain_query(self, lf: pl.LazyFrame) -> str:
        """
        Show the execution plan for a lazy query.
        
        TODO: Implement to:
        - Use .explain() to show query plan
        - Display optimization details
        
        Args:
            lf: LazyFrame to explain
            
        Returns:
            Explanation string
        """
        raise NotImplementedError("explain_query not implemented")


def create_sample_data():
    """Create sample data for testing."""
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Create larger sample dataset
    n_rows = 10000
    transactions_data = {
        'transaction_id': range(1, n_rows + 1),
        'customer_id': [i % 1000 for i in range(n_rows)],
        'amount': [100 + (i % 1000) for i in range(n_rows)],
        'date': ['2024-' + f"{(i % 12) + 1:02d}-" + f"{(i % 28) + 1:02d}" for i in range(n_rows)],
        'category': [['Electronics', 'Books', 'Clothing', 'Food'][i % 4] for i in range(n_rows)]
    }
    pd.DataFrame(transactions_data).to_csv(sample_dir / 'transactions.csv', index=False)
    
    customers_data = {
        'customer_id': range(1, 1001),
        'name': [f"Customer_{i}" for i in range(1, 1001)],
        'region': [[['North', 'South', 'East', 'West'][i % 4] for i in range(1, 1001)]][0]
    }
    pd.DataFrame(customers_data).to_csv(sample_dir / 'customers.csv', index=False)
    
    print("✓ Sample data created")


def main():
    """Main function."""
    
    print("=" * 60)
    print("Exercise 9: Using Polars Lazy Computation")
    print("=" * 60)
    
    try:
        if not Path("sample_data").exists():
            create_sample_data()
        
        processor = PolarsDataProcessor()
        
        # TODO: Implement the main workflow:
        # 1. Load data lazily
        # 2. Perform lazy aggregations
        # 3. Compare eager vs lazy performance
        # 4. Show execution plans
        # 5. Export results
        
        print("\n[INCOMPLETE] TODO: Implement the six methods above")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
