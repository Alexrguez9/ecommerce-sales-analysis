# Architecture

## Overview

This project follows a batch-oriented analytics architecture designed to ingest e-commerce data, validate its quality, store it in PostgreSQL and expose analytical data through SQL views for business intelligence dashboards.

## Data Flow

CSV Datasets
     │
     ▼
Python ETL Pipeline
     │
     ├── Extract
     ├── Transform
     ├── Data Quality Checks
     └── Load
     │
     ▼
PostgreSQL
     │
     ├── Operational Tables
     │
     ▼
Analytics Schema
     │
     └── SQL Views
     │
     ▼
Metabase Dashboard

# Components
## Data Source

The project uses public e-commerce CSV datasets as the source of the ETL pipeline.

## ETL Pipeline

The ETL pipeline is implemented in Python and divided into three stages:

Extract: reads the source CSV files.
Transform: converts and prepares data types, including date columns.
Load: loads the processed datasets into PostgreSQL.

The pipeline also includes logging, execution timing, error handling and ETL reporting.

## Data Quality

Before loading the datasets, the pipeline performs data quality checks:

Dataset shape validation.
Null value detection.
Duplicate primary key detection.

## Database

PostgreSQL is used as the relational database.
The database runs locally inside a Docker container using Docker Compose.

## Analytics Layer

An analytics schema contains SQL views designed specifically for analytical consumption.
The views calculate business metrics such as:

Revenue.
Orders.
Average Order Value.
Sales by state.
Sales by category.
Payment methods.
Seller performance.
Customer Lifetime Value.
Delivery performance.
Product reviews.

## Business Intelligence

Metabase consumes the analytical views and provides the final business dashboard.

## Architectural Decision

This project intentionally uses a batch-oriented ETL architecture.
The objective of this first version is to demonstrate the complete analytical data flow, from raw data ingestion to business intelligence consumption.
The architecture prioritizes clarity, reproducibility and separation of responsibilities.
Future versions may evolve towards an API-driven architecture with external data sources, a backend service and a custom frontend.