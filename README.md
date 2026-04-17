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

| Layer | Tools & Technologies |
|-------|----------------------|
| **Data Collection** | HTTP requests, BeautifulSoup, Boto3, REST APIs |
| **Data Processing** | Pandas, Polars, PySpark, DuckDB |
| **Storage** | PostgreSQL, AWS S3, CSV/JSON/Parquet files |
| **Analytics** | Spark SQL, DuckDB, Polars lazy frames |
| **Quality** | Great Expectations, Pandas validation |
| **Orchestration** | Docker, Docker Compose |

### 🎯 Core Competencies You'll Master

| Skill | Level | Exercises |
|-------|-------|-----------|
| 🐍 **Python Data Processing** | Beginner → Advanced | 1-4, 6-10 |
| 🕸️ **Web APIs & Scraping** | Beginner | 1-2 |
| ☁️ **AWS & Cloud Storage** | Beginner | 3 |
| 🗄️ **SQL & Database Design** | Beginner → Intermediate | 5, 8 |
| ⚡ **Distributed Processing** | Intermediate → Advanced | 6-7 |
| 📊 **Analytics Engines** | Intermediate | 8-9 |
| ✅ **Data Quality & Validation** | Advanced | 10 |

> **💡 Tip:** Complete all exercises and share your GitHub repo? You could earn a free copy of "Introduction to Data Engineering"!

## 📋 Prerequisites

Before you get started, ensure you have these tools installed:

> **🐳 Docker is required for all exercises!** It ensures 100% reproducibility.

### Required
- **Docker** - Container runtime for isolated environments
- **Docker Compose** - Multi-container orchestration
- **Git** - Version control

### Optional (for local development)
- **Python 3.9+** - Run exercises without Docker (not recommended)

### Installation

<details>
<summary><b>🍎 macOS</b></summary>

```bash
# Install using Homebrew
brew install docker docker-compose git

# Or download Docker Desktop from:
# https://www.docker.com/products/docker-desktop
```
</details>

<details>
<summary><b>🐧 Linux (Ubuntu/Debian)</b></summary>

```bash
# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io docker-compose git

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

1. Download [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
2. Follow the installation wizard
3. Enable WSL 2 (Windows Subsystem for Linux 2)
4. Install Git from [git-scm.com](https://git-scm.com/)

</details>

### Verify Installation

```bash
docker --version
docker-compose --version
git --version
```

---

## 📂 Project Structure

Each exercise includes:
- 📄 **README.md** - Detailed problem description, requirements, and hints
- 🐳 **Dockerfile** - Pre-configured container with all dependencies
- 🔧 **docker-compose.yml** - Container orchestration (if multi-container setup needed)
- 📦 **requirements.txt** - Python package dependencies
- 💻 **solution.py** - Starter code with TODO sections to fill in
- 📊 **sample_data/** - Sample datasets for testing

---

## 🚀 Quick Start (5 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Data-Engineering-UpWeGo.git
cd Data-Engineering-UpWeGo
```

### Step 2: Start with Exercise 1
```bash
cd Exercises/Exercise-1
```

### Step 3: Build & Run
```bash
docker-compose build
docker-compose run app python solution.py
```

### Step 4: Edit & Code
Open `solution.py` in your editor and implement the required functionality (look for `TODO` comments).

### Step 5: Test Your Solution
```bash
docker-compose run app python solution.py
```

> **Next:** Move to Exercise 2 when Exercise 1 passes all tests!

---

## 📚 Exercises at a Glance

### 🌱 Level 1: Foundation (Exercises 1-5)

Get comfortable with core data engineering tasks.

#### ✅ [Exercise 1: Downloading Files](./Exercises/Exercise-1/README.md)
**Difficulty:** ⭐ | **Time:** ~30 min

Download files from HTTP sources, handle archives, and validate data locally.

