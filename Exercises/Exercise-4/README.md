# Exercise 4: Convert JSON to CSV + Ragged Directories

## Objective

Learn to traverse complex directory structures and convert between data formats (JSON to CSV).

## Problem Description

You are given a directory structure containing JSON files at various levels and with varying structures (ragged/non-uniform). Your task is to:

1. Recursively traverse a directory tree
2. Find all JSON files regardless of depth
3. Parse JSON files with different structures
4. Convert each to CSV format
5. Handle missing columns and nested data
6. Organize output files logically

This is common in real-world scenarios where data comes from different sources with inconsistent schemas.

## Requirements

- Recursively traverse directories
- Handle all JSON file locations
- Parse JSON with various structures
- Normalize JSON to tabular format (CSV)
- Handle nested JSON objects/arrays
- Deal with missing columns across files
- Create consistent output structure
- Handle errors gracefully

## Hints

- Use `pathlib.Path.glob()` or `os.walk()` for directory traversal
- Use `json.load()` for parsing JSON files
- Flatten nested JSON using functions or Pandas utilities
- Use `pd.json_normalize()` for automatic JSON flattening
- Handle lists in JSON by creating separate rows
- Use `pd.concat()` to handle varying columns
- Fill missing values consistently

## Data

Sample data: The exercise includes a `sample_data/` directory with JSON files at various depths and with different structures.

## Expected Output

After running your solution, you should have:
- A `csv_output/` directory matching the input structure
- CSV files converted from JSON with consistent schema
- A mapping file showing conversions performed
- Summary statistics on files processed

## Testing Your Solution

Create sample JSON data first (or it will be provided), then:

```bash
docker-compose build
docker-compose run app python solution.py
```

Expected output:
```
Traversing directory structure...
Found JSON files:
  - sample_data/data/file1.json
  - sample_data/nested/file2.json
  - sample_data/nested/deep/file3.json
Converting JSON to CSV...
✓ Converted: file1.json → file1.csv (100 rows)
✓ Converted: file2.json → file2.csv (50 rows)
✓ Converted: file3.json → file3.csv (75 rows)
Total: 3 files converted, 225 rows processed
Success!
```

## Bonus Challenges

1. **Nested Data** - Handle deeply nested JSON structures
2. **Array Flattening** - Properly flatten arrays within JSON
3. **Schema Validation** - Validate JSON against a schema before conversion
4. **Parallel Processing** - Convert multiple files concurrently
5. **Format Detection** - Auto-detect and handle JSON errors
6. **Compression** - Output to compressed CSV files (gzip)

## Resources

- [Pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [JSON Documentation](https://docs.python.org/3/library/json.html)
- [Pandas json_normalize](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)
- [Directory Traversal Guide](https://realpython.com/python-pathlib/)

## Next Steps

Once you complete this exercise, move to Exercise 5 to learn about database design and data modeling with Postgres.
