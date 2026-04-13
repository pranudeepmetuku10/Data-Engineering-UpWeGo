# Exercise 2: Web Scraping + Downloading + Pandas

## Objective

Combine web scraping, file downloading, and data processing with Pandas to extract and analyze data from multiple sources.

## Problem Description

You are tasked with building a data pipeline that:

1. Scrapes a website to find download links
2. Downloads multiple CSV/JSON files from those links
3. Processes the data using Pandas
4. Performs data aggregation and transformation
5. Outputs results to a CSV file

This is a common real-world scenario where data comes from multiple web sources that need to be consolidated.

## Requirements

- Use BeautifulSoup to parse HTML and extract links
- Download multiple files from extracted URLs
- Load data from various formats (CSV, JSON)
- Use Pandas to clean, filter, and aggregate data
- Handle missing data and inconsistencies
- Combine data from multiple sources

## Hints

- Use `BeautifulSoup` to parse HTML
- Use `requests` for HTTP operations
- Use `pandas.read_csv()` and `pandas.read_json()` for loading data
- Use `requests` or `urllib` to build and validate URLs
- Consider using `urllib.parse.urljoin()` for relative URL conversion
- Handle HTTP errors gracefully
- Use Pandas `concat()` or `merge()` to combine DataFrames

## Data

The exercise uses sample data from a realistic web source. You'll scrape links and download actual data files.

## Expected Output

After running your solution, you should have:
- Downloaded CSV/JSON files in a `data/` directory
- Aggregated data in `output/aggregated_data.csv`
- Statistics file showing data quality metrics
- Console output showing progress and summary

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

Expected output:
```
Scraping web page...
Found 5 download links
Downloading files...
✓ Downloaded: data1.csv (100 rows)
✓ Downloaded: data2.csv (150 rows)
✓ Downloaded: data3.csv (200 rows)
Loading and processing data...
✓ Loaded: 3 DataFrames (450 total rows)
Combining data...
✓ Combined: 450 rows, 5 columns
Aggregating by category...
Output saved to: output/aggregated_data.csv
Success!
```

## Bonus Challenges

1. **Error Recovery** - Implement retry logic for failed downloads
2. **Data Validation** - Add validation to check data quality before aggregation
3. **Concurrent Processing** - Download and process multiple files concurrently
4. **Caching** - Cache downloaded files to avoid re-downloading
5. **Scheduling** - Use APScheduler to run the pipeline on a schedule

## Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [HTML Parsing Tutorial](https://realpython.com/beautiful-soup-web-scraper/)

## Next Steps

Once you complete this exercise, move to Exercise 3 to learn about AWS S3 and Boto3 for cloud-based data retrieval.
