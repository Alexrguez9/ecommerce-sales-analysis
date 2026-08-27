# Data Model

## Tables and Granularity

| Table | Granularity | Primary Key |
|---|---|---|
| customers | 1 row = 1 customer record | customer_id |
| sellers | 1 row = 1 seller | seller_id |
| products | 1 row = 1 product | product_id |
| orders | 1 row = 1 order | order_id |
| order_items | 1 row = 1 item within an order | order_id + order_item_id |
| order_payments | 1 row = 1 payment within an order | order_id + payment_sequential |
| order_reviews | 1 row = 1 customer review | review_id |

## Main Relationships

customers
    │
    │ customer_id
    ▼
orders
    │
    ├──────────────► order_payments
    │
    ├──────────────► order_reviews
    │
    ▼
order_items ◄──────── sellers
    │
    ▼
products

## Notes

The customer_unique_id column identifies the actual customer across multiple orders, while customer_id identifies a specific customer record associated with an order.

The composite primary keys in order_items and order_payments represent the grain of those transactional tables.