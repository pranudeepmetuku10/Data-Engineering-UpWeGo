# 🚀 Data Engineering Practice Problems

> **Master 10 Essential Data Engineering Skills Through Hands-On Exercises**

![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![License](https://img.shields.io/badge/License-MIT-blue) ![Docker](https://img.shields.io/badge/Container-Docker-blue) ![Python](https://img.shields.io/badge/Python-3.9+-yellow)

## Welcome! 👋

Welcome to the **Data Engineering Practice Problems** repository! This is a comprehensive, hands-on learning platform with **10 carefully curated exercises** designed to help you master the fundamental skills required in modern data engineering.

### Why This Project?

Data Engineering requires a **diverse technical toolkit**. It's rare to be proficient in just one area. This project takes you on a guided journey through:

- ✨ **Web APIs & Data Collection** - HTTP requests, web scraping
- 🏗️ **Data Processing** - Pandas, Polars, PySpark
- ☁️ **Cloud Infrastructure** - AWS S3, Boto3
- 🗄️ **Database Engineering** - PostgreSQL, schema design
- ⚡ **Distributed Processing** - Apache Spark, DuckDB
- 🔍 **Data Quality** - Validation, testing, Great Expectations
- 📊 **Modern Tools** - Polars, DuckDB, lazy evaluation

**All exercises are containerized with Docker** for guaranteed reproducibility.

---

## 🛠 Tech Stack Overview

```
    COLLECT        PROCESS        STORE        ANALYZE        SERVE
       │               │             │             │             │
       ▼               ▼             ▼             ▼             ▼
    ┌─────┐        ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐
    │ API │───────→│ ETL │────→│ DB  │────→│PySpark│────→│ API │
    └─────┘        └─────┘      └─────┘      └─────┘      └─────┘
       ▲               ▲             ▲             ▲             ▲
    S3 | Files    Clean | Transform Indexes    Analytics     Reports
```

**Note:** If you complete all exercises and share your GitHub repo, you can receive a free copy of "Introduction to Data Engineering"!

---

## 🎯 Topics Covered

```
┌──────────────────────────────────────────────────────────────┐
│  SKILL TREE                                                  │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ✦ Python Data Processing    ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Web APIs & Web Scraping   ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Cloud Storage (AWS S3)    ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Database Design & SQL     ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Distributed Processing    ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Analytics Engines         ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│  ✦ Data Quality & Validation ⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺   [■■■■■■■■■□]  │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

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

### 🟢 Beginner Exercises

#### [Exercise 1 - Downloading Files](./Exercises/Exercise-1/README.md)
```
    ☁️  REMOTE SERVER                LOCAL MACHINE
    ┌──────────────┐                ┌──────────────┐
    │   file.zip   │  ────HTTP───→  │  file.zip    │
    └──────────────┘                └──────┬───────┘
                                           │
                                           ▼
                                    ┌────────────┐
                                    │ extract()  │
                                    └────┬───────┘
                                         │
                                         ▼
                                    ┌───────────┐
                                    │   data/   │
                                    └───────────┘
```
Learn to download files from HTTP sources, unzip them, and store them locally using Python.

**Skills:** HTTP requests, file I/O, zip handling

---

#### [Exercise 2 - Web Scraping + Downloading + Pandas](./Exercises/Exercise-2/README.md)
```
    🌐 WEB PAGE                    📊 PANDAS
    ┌──────────────┐              ┌─────────────┐
    │ <html>       │              │ DataFrame   │
    │  <a href>    │────EXTRACT───│ Title │ URL │
    │  <a href>────┘              └─────────────┘
    │  <a href>    │
    └──────────────┘
```
Practice web scraping, URI building, file downloads, and basic data aggregation with Pandas.

**Skills:** Web scraping, HTTP requests, Pandas, data aggregation

---

#### [Exercise 3 - Boto3 AWS + S3 + Python](./Exercises/Exercise-3/README.md)
```
    ☁️  AWS S3 BUCKET             🐍 PYTHON APP
    ┌──────────────┐              ┌──────────────┐
    │ data/        │  ←Boto3──→   │ boto3.client │
    │ ├─ file1.csv │              │ .download()  │
    │ ├─ file2.csv │              └──────┬───────┘
    │ └─ file3.csv │                     │
    └──────────────┘              ┌──────▼────────┐
                                  │ local_file.csv│
                                  └───────────────┘
```
Work with AWS S3 using Boto3 to perform multi-step data retrieval from cloud storage.

**Skills:** AWS, S3, Boto3, cloud storage

---

#### [Exercise 4 - Convert JSON to CSV](./Exercises/Exercise-4/README.md)
```
    📁 RAGGED DIRECTORY          🔄 CONVERSION
    data/                        
    ├─ file1.json ──────┐
    ├─ nested/          │
    │  └─ file2.json ───┼──→ [flatten] ──→ ┌──────────┐
    └─ deep/nested/     │                  │ file.csv │
       └─ file3.json ───┘                  └──────────┘
```
Traverse ragged directory structures, find JSON files, and convert them to CSV format.

**Skills:** File traversal, JSON/CSV handling, Python file operations

---

#### [Exercise 5 - Data Modeling for Postgres](./Exercises/Exercise-5/README.md)
```
    📋 SCHEMA DESIGN              🗄️  POSTGRES DB
    Customers ─────────┐          Customers ──────┐
    Products  ────┐    ├─(Keys)──→ PK: customer_id │
    Orders    ────┼────┤          FK: product_id   │
    OrderItems ───┘    │          └─────────────────┘
                       │
                       └─(Indexes)→ idx_cust_email
                                   idx_order_date
```
Design a database schema, create tables in Postgres, and perform data ingestion via Python.

**Skills:** Database design, schema modeling, SQL, Python + Postgres

---

### 🟡 Intermediate Exercises

#### [Exercise 6 - Ingestion and Aggregation with PySpark](./Exercises/Exercise-6/README.md)
```
    📂 DATA FILES              ⚡ SPARK CLUSTER
    orders.csv ────────┐       ┌──────────────┐
    products.csv ──┬───┼──→    │ Spark Driver │
    customers.csv─ │   │       ├──────────────┤
                   └─→ │       │ Worker 1     │
                  Load │       ├──────────────┤
                       │       │ Worker 2     │
                       └──────→│ Worker N     │
                               └──┬───────────┘
                                  │
                          Results (Aggregated)
```
Load data files using PySpark and perform basic aggregations on distributed data.

**Skills:** PySpark, data loading, aggregations, distributed processing

---

#### [Exercise 7 - Using Various PySpark Functions](./Exercises/Exercise-7/README.md)
```
    🔧 PYSPARK FUNCTIONS
    
    F.initcap()     ──┐
    F.upper()       ──┤
    F.when()        ──┼──→ DataFrame Transform  ──→ Results
    F.datediff()    ──┤
    F.row_number()  ──┤
    F.collect_list()──┘
```
Apply multiple PySpark SQL functions to solve real-life data problems.

**Skills:** PySpark SQL functions, transformations, problem-solving

---

#### [Exercise 8 - DuckDB for Analytics and Transforms](./Exercises/Exercise-8/README.md)
```
    📊 DUCKDB (In-Memory OLAP)
    
    SQL Query                     Result
    SELECT ... FROM ...           ┌──────────────┐
    GROUP BY ...            ──→   │ Fast Results │
    WHERE ...                     │ In-Memory    │
    JOIN ...                      └──────────────┘
    
    ✨ No Server Required!
```
Perform analytical and transformation tasks using DuckDB, a modern SQL engine.

**Skills:** DuckDB, SQL analytics, data transformation

---

#### [Exercise 9 - Polars Lazy Computation](./Exercises/Exercise-9/README.md)
```
    ⏳ LAZY EVALUATION              ⚡ OPTIMIZED EXECUTION
    
    df.lazy()                      Optimization
    .filter()        ─────────────→ Pushdown
    .select()               ↓       Reordering
    .groupby()             ↓        Pruning
    .collect()  ◄──────────┘
    
    ✨ Faster, Leaner, Smarter!
```
Master Polars, a Rust-based data processing library with lazy evaluation.

**Skills:** Polars, lazy evaluation, SQL context, performance optimization

---

### 🔴 Advanced Exercises

#### [Exercise 10 - Data Quality with Great Expectations](./Exercises/Exercise-10/README.md)
```
    ✓ DATA QUALITY CHECKS
    
    Input Data    Expectations      Validation       Report
    ┌──────────┐  ┌────────────┐   ┌──────────┐    ┌────────┐
    │ CSV File │→ │ No Nulls   │──→│ ✓ PASS   │───→│✓ Clean │
    │ (Dirty)  │  │ Valid Type │   │ ✗ FAIL   │    │✗ Issues│
    │          │  │ In Range   │   │ ⚠ WARN   │    └────────┘
    └──────────┘  └────────────┘   └──────────┘
```
Implement data quality checks using Great Expectations to identify and catch data issues.

**Skills:** Data quality, Great Expectations, validation, testing

---

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

---

## 📈 Progress Tracker

Track your journey through the exercises:

```
╔══════════════════════════════════════════════════════════════════╗
║ 🎯 EXERCISE COMPLETION STATUS                                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║ BEGINNER LEVEL                                                   ║
║ ├─ □ Exercise 1: Downloading Files                           ║
║ ├─ □ Exercise 2: Web Scraping + Pandas                       ║
║ ├─ □ Exercise 3: AWS S3 + Boto3                              ║
║ ├─ □ Exercise 4: JSON to CSV Conversion                      ║
║ └─ □ Exercise 5: Postgres Data Modeling                      ║
║                                                                  ║
║ INTERMEDIATE LEVEL                                               ║
║ ├─ □ Exercise 6: PySpark Ingestion                           ║
║ ├─ □ Exercise 7: PySpark Functions                           ║
║ ├─ □ Exercise 8: DuckDB Analytics                            ║
║ └─ □ Exercise 9: Polars Lazy Computation                     ║
║                                                                  ║
║ ADVANCED LEVEL                                                   ║
║ └─ □ Exercise 10: Data Quality Checks                        ║
║                                                                  ║
║ Progress: [□□□□□□□□□□] 0% ✨ (0 / 10 completed)              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

💡 Tip: Edit the progress tracker above as you complete exercises!

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

---

## 🔧 Tech Stack by Exercise

```
EX1 → requests       EX6 → pyspark         EX10 → great-expectations
EX2 → beautifulsoup  EX7 → pyspark              (+ pandas)
EX3 → boto3          EX8 → duckdb
EX4 → pathlib        EX9 → polars
EX5 → psycopg2       (+ pandas)
     (+ sqlalchemy)

     All exercises use Docker for reproducibility! 🐳
```

## Getting Help

- Check the README.md in each exercise folder for detailed guidance
- Look at the hints section in each exercise
- Review the starter code comments for additional context
- Search for error messages in the documentation links above

---

## 🎓 Recommended Learning Path

```
Choose Your Adventure:

┌─────────────────────────────────────────────────────────────┐
│             START HERE                                      │
│                  ↓                                          │
│          ┌──────────────────┐                              │
│          │   Exercise 1     │  (Downloading Files)         │
│          └────────┬─────────┘                              │
│                   ↓                                         │
│          ┌──────────────────┐                              │
│          │   Exercise 2     │  (Web Scraping)             │
│          └────────┬─────────┘                              │
│                   ↓                                         │
│          ┌──────────────────┐                              │
│          │   Exercise 3     │  (Cloud Storage)            │
│          └────────┬─────────┘                              │
│                   ↓                                         │
│          ┌──────────────────┐                              │
│          │   Exercise 4     │  (Format Conversion)        │
│          └────────┬─────────┘                              │
│                   ↓                                         │
│          ┌──────────────────┐                              │
│          │   Exercise 5     │  (Database Design)          │
│          └────────┬─────────┘                              │
│                   ↓                                         │
│     ┌─────────────┴──────────────┐                        │
│     ↓                            ↓                        │
│  ┌──────────┐            ┌──────────────┐                │
│  │Exercise 6│            │ Exercise 8   │               │
│  │(PySpark) │            │ (DuckDB)     │               │
│  └────┬─────┘            └──────┬───────┘               │
│       ↓                          ↓                       │
│  ┌──────────┐            ┌──────────────┐               │
│  │Exercise 7│            │ Exercise 9   │               │
│  │(Functions)            │ (Polars)     │               │
│  └────┬─────┘            └──────┬───────┘               │
│       ↓                          ↓                       │
│     ┌─────────────────────────────┐                     │
│     │    Exercise 10              │                     │
│     │ (Data Quality)              │                     │
│     │ 🎓 YOU ARE NOW A DATA ENGINEER! 🎓               │
│     └─────────────────────────────┘                     │
│                                                         │
└─────────────────────────────────────────────────────────┘

⚡ Each exercise builds on previous knowledge!
   Start with Exercise 1 and progress sequentially.
```

---

## 📊 Project Statistics

```
┌─────────────────────────────────────────┐
│ 📈 BY THE NUMBERS                      │
├─────────────────────────────────────────┤
│                                         │
│  ✓ 10    Total Exercises                │
│  ✓ 50+   Coding Tasks                   │
│  ✓ 7     Data Engineering Tools         │
│  ✓ 5     Python Libraries               │
│  ✓ 100%  Dockerized & Portable          │
│  ✓ ∞     Learning Potential             │
│                                         │
│  ⏱️  Time to Complete: 40-60 hours     │
│  💪 Difficulty: Beginner → Advanced    │
│  🎓 DIY Certification: Share your work! │
│                                         │
└─────────────────────────────────────────┘
```

## Contributing

Feel free to fork this repository and submit pull requests with improvements, additional exercises, or corrections. See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

This project is open source and available under the MIT License.

---

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    🚀 YOU ARE NOW A DATA ENGINEER 🚀                         ║
║                                                                               ║
║                 σ(σ⌐█_█) Collection...                                       ║
║                   \\(°-°)/ Processing...                                      ║
║                  (★^●^★)  Analyzing...                                       ║
║                   ~(o_o)~ Validating...                                      ║
║                  (◕ ◞౪◟ ◕)  Delivering Results!                              ║
║                                                                               ║
║   Remember: Every byte counts, every query optimizes, every test validates! ║
║                                                                               ║
║  "Data is the new oil, but only if you know how to refine it." — You       ║
║                                                                               ║
║  Keep learning. Keep building. Keep engineering.                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

                        Made with 💻 and ☕ for data nerds
```
