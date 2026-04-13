# Exercise 8: Using DuckDB for Analytics and Transforms

## Objective

Learn DuckDB, a fast SQL-based analytics engine that's perfect for in-process OLAP workloads.

## Problem Description

You need to build an analytics pipeline using DuckDB that:

1. Loads data from CSV and Parquet files
2. Performs SQL-based transformations and joins
3. Executes complex analytical queries
4. Computes aggregations and window functions  
5. Exports results in multiple formats

DuckDB provides a SQL interface and runs directly in Python without a server, making it ideal for data analysis.

## Requirements

- Load multiple data formats (CSV, Parquet, JSON)
- Execute SQL queries directly in Python
- Use advanced SQL features (CTEs, window functions, etc.)
- Perform efficient OLAP operations
- Write results to multiple formats
- Handle in-memory and larger-than-memory datasets
- Work with relational algebra operations

## Hints

- Use `duckdb.sql()` for SQL queries
- Use `duckdb.from_df()` for Pandas DataFrames
- Use `duckdb.read_csv()` or `duckdb.read_parquet()` for file loading
- SQL syntax is similar to Postgres but with some extensions
- Use `COPY` for exporting data
- DuckDB has excellent Pandas integration
- Use `.df()` to convert results back to Pandas

## Data

Sample data: Sales, customers, products data in CSV format.

## Expected Output

After running your solution, you should have:
- Loaded data from multiple sources
- Complex analytical results
- Joined datasets with proper relationships
- Aggregations and metrics
- Exported results in multiple formats
- Performance benchmarks

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

## Bonus Challenges

1. **Complex CTEs** - Multi-level common table expressions
2. **JSON Support** - Work with JSON data types
3. **Approximations** - Use approximate aggregations for speed
4. **Performance** - Optimize query execution
5. **Partitioned Reads** - Work with partitioned Parquet files

## Resources

- [DuckDB Documentation](https://duckdb.org/docs/)
- [DuckDB SQL Reference](https://duckdb.org/docs/sql/introduction.html)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview.html)
- [Getting Started](https://duckdb.org/docs/guides/getting_started.html)

## Next Steps

Complete this exercise to move to Exercise 9 on Polars.
