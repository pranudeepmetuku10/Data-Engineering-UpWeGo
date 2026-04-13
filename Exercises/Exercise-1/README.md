# Exercise 1: Downloading Files

## Objective

Learn to download files from HTTP sources, unzip them, and store them locally using Python. This is a fundamental skill in data engineering for retrieving raw data from various sources.

## Problem Description

You are given a URL that points to a compressed archive containing multiple data files. Your task is to:

1. Download the compressed file from the provided URL
2. Save it locally
3. Extract/unzip the contents
4. Organize the extracted files in a designated directory
5. Verify that all files were extracted successfully

## Requirements

- Download files from HTTP endpoints
- Handle zip file extraction
- Create and manage local directories
- Implement error handling (network failures, invalid files, etc.)
- Log or output progress information

## Hints

- Use the `requests` library for HTTP downloads
- Use the `zipfile` module for extraction
- Use `os` or `pathlib` for directory operations
- Consider implementing a progress bar using `tqdm` for large files
- Always handle exceptions gracefully

## Data

The exercise uses sample data from a public source. The download URL and expected files are specified in the starter code.

## Expected Output

After running your solution, you should have:
- A `downloads/` directory with extracted files
- Console output showing download progress
- A summary of all extracted files

## Testing Your Solution

```bash
docker-compose build
docker-compose run app python solution.py
```

You should see output similar to:
```
Downloading file from URL...
Downloaded: sample_data.zip (X bytes)
Extracting files...
Extracted: file1.csv
Extracted: file2.json
Extracted: file3.txt
Total files extracted: 3
Success!
```

## Bonus Challenges

1. **Retry Logic** - Implement automatic retry on download failure (with exponential backoff)
2. **Checksum Verification** - Verify the integrity of downloaded files using checksums
3. **Concurrent Downloads** - Download multiple files simultaneously using `concurrent.futures`
4. **Resume Downloads** - Implement resumable downloads for large files
5. **S3 Alternative** - Instead of HTTP, download from AWS S3

## Resources

- [Requests Documentation](https://docs.python-requests.org/)
- [Zipfile Documentation](https://docs.python.org/3/library/zipfile.html)
- [Pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [TQDM Progress Bar](https://tqdm.github.io/)

## Next Steps

Once you complete this exercise, move to Exercise 2 to learn about web scraping in combination with file downloading.
