# Exercise 5: Data Modeling for Postgres + Python

## Objective

Learn to design database schemas, create normalized tables, and perform data ingestion using Python with Postgres.

## Problem Description

You are given a set of CSV files containing related data about an e-commerce business. Your task is to:

1. Analyze the data structure and relationships
2. Design a normalized database schema
3. Create tables in Postgres with appropriate:
   - Primary keys and constraints
   - Foreign key relationships
   - Indexes for performance
   - Data types and validations
4. Ingest CSV data into the database using Python
5. Perform validation queries

This is a critical skill for data engineers who need to design scalable database schemas.

## Requirements

- Understand data normalization (1NF, 2NF, 3NF)
- Design efficient database schemas
- Create tables with constraints and indexes
- Use Postgres data types effectively
- Perform bulk data ingestion
- Handle duplicate and invalid data
- Implement data validation

## Data Model Design

You'll work with an e-commerce dataset with these logical entities:

- **Customers** - Customer information
- **Products** - Product catalog
- **Orders** - Customer orders
- **OrderItems** - Individual items in orders
- **Categories** - Product categories

## Hints

- Use `psycopg2` or `SQLAlchemy` to connect to Postgres
- Use CREATE TABLE statements with proper constraints
- Add PRIMARY KEY, FOREIGN KEY, NOT NULL constraints
- Create indexes on frequently queried columns
- Use `COPY` or bulk insertion for performance
- Handle natural keys vs surrogate keys
- Use transactions for data consistency
- Validate data before insertion

## Expected Schema

```
Customers (customer_id, name, email, city, state, country)
Categories (category_id, category_name, description)
Products (product_id, product_name, category_id, price, stock_quantity)
Orders (order_id, customer_id, order_date, total_amount)
OrderItems (order_item_id, order_id, product_id, quantity, unit_price)
```

## Expected Output

After running your solution, you should have:
- Tables created in Postgres with appropriate schema
- Sample data inserted from CSV files
- Indexes created for performance
- Validation queries showing data integrity
- Summary statistics about inserted data

## Testing Your Solution

First, ensure Postgres is running:

```bash
docker-compose build
docker-compose up -d db
docker-compose run app python solution.py
```

You can also connect directly to verify:

```bash
docker-compose exec db psql -U upwego -d exercise5_db -c "SELECT COUNT(*) FROM customers;"
```

## Bonus Challenges

1. **Advanced Constraints** - Add check constraints and unique constraints
2. **Materialized Views** - Create views for reporting
3. **Triggers** - Implement database triggers for audit logging
4. **Partitioning** - Implement table partitioning for large datasets
5. **Replication** - Set up read replicas
6. **Backup/Restore** - Implement backup and recovery procedures

## Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
- [psycopg2 Documentation](https://www.psycopg.org/psycopg2/docs/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/)

## Next Steps

Once you complete this exercise, move to Exercise 6 to work with distributed data processing using PySpark.
