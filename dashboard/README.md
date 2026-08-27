# Dashboard

The dashboard was built with Metabase using the analytical SQL views created in the `analytics` schema.

## Main KPIs

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value

## Business Areas

### Sales Performance

- Revenue over time
- Revenue by state
- Revenue by product category

### Payments

- Payment method distribution

### Sellers

- Top sellers by revenue

### Logistics

- Delivery performance

### Customer Satisfaction

- Average review score by category

## Data Source

The dashboard consumes PostgreSQL views from:

analytics.vw_kpis
analytics.vw_sales_by_month
analytics.vw_sales_by_state
analytics.vw_sales_by_category
analytics.vw_payment_methods
analytics.vw_top_sellers
analytics.vw_customer_ltv
analytics.vw_delivery_performance
analytics.vw_category_reviews