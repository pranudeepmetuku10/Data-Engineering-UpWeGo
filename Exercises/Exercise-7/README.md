# Exercise 7: Using Various PySpark Functions

## Objective

Master advanced PySpark SQL functions for real-world data transformation and analysis tasks.

## Problem Description

You need to build a complex data transformation pipeline using PySpark that:

1. Uses multiple PySpark SQL functions
2. Performs conditional transformations
3. Handles string operations
4. Works with dates and timestamps
5. Creates computed columns
6. Handles nulls and edge cases

This teaches you to solve complex problems by combining multiple functions creatively.

## Key Functions to Use

- String Functions: `concat`, `upper`, `lower`, `substring`, `trim`, `split`
- Math Functions: `round`, `abs`, `power`, `sqrt`
- Date Functions: `current_date`, `datediff`, `date_add`, `date_format`
- Conditional Functions: `when`, `case`, `coalesce`, `ifnull`
- Array Functions: `array`, `explode`, `size`, `array_contains`
- Window Functions: `row_number`, `rank`, `lead`, `lag`
- Aggregation Functions: `collect_list`, `collect_set`

## Requirements

- Use 5+ different PySpark SQL functions
- Combine functions to solve complex problems
- Handle data type conversions
- Perform string transformations
- Calculate derived metrics
- Handle null values appropriately
- Optimize query performance

## Hints

- Import from `pyspark.sql.functions` for F.function_name()
- String functions: F.concat, F.upper, F.lower, F.trim, F.split
- Use F.when().otherwise() for conditional logic
- Date functions: F.current_date(), F.datediff(), F.date_add()
- Window functions need a Window.partitionBy() specification
- Use `.alias()` to name computed columns
- Chain functions together for complex transformations

## Expected Tasks

1. Transform customer names to title case
2. Calculate customer lifetime value (CLV)
3. Extract year from date columns
4. Use row_number for ranking
5. Handle multiple data types in transformations
6. Create complex business logic calculations

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

## Bonus Challenges

1. **Complex Case Statements** - Nested conditions
2. **String Parsing** - Extract/parse complex string patterns
3. **Date Calculations** - Age, tenure, elapsed time calculations
4. **Array Operations** - Multi-value handling
5. **Performance Tuning** - Optimize complex queries

## Resources

- [PySpark SQL Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html)
- [Window Functions Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html#window-functions)

## Next Steps

Complete this exercise to prepare for Exercise 8 on DuckDB.
