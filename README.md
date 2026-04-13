# Data Engineering Practice Problems

Welcome to the Data Engineering Practice Problems repository! This repository contains 10 hands-on exercises designed to help you develop the diverse technical skills required in modern data engineering.

## Overview

One of the main obstacles of Data Engineering is the large and varied technical skills that can be required on a day-to-day basis. This repository aims to help you master those skills through practical, real-world exercises.

**Note:** If you complete all exercises and share your GitHub repo, you can receive a free copy of "Introduction to Data Engineering"!

## Topics Covered

- **Python Data Processing** - CSV, flat-file, Parquet, JSON
- **SQL & Database Design** - Table design, normalization, indexing
- **Data Ingestion** - Python + Postgres, APIs, cloud storage
- **PySpark** - Distributed processing and aggregations
- **Data Cleansing** - Handling dirty data and quality issues
- **Modern Tools** - DuckDB, Polars, Great Expectations

## Prerequisites

Before getting started, ensure you have installed:

- **Docker** - For containerized environments
- **Docker Compose** - For orchestrating multi-container setups
- **Git** - For version control
- **Python 3.9+** - Local development (optional, Docker includes it)

### Installation

**macOS (using Homebrew):**
```bash
brew install docker docker-compose git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install docker.io docker-compose git
curl https://get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER
```

**Windows:**
Download and install Docker Desktop from https://www.docker.com/products/docker-desktop

## Exercise Structure

Each exercise is located in `Exercises/Exercise-N/` and contains:

- **README.md** - Problem description, requirements, and hints
- **Dockerfile** - Container setup with all dependencies
- **docker-compose.yml** - Container orchestration (if needed)
- **requirements.txt** - Python package dependencies
- **solution.py** - Starter code with TODO placeholders
- **sample_data/** - Sample data files for testing (where applicable)

## How to Work on the Problems

1. Navigate to the exercise folder:
   ```bash
   cd Exercises/Exercise-1
   ```

2. Read the README.md for detailed instructions

3. Build and run the Docker environment:
   ```bash
   docker-compose build
   docker-compose run app python solution.py
   ```

4. Edit `solution.py` to implement the required functionality

5. Test your solution:
   ```bash
   docker-compose run app python solution.py
   ```

## Exercises

### Beginner Exercises

#### [Exercise 1 - Downloading Files](./Exercises/Exercise-1/README.md)
Learn to download files from HTTP sources, unzip them, and store them locally using Python.

**Skills:** HTTP requests, file I/O, zip handling

#### [Exercise 2 - Web Scraping + Downloading + Pandas](./Exercises/Exercise-2/README.md)
Practice web scraping, URI building, file downloads, and basic data aggregation with Pandas.

**Skills:** Web scraping, HTTP requests, Pandas, data aggregation

#### [Exercise 3 - Boto3 AWS + S3 + Python](./Exercises/Exercise-3/README.md)
Work with AWS S3 using Boto3 to perform multi-step data retrieval from cloud storage.

**Skills:** AWS, S3, Boto3, cloud storage

#### [Exercise 4 - Convert JSON to CSV](./Exercises/Exercise-4/README.md)
Traverse ragged directory structures, find JSON files, and convert them to CSV format.

**Skills:** File traversal, JSON/CSV handling, Python file operations

#### [Exercise 5 - Data Modeling for Postgres](./Exercises/Exercise-5/README.md)
Design a database schema, create tables in Postgres, and perform data ingestion via Python.

**Skills:** Database design, schema modeling, SQL, Python + Postgres, indexing

### Intermediate Exercises

#### [Exercise 6 - Ingestion and Aggregation with PySpark](./Exercises/Exercise-6/README.md)
Load data files using PySpark and perform basic aggregations on distributed data.

**Skills:** PySpark, data loading, aggregations, distributed processing

#### [Exercise 7 - Using Various PySpark Functions](./Exercises/Exercise-7/README.md)
Apply multiple PySpark SQL functions to solve real-life data problems.

**Skills:** PySpark SQL functions, transformations, problem-solving

#### [Exercise 8 - DuckDB for Analytics and Transforms](./Exercises/Exercise-8/README.md)
Perform analytical and transformation tasks using DuckDB, a modern SQL engine.

**Skills:** DuckDB, SQL analytics, data transformation, query optimization

#### [Exercise 9 - Polars Lazy Computation](./Exercises/Exercise-9/README.md)
Master Polars, a Rust-based data processing library with lazy evaluation for larger-than-memory datasets.

**Skills:** Polars, lazy evaluation, SQL context, performance optimization

### Advanced Exercises

#### [Exercise 10 - Data Quality with Great Expectations](./Exercises/Exercise-10/README.md)
Implement data quality checks using Great Expectations to identify and catch data issues.

**Skills:** Data quality, Great Expectations, validation, testing

## Quick Start

Get started with Exercise 1:

```bash
cd Exercises/Exercise-1
docker-compose build
docker-compose run app python solution.py
```

Then open `solution.py` and fill in the TODO sections.

## Local Development (Optional)

If you prefer to run exercises locally without Docker:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r Exercises/Exercise-1/requirements.txt
python Exercises/Exercise-1/solution.py
```

## Project Structure

```
Data-Engineering-UpWeGo/
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
├── Exercises/
│   ├── Exercise-1/              # Downloading files
│   ├── Exercise-2/              # Web scraping + Pandas
│   ├── Exercise-3/              # AWS Boto3 + S3
│   ├── Exercise-4/              # JSON to CSV conversion
│   ├── Exercise-5/              # Postgres data modeling
│   ├── Exercise-6/              # PySpark ingestion
│   ├── Exercise-7/              # PySpark functions
│   ├── Exercise-8/              # DuckDB analytics
│   ├── Exercise-9/              # Polars lazy computation
│   └── Exercise-10/             # Data quality checks
```

## Resources

### Python
- [Python Official Docs](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)

### Data Processing
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Polars Documentation](https://pola-rs.github.io/polars/py-polars/)
- [DuckDB Documentation](https://duckdb.org/docs/)

### Database
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

### Cloud & DevOps
- [AWS Documentation](https://docs.aws.amazon.com/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Docker Documentation](https://docs.docker.com/)

### Data Quality
- [Great Expectations Documentation](https://docs.greatexpectations.io/)

## Getting Help

- Check the README.md in each exercise folder for detailed guidance
- Look at the hints section in each exercise
- Review the starter code comments for additional context
- Search for error messages in the documentation links above

## Contributing

Feel free to fork this repository and submit pull requests with improvements, additional exercises, or corrections.

## License

This project is open source and available under the MIT License.

---

**Ready to level up your Data Engineering skills? Start with [Exercise 1](./Exercises/Exercise-1/README.md)!**
