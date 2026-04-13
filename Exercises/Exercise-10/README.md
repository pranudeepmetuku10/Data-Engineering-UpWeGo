# Exercise 10: Data Quality with Great Expectations

## Objective

Implement comprehensive data quality checks using Great Expectations to catch data issues and maintain high data standards.

## Problem Description

You are given an existing data pipeline with data quality issues. You need to:

1. Define data quality expectations (validations)
2. Create a suite of validation rules
3. Execute the validation suite against data
4. Create data documentation
5. Handle and report validation failures
6. Implement corrective actions

This demonstrates a critical aspect of modern data engineering: ensuring data quality throughout the pipeline.

## Requirements

- Define Expectations for tables and columns
- Create ExpectationSuite
- Validate against real data
- Generate data quality reports
- Handle missing values
- Check value ranges and types
- Validate relationships between fields
- Document data quality issues
- Implement retry/correction logic

## Common Expectations to Implement

- `expect_column_to_exist()` - Column exists
- `expect_column_values_to_be_in_set()` - Values in allowed set
- `expect_column_values_to_be_between()` - Values in range
- `expect_column_values_to_not_be_null()` - No missing values
- `expect_table_row_count_to_be_between()` - Row count in range
- `expect_column_values_to_be_unique()` - Unique values
- `expect_column_values_to_match_regex()` - Pattern matching
- `expect_table_columns_to_match_ordered_list()` - Schema validation

## Hints

- Use `PandasDataset` for data frame validation
- Use `ge.from_pandas()` to wrap DataFrames
- Create `ExpectationSuite` with multiple expectations
- Use `validate()` to run checks
- Configure `ExpectationEngineForDataFrames`
- Handle validation results with checkpoints
- Generate HTML reports for documentation
- Use data_asset_name for identification

## Data

The exercise includes a CSV file with intentional data quality issues:
- Missing values in key columns
- Out-of-range values
- Invalid formats
- Duplicate records
- Inconsistent data types

## Expected Output

After running your solution, you should have:
- Created validation rules for your data
- Executed validation suite showing failures
- Generated data quality report
- Identified all data issues
- Proposed corrective actions
- Created documentation of findings

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

Expected output:
```
Loading data...
✓ Loaded dirty_data.csv
Creating expectations...
✓ Created expectation suite
Running validation...
✓ Validation complete
Results:
  Total checks: 15
  Passed: 11
  Failed: 4
Issues found:
  - Missing email_addresses: 3 rows
  - Invalid ages (>150): 2 rows
  - Duplicate customer IDs: 1 occurrence
  - Invalid phone format: 5 rows
Report saved to: validation_report.html
```

## Bonus Challenges

1. **Custom Expectations** - Define your own validation logic
2. **Batch Processing** - Validate multiple tables
3. **Profiling** - Auto-generate expectations from data
4. **Store Metrics** - Store historical validation metrics
5. **Automated Fixes** - Attempt to fix common issues
6. **Alerts** - Send alerts on validation failures

## Resources

- [Great Expectations Documentation](https://docs.greatexpectations.io/)
- [Core Concepts](https://docs.greatexpectations.io/docs/guides/setup/set_up_a_gx_project)
- [Expectations](https://docs.greatexpectations.io/docs/reference/expectations/expectations)
- [Validation](https://docs.greatexpectations.io/docs/guides/validation/validate_your_data)

## Congratulations!

Completing this exercise finishes the entire Data Engineering Practice suite! You've now learned:

✓ File downloading and extraction  
✓ Web scraping and data integration  
✓ Cloud storage (AWS S3)  
✓ Data format conversion  
✓ Database design and SQL  
✓ Distributed processing (PySpark)  
✓ Modern analytics tools (DuckDB, Polars)  
✓ Data quality and validation  

You're now well-equipped to tackle real data engineering challenges!
