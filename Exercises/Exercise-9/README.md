# Exercise 9: Using Polars Lazy Computation

## Objective

Master Polars, a modern Rust-based data processing library with SQL context and lazy evaluation for handling larger-than-memory datasets efficiently.

## Problem Description

You need build a data processing pipeline using Polars that:

1. Loads data from multiple formats
2. Uses lazy evaluation for query optimization
3. Performs complex transformations
4. Executes efficient aggregations
5. Handles data larger than available memory
6. Compares eager vs lazy evaluation performance

Polars is faster than Pandas for large datasets and supports both eager (immediate) and lazy (deferred) execution.

## Requirements

- Use lazy evaluation with `.lazy()`
- Chain multiple operations before `.collect()`
- Perform filtered aggregations efficiently
- Join large datasets
- Handle missing values
- Compare performance metrics
- Export results in multiple formats

## Key Concepts

**Lazy Evaluation:** Operations are not executed immediately. Instead, they're optimized and executed when `.collect()` is called.

**Query Optimization:** Polars optimizes the entire execution plan before running.

**Advantages Over Pandas:**
- Faster execution on large datasets
- Lower memory usage
- Support for larger-than-memory processing
- Better type safety with schemas
- Multi-threaded operations

## Hints

- Use `pl.lazy()` to enable lazy evaluation
- Chain methods without `.collect()` until the end
- Use `pl.Expr` for column expressions
- Use `.with_columns()` for adding computed columns
- Use `.group_by()` for aggregations
- Use `.filter()` for where clauses
- Use `.join()` for table joins
- Profile with `.explain()` to see execution plans

## Data

Sample data: Multiple CSV files with customer, transaction, and product information.

## Expected Output

After running your solution, you should have:
- Lazy query execution results
- Performance comparison (eager vs lazy)
- Complex transformations applied
- Aggregated metrics
- Exported results in Parquet format
- Execution plans shown

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

## Bonus Challenges

1. **Streaming** - Use Polars Streaming API
2. **SQL Context** - Use Polars SQL interface
3. **Custom Functions** - Define and use custom functions
4. **Schema Definition** - Use explicit schema for data loading
5. **Partitioning** - Work with partitioned datasets
6. **Arrow Integration** - Use Apache Arrow for zero-copy reads

## Resources

- [Polars Documentation](https://pola-rs.github.io/polars/py-polars/)
- [Lazy Evaluation Guide](https://pola-rs.github.io/polars/user-guide/lazy-api/)
- [Performance Tips](https://pola-rs.github.io/polars/user-guide/performance/)
- [SQL API](https://pola-rs.github.io/polars/user-guide/expressions/sql/)

## Next Steps

Complete this exercise to move to the Advanced Exercise 10 on Data Quality with Great Expectations.
