"""
Exercise 10: Data Quality with Great Expectations

Objective: Implement comprehensive data quality checks using Great Expectations.

TODO: Complete the following functions to:
1. Load data and identify issues
2. Create an expectation suite
3. Define quality expectations
4. Validate data
5. Generate quality reports
6. Handle failures
"""

from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd
import great_expectations as ge
from great_expectations.core.batch import RuntimeBatchRequest


class DataQualityValidator:
    """Data quality validation using Great Expectations."""
    
    def __init__(self, data_dir: str = "sample_data", output_dir: str = "validation_reports"):
        """
        Initialize validator.
        
        Args:
            data_dir: Directory with data files
            output_dir: Directory for validation reports
        """
        self.data_dir = Path(data_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.context = None
    
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data file.
        
        TODO: Implement to:
        - Read CSV file
        - Return DataFrame
        
        Args:
            file_path: Path to data file
            
        Returns:
            Loaded DataFrame
        """
        raise NotImplementedError("load_data not implemented")
    
    def create_expectation_suite(self, suite_name: str) -> None:
        """
        Create an expectation suite.
        
        TODO: Implement to:
        - Initialize Great Expectations context
        - Create new expectation suite
        - Store suite reference
        
        Args:
            suite_name: Name for the expectation suite
        """
        raise NotImplementedError("create_expectation_suite not implemented")
    
    def add_column_expectations(self, dataset, column_name: str,
                               expectation_type: str, **kwargs) -> None:
        """
        Add expectations for a column.
        
        TODO: Implement to:
        - Use ge.from_pandas() to wrap DataFrame
        - Add specific column expectations:
          - expect_column_to_exist()
          - expect_column_values_to_not_be_null()
          - expect_column_values_to_be_in_set()
          - expect_column_values_to_be_between()
          - expect_column_values_to_be_of_type()
        
        Args:
            dataset: Great Expectations dataset
            column_name: Column to validate
            expectation_type: Type of expectation
            **kwargs: Additional parameters for expectation
        """
        raise NotImplementedError("add_column_expectations not implemented")
    
    def add_table_expectations(self, dataset) -> None:
        """
        Add table-level expectations.
        
        TODO: Implement to:
        - expect_table_row_count_to_be_between()
        - expect_table_columns_to_match_ordered_list()
        - expect_table_columns_to_exist()
        
        Args:
            dataset: Great Expectations dataset
        """
        raise NotImplementedError("add_table_expectations not implemented")
    
    def validate_data(self, df: pd.DataFrame) -> Dict:
        """
        Validate data against expectation suite.
        
        TODO: Implement to:
        - Convert DataFrame to GE dataset
        - Run validation
        - Collect results
        - Return validation report
        
        Args:
            df: DataFrame to validate
            
        Returns:
            Validation results dictionary
        """
        raise NotImplementedError("validate_data not implemented")
    
    def identify_issues(self, validation_results: Dict) -> Dict[str, List]:
        """
        Identify and categorize data quality issues.
        
        TODO: Implement to:
        - Parse validation results
        - Extract failed expectations
        - Categorize issues
        - Return issue summary
        
        Args:
            validation_results: Results from validation
            
        Returns:
            Dictionary of identified issues
        """
        raise NotImplementedError("identify_issues not implemented")
    
    def generate_report(self, validation_results: Dict, output_filename: str) -> str:
        """
        Generate data quality report.
        
        TODO: Implement to:
        - Create summary of validation
        - Generate HTML report
        - Save report to file
        - Return report path
        
        Args:
            validation_results: Validation results
            output_filename: Name for output file
            
        Returns:
            Path to generated report
        """
        raise NotImplementedError("generate_report not implemented")


def create_dirty_sample_data():
    """Create sample data with intentional quality issues."""
    sample_dir = Path("sample_data")
    sample_dir.mkdir(parents=True, exist_ok=True)
    
    # Create data with known quality issues
    customers_data = {
        'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, None],  # Issue: Missing ID
        'name': ['Alice', 'Bob', None, 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack'],  # Issue: Missing name
        'email': ['alice@example.com', None, None, 'diana@example.com', 'invalid-email', 
                 'frank@example.com', None, 'henry@example.com', 'iris@example.com', 'jack@example.com'],  # Issues: Missing and invalid
        'age': [30, 25, 35, 28, None, 150, 32, 29, 26, 31],  # Issues: Missing, out of range (150)
        'signup_date': ['2023-01-01', '2023-02-15', None, '2023-04-20', '2023-05-10',
                       '2023-06-01', '2023-07-15', '2023-08-20', '2023-09-10', '2023-10-05'],  # Issue: Missing date
        'status': ['active', 'active', 'inactive', 'active', 'active', 'active', 'inactive', 'active', None, 'active']  # Issue: Missing status
    }
    
    pd.DataFrame(customers_data).to_csv(sample_dir / 'customers_dirty.csv', index=False)
    print("✓ Dirty sample data created with known quality issues")


def main():
    """Main function."""
    
    print("=" * 60)
    print("Exercise 10: Data Quality with Great Expectations")
    print("=" * 60)
    
    validator = None
    try:
        # Create sample data with quality issues
        if not Path("sample_data").exists():
            print("\nCreating sample data with quality issues...")
            create_dirty_sample_data()
        
        # TODO: Implement the main workflow:
        # validator = DataQualityValidator()
        
        # 1. Load the data
        # print("\nLoading data...")
        # df = validator.load_data("sample_data/customers_dirty.csv")
        # print(f"✓ Loaded {len(df)} rows")
        
        # 2. Create expectation suite
        # print("\nCreating expectation suite...")
        # validator.create_expectation_suite("customer_quality")
        
        # 3. Add expectations
        # print("\nAdding quality expectations...")
        # TODO: Add various expectations
        
        # 4. Validate data
        # print("\nValidating data...")
        # results = validator.validate_data(df)
        
        # 5. Identify issues
        # print("\nIdentifying data quality issues...")
        # issues = validator.identify_issues(results)
        # for issue_type, details in issues.items():
        #     print(f"  - {issue_type}: {details}")
        
        # 6. Generate report
        # print("\nGenerating quality report...")
        # report_path = validator.generate_report(results, "quality_report.html")
        # print(f"✓ Report saved to: {report_path}")
        
        # print("\n" + "=" * 60)
        # print("Success! Data quality validation completed")
        # print("=" * 60)
        
        print("\n[INCOMPLETE] TODO: Implement the seven methods above")
        print("\nThis exercise demonstrates:")
        print("  - Data quality validation")
        print("  - Great Expectations framework")
        print("  - Quality metrics and reporting")
        print("  - Issue detection and categorization")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        raise
    finally:
        if validator:
            pass  # Clean up if needed


if __name__ == "__main__":
    main()