- **Skills:** HTTP requests, file I/O, zip extraction, Python basics
- **Tools:** `requests`, `urllib`, `zipfile`
- **Real-world use:** Ingesting data from APIs and external sources

---

#### ✅ [Exercise 2: Web Scraping + Data Aggregation](./Exercises/Exercise-2/README.md)
**Difficulty:** ⭐⭐ | **Time:** ~45 min

Extract data from web pages, build URLs dynamically, and aggregate results with Pandas.

- **Skills:** Web scraping, HTML parsing, data aggregation
- **Tools:** `requests`, `BeautifulSoup`, `pandas`
- **Real-world use:** Collecting data from websites without APIs

---

#### ✅ [Exercise 3: AWS S3 + Boto3](./Exercises/Exercise-3/README.md)
**Difficulty:** ⭐⭐ | **Time:** ~45 min

Access cloud storage, list objects, and download files from AWS S3 buckets.

- **Skills:** Cloud APIs, AWS services, authentication
- **Tools:** `boto3`, AWS SDK
- **Real-world use:** Working with cloud-based data repositories

---

#### ✅ [Exercise 4: JSON to CSV Conversion](./Exercises/Exercise-4/README.md)
**Difficulty:** ⭐⭐ | **Time:** ~40 min

Traverse complex directory structures, parse JSON files, and convert to CSV format.

- **Skills:** File system traversal, JSON/CSV conversion, data flattening
- **Tools:** `pathlib`, `json`, `pandas`
- **Real-world use:** Data format standardization

---

#### ✅ [Exercise 5: Database Design & Data Modeling](./Exercises/Exercise-5/README.md)
**Difficulty:** ⭐⭐⭐ | **Time:** ~60 min

Design normalized schemas, create tables in PostgreSQL, and perform data ingestion.

- **Skills:** Database design, normalization, SQL, relational modeling
- **Tools:** PostgreSQL, `psycopg2`, `sqlalchemy`
- **Real-world use:** Architecting data warehouses and operational databases

---

### ⚡ Level 2: Processing & Analytics (Exercises 6-9)

Master distributed processing and modern analytics tools.

#### ✅ [Exercise 6: PySpark Data Ingestion & Aggregation](./Exercises/Exercise-6/README.md)
**Difficulty:** ⭐⭐⭐ | **Time:** ~50 min

Load data into Spark DataFrames and perform aggregations on distributed clusters.

- **Skills:** Distributed computing, Spark DataFrames, aggregations
- **Tools:** Apache Spark, PySpark
- **Real-world use:** Processing massive datasets that don't fit in memory

---

#### ✅ [Exercise 7: PySpark Functions & Transformations](./Exercises/Exercise-7/README.md)
**Difficulty:** ⭐⭐⭐ | **Time:** ~50 min

Apply various PySpark SQL functions to solve complex data problems.

- **Skills:** PySpark transformations, windowing functions, string operations
- **Tools:** PySpark SQL, UDFs
- **Real-world use:** Complex data transformations at scale

---

#### ✅ [Exercise 8: DuckDB Analytics](./Exercises/Exercise-8/README.md)
**Difficulty:** ⭐⭐⭐ | **Time:** ~45 min

Perform OLAP analytics using DuckDB's high-performance in-memory engine.

- **Skills:** SQL analytics, analytical processing, performance optimization
- **Tools:** DuckDB, SQL
- **Real-world use:** Fast analytics on structured data

---

#### ✅ [Exercise 9: Polars Lazy Evaluation](./Exercises/Exercise-9/README.md)
**Difficulty:** ⭐⭐⭐ | **Time:** ~50 min

Master Polars, a Rust-based library with lazy evaluation for optimal query planning.

- **Skills:** Lazy evaluation, query optimization, modern data frames
- **Tools:** Polars, lazy API, SQL context
- **Real-world use:** Next-generation high-performance data processing

---

### 🎓 Level 3: Advanced (Exercise 10)

Production-ready data quality and governance.

