-- Ventas por estado
CREATE VIEW sales_by_state AS

SELECT
    c.customer_state,
    ROUND(SUM(op.payment_value),2) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
INNER JOIN order_payments op
ON o.order_id=op.order_id
GROUP BY c.customer_state;

-- Ventas por estado
CREATE VIEW sales_by_category AS

SELECT
    p.product_category_name,
    ROUND(SUM(oi.price),2) AS revenue,
    COUNT(*) AS total_sales

FROM products p
INNER JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.product_category_name;

-- Top vendedores
CREATE VIEW top_sellers AS

SELECT
    seller_id,
    ROUND(SUM(price),2) revenue,
    COUNT(*) orders
FROM order_items
GROUP BY seller_id;