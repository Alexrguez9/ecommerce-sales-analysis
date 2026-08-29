# Ecommerce Sales Analysis

An end-to-end data analytics project that processes e-commerce data through a Python ETL pipeline, stores it in PostgreSQL and exposes business metrics through SQL analytical views and a Metabase dashboard.

## Architecture
```text
CSV Datasets
     ↓
Python ETL Pipeline
     ├── Extract
     ├── Transform
     ├── Data Quality Checks
     └── Load
          ↓
     PostgreSQL
          ↓
   Analytics SQL Views
          ↓
   Metabase Dashboard
```

## Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- SQL
- Pytest
- Metabase

## Data Model

The project contains the following main entities:

Customers
Sellers
Products
Orders
Order Items
Order Payments
Order Reviews

More information is available in docs/data_model.md

## Dataset

Olist Brazilian E-commerce Dataset (Kaggle)

## ETL Pipeline

The ETL pipeline follows four main stages:

### Extract

Reads the raw CSV datasets.

### Transform

Converts date columns to appropriate datetime formats.

### Data Quality

Checks:
Dataset shape.
Null values.
Duplicate primary keys.

### Load

Loads the processed datasets into PostgreSQL.

The pipeline also includes logging, error handling, execution timing and ETL reporting.

## Analytics

Business metrics are exposed through PostgreSQL views inside the analytics schema.

Examples include:

Revenue and orders over time.
Revenue by customer state.
Revenue by product category.
Payment method performance.
Top sellers.
Customer Lifetime Value.
Delivery performance.
Product category review scores.


## Running the Project

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd ecommerce-sales-analysis
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

> On Windows, use:
>
> ```bash
> venv\Scripts\activate
> ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update the `.env` file if necessary.

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Create database schemas and tables

Execute the following SQL scripts against the PostgreSQL database:

```text
sql/schema/create_schema.sql
sql/schema/create_tables.sql
```

### 7. Run the ETL pipeline

```bash
python -m src.main
```

### 8. Run tests

```bash
pytest
```

## Future Improvements

* Add data quality checks to the ETL pipeline.
* Improve test coverage.
* Add automated database migrations.
* Add CI/CD integration.


This repository represents Version 1 of the project.

Potential future improvements include:

External API data ingestion.
API-driven backend architecture.
FastAPI service layer.
Custom frontend dashboards.
Automated pipeline orchestration.
Cloud deployment.
CI/CD integration.


## Author

Alejandro Rodríguez Montero

LinkedIn: https://www.linkedin.com/in/alejandro-jos%C3%A9-rodr%C3%ADguez-montero/