#### ✅ [Exercise 10: Data Quality with Great Expectations](./Exercises/Exercise-10/README.md)
**Difficulty:** ⭐⭐⭐⭐ | **Time:** ~60 min

Implement comprehensive data quality checks and validation pipelines.

- **Skills:** Data validation, quality metrics, testing frameworks, reporting
- **Tools:** Great Expectations, Pandas, pytest
- **Real-world use:** Ensuring data integrity in production pipelines

---

## 🎯 Recommended Learning Path

```
START HERE ↓

Exercise 1 (Files) → Exercise 2 (Scraping) → Exercise 3 (Cloud)
    ↓                                             ↓
Exercise 4 (Formats) ← ← ← ← ← ← ← ← ← ← ← ← ← ↓
    ↓                                             ↓
Exercise 5 (Databases) ← ← ← ← ← ← ← ← ← ← ← ← ↓
    ↓
    ├─→ Exercise 6 (Spark) → Exercise 7 (Spark +) ┐
    │                                              ├→ Exercise 10 (Quality) 
    └─→ Exercise 8 (DuckDB) → Exercise 9 (Polars)┘

🎓 Complete all 10 exercises → You're a Data Engineer! 🚀
```

---

## 💼 Local Development (Optional)

If you want to run exercises locally without Docker:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies for an exercise
pip install -r Exercises/Exercise-1/requirements.txt

# Run the solution
python Exercises/Exercise-1/solution.py
```

> **Note:** Docker is recommended for consistency across different systems.

---

## 📊 Progress Tracking

Create a file called `PROGRESS.md` in your fork and track completion:

```markdown
# My Progress 📈

- [ ] Exercise 1 - Downloading Files
- [ ] Exercise 2 - Web Scraping + Pandas
- [ ] Exercise 3 - AWS S3 + Boto3
- [ ] Exercise 4 - JSON to CSV
- [ ] Exercise 5 - Postgres Modeling
- [ ] Exercise 6 - PySpark Ingestion
- [ ] Exercise 7 - PySpark Functions
- [ ] Exercise 8 - DuckDB Analytics
- [ ] Exercise 9 - Polars Lazy Computation
- [ ] Exercise 10 - Data Quality

