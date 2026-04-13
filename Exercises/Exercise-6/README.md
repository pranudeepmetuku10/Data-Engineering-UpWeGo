# Exercise 6: Ingestion and Aggregation with PySpark

## Objective

Learn to use PySpark for distributed data processing, loading files, and performing aggregations at scale.

## Problem Description

You are tasked with building a PySpark pipeline that:

1. Loads multiple data files in various formats
2. Performs data ingestion into Spark DataFrames
3. Cleans and transforms data at scale
4. Performs complex aggregations
5. Writes results to multiple output formats

This demonstrates real-world data processing using distributed computing frameworks.

## Requirements

- Initialize a Spark Session
- Load data from CSV, Parquet, JSON formats
- Create and manipulate Spark DataFrames
- Perform aggregations (groupBy, sum, count, avg)
- Join multiple datasets
- Cache DataFrames for performance
- Write output in multiple formats
- Handle large datasets efficiently

## Hints

- Use `SparkSession.builder` to create session
- Use `spark.read` with format options
- Use `.groupBy()` and `.agg()` for aggregations
- Use `.select()` and `.filter()` for transformations
- Cache DataFrames with `.cache()` before multiple operations
- Use `.coalesce()` or `.repartition()` for optimization
- Avoid `collect()` on large DataFrames
- Use `.explain()` to understand execution plans

## Data

The exercise includes sample sales data with:
- Orders (order_id, customer_id, amount, date)
- Products (product_id, category, price)
- Customers (customer_id, region, signup_date)

## Expected Output

After running your solution, you should have:
- Loaded data from multiple sources
- Aggregated sales figures
- Generated regional summaries
- Saved results in multiple formats
- Performance metrics shown

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

Expected output:
```
Loading data files...
✓ Loaded orders: 100,000 rows
✓ Loaded products: 1,000 rows
✓ Loaded customers: 10,000 rows
Performing aggregations...
✓ Total sales: $2,543,210.50
✓ Orders by region: 5 regions
✓ Top products: 10 items
Writing results...
✓ Saved to: results/
Success!
```

## Bonus Challenges

1. **Window Functions** - Use window functions for running totals
2. **User Defined Functions** - Create UDFs for custom logic
3. **Streaming** - Use PySpark Streaming for real-time processing
4. **Machine Learning** - Use MLlib for predictive analytics
5. **Delta Lake** - Save to Delta format for ACID transactions
6. **JDBC/Databases** - Write directly to Postgres or MySQL

## Resources

- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [PySpark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [PySpark RDD vs DataFrame](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

## Next Steps

Once you complete this exercise, move to Exercise 7 to learn about advanced PySpark SQL functions.
