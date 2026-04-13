# Quick Start Guide

Get started with the Data Engineering Practice Problems in 5 minutes!

## Prerequisites

- Docker and Docker Compose installed
- Git for version control
- Text editor or IDE (VS Code, PyCharm, etc.)
- ~2GB free disk space

## Installation (macOS with Homebrew)

```bash
# Install Docker
brew install docker docker-compose

# Clone the repository
git clone https://github.com/YOUR_USERNAME/Data-Engineering-UpWeGo.git
cd Data-Engineering-UpWeGo

# Verify installation
docker --version
docker-compose --version
```

## Running Your First Exercise (Exercise 1)

```bash
# Navigate to the exercise
cd Exercises/Exercise-1

# Build the Docker image
docker-compose build

# Run the exercise
docker-compose run app python solution.py
```

## Next Steps

1. **Read the README** in each exercise folder
2. **Review the TODO comments** in `solution.py`
3. **Implement the functions** one by one
4. **Test your solution** using the docker-compose commands
5. **Move to the next exercise** when complete

## Common Docker Commands

```bash
# Navigate to an exercise
cd Exercises/Exercise-X

# Build the Docker image (run once or after dependency changes)
docker-compose build

# Run the Python script
docker-compose run app python solution.py

# Start an interactive shell
docker-compose run app bash

# View logs
docker-compose logs -f

# Clean up Docker resources
docker-compose down
docker system prune
```

## Exercise Overview

```
Beginner (Exercises 1-5)
├── 1: File Downloading
├── 2: Web Scraping + Pandas
├── 3: AWS S3 + Boto3
├── 4: JSON/CSV Conversion
└── 5: Postgres Database

Intermediate (Exercises 6-9)
├── 6: PySpark Aggregation
├── 7: PySpark Functions
├── 8: DuckDB Analytics
└── 9: Polars Lazy Computation

Advanced (Exercise 10)
└── 10: Data Quality with Great Expectations
```

## Local Development (Optional)

If you want to run without Docker:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r Exercises/Exercise-1/requirements.txt

# Run the solution
python Exercises/Exercise-1/solution.py
```

## Troubleshooting

### Docker issues
```bash
# Restart Docker daemon
docker-compose restart

# Remove and rebuild
docker-compose down
docker-compose build --no-cache

# Check system resources
docker system df
```

### Port conflicts
```bash
# Check if port is in use (macOS/Linux)
lsof -i :5432  # for Postgres

# Use different port in docker-compose.yml
# ports:
#   - "5433:5432"
```

### Memory issues
```bash
# Increase Docker memory (Docker Desktop)
# Settings → Resources → Memory: 4GB or higher

# Or in Docker settings
{
  "memory": 4096  # MB
}
```

## Tips for Success

1. **Read the README first** - Each exercise has important context
2. **Review hints** - They point to the right approach
3. **Start simple** - Get basic functionality working first
4. **Test often** - Run your code after each change
5. **Use print statements** - Debug by printing intermediate values
6. **Check documentation** - The library docs are your friends
7. **Compare with hints** - If stuck, review the hints section

## Getting Help

1. **Check the README** - Most questions are answered there
2. **Review hints** - Exercise hints provide guidance
3. **Search issues** - See if similar problems exist
4. **Ask in discussions** - Use GitHub Discussions
5. **Contact maintainers** - Open an issue if truly stuck

## Next Challenge

After completing all exercises:

1. **Build your own project** - Apply these skills to real data
2. **Contribute solutions** - Help others by sharing your implementations
3. **Optimize your code** - Improve performance and efficiency
4. **Extend exercises** - Add bonus challenges
5. **Learn advanced topics** - Explore monitoring, testing, deployment

## Resources

- [Main README](../README.md) - Full project overview
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- Exercise READMEs - Detailed problem descriptions
- External [Resources section](../README.md#resources) in main README

---

## Ready?

Let's get started! 🚀

```bash
cd Exercises/Exercise-1
docker-compose build
docker-compose run app python solution.py
```

Happy learning! Feel free to reach out if you need help. 😊