**Total Progress:** 0/10 ✨
```

---

## 📚 Learning Resources

<details>
<summary><b>Python & Data Processing</b></summary>

- [Python Official Documentation](https://docs.python.org/3/) - Core language reference
- [Real Python](https://realpython.com/) - In-depth tutorials
- [Pandas Documentation](https://pandas.pydata.org/docs/) - Data manipulation
- [Polars Documentation](https://pola-rs.github.io/polars/) - Modern data frames

</details>

<details>
<summary><b>Distributed Processing</b></summary>

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/) - Distributed computing
- [PySpark API](https://spark.apache.org/docs/latest/api/python/) - Spark Python API
- [DuckDB Documentation](https://duckdb.org/docs/) - In-memory OLAP

</details>

<details>
<summary><b>Databases & SQL</b></summary>

- [PostgreSQL Documentation](https://www.postgresql.org/docs/) - relational database
- [SQL Tutorial](https://www.w3schools.com/sql/) - Interactive SQL learning
- [Database Design](https://en.wikipedia.org/wiki/Database_design) - Design principles

</details>

<details>
<summary><b>Cloud & DevOps</b></summary>

- [AWS Documentation](https://docs.aws.amazon.com/) - AWS services reference
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python
- [Docker Documentation](https://docs.docker.com/) - Container fundamentals
- [Docker Compose](https://docs.docker.com/compose/) - Multi-container applications

</details>

<details>
<summary><b>Data Quality & Testing</b></summary>

- [Great Expectations](https://docs.greatexpectations.io/) - Data validation framework
- [pytest Documentation](https://docs.pytest.org/) - Python testing
- [Data Quality Fundamentals](https://www.stitchdata.com/resources/data-quality/) - Best practices

</details>

---

## 🔧 Technology Stack by Exercise

| Exercise Range | Category | Key Technologies |
|---|---|---|
| Ex 1-5 | Foundation | `requests`, `boto3`, `psycopg2`, `beautifulsoup4` |
| Ex 6-7 | Spark | `pyspark` (Spark SQL, DataFrame API) |
| Ex 8 | Analytics | `duckdb` (OLAP, in-memory processing) |
| Ex 9 | Modern | `polars` (Rust-based, lazy evaluation) |
| Ex 10 | Quality | `great-expectations`, `pytest` |

**All exercises are containerized with 🐳 Docker for reproducibility!**

**Estimated Time to Complete:** 40-60 hours  
**Difficulty Progression:** Beginner → Intermediate → Advanced  
**Certification:** Share your work and get recognized! 🎓

---

## ❓ Getting Help

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| `docker: command not found` | Install Docker Desktop or Docker Engine for your OS |
| `permission denied` | Add user to docker group: `sudo usermod -aG docker $USER` |
| Container build fails | Check `requirements.txt` file and ensure Docker daemon is running |
| Import errors in Python | Run `pip install -r requirements.txt` inside the container |
| Can't connect to database | Ensure `docker-compose up -d` completed; check logs with `docker-compose logs` |

### Where to Find Help

1. **Exercise README.md** - Each exercise has detailed problem descriptions and hints
2. **Starter code comments** - Look for TODO and NOTE comments in `solution.py`
3. **Official documentation** - Use the resource links in the Learning Resources section
4. **Stack Overflow** - Search with your error message + tool name
5. **GitHub Issues** - Check if others have reported the same problem

---

## 🎁 Extra Features

### Bonus Content

- 📄 **QUICKSTART.md** - Skip to the action (5-minute setup)
- 📖 **CONTRIBUTING.md** - How to contribute new exercises
- 📊 **Exercise solutions** - Reference implementations (after completion)

### Next Steps After Completion

Level up your skills with these advanced topics:
- **Workflow Orchestration:** Apache Airflow, Prefect, Dagster
- **Transformation:** dbt (data build tool)
- **Real-time Processing:** Apache Kafka, Spark Streaming
- **Orchestration:** Kubernetes (K8s) for production deployments
- **Cloud Platforms:** Snowflake, Google BigQuery, AWS Redshift
- **Advanced Analytics:** Machine learning pipelines, feature stores

---

## 🏆 Share Your Success

After completing all 10 exercises:

1. ✅ Fork this repository
2. ✅ Complete all exercises with passing tests
3. ✅ Push your solutions to GitHub
4. ✅ Add a `PROGRESS.md` file documenting what you learned
5. ✅ (Optional) Submit your repo for a free copy of "Introduction to Data Engineering"

---

## 📊 By the Numbers

- **✨ 10** comprehensive exercises
- **🎯 50+** individual coding tasks
- **🛠️ 7** different data engineering tools and libraries
- **👥 100%** containerized and portable
- **⏱️ 40-60** hours of practical learning
- **📈 Difficulty:** Beginner → Advanced
- **🎓 Certification:** Share & get recognized!

---

## 🤝 Contributing

We ❤️ contributions! Help us improve this project:

- **Found a bug?** Open an issue on GitHub
- **Have a better solution?** Submit a pull request
- **Want to add exercises?** See [CONTRIBUTING.md](./CONTRIBUTING.md)
- **Grammar/clarity issues?** We accept all improvements!

**[See CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.**

---

## 📄 License

This project is open source and licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

<div align="center">

## 🚀 Ready to Become a Data Engineer?

### **[→ Start with Exercise 1 ←](./Exercises/Exercise-1/README.md)**

Every expert was once a beginner.  
Every master was once a student.  
Every data engineer started with these fundamentals.

---

**Made with 💻 and ☕ by data engineers, for data engineers**

⭐ If this project helped you, please star it! 🙏

</div>
