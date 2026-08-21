/*
===============================================================================
EXECUTIVE KPIs
===============================================================================
*/

DROP VIEW IF EXISTS analytics.vw_kpis;
CREATE VIEW analytics.vw_kpis AS
WITH order_totals AS (
    SELECT
        order_id,
        SUM(payment_value) AS order_total
    FROM order_payments
    GROUP BY order_id
)
SELECT
    (SELECT COUNT(*) FROM orders) AS total_orders,
    (SELECT ROUND(SUM(payment_value),2)
     FROM order_payments) AS total_revenue,
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM sellers) AS total_sellers,
    (SELECT COUNT(*) FROM products) AS total_products,
    (
        SELECT ROUND(AVG(order_total),2)
        FROM order_totals
    ) AS average_order_value;



/*
===============================================================================
SALES
===============================================================================
*/

DROP VIEW IF EXISTS analytics.vw_sales_by_month;
CREATE VIEW analytics.vw_sales_by_month AS
WITH order_totals AS (
    SELECT
        o.order_id,
        DATE_TRUNC(
            'month',
            o.order_purchase_timestamp
        ) AS month,
        SUM(op.payment_value) AS order_total
    FROM orders o
    INNER JOIN order_payments op
        ON o.order_id = op.order_id
    GROUP BY
        o.order_id,
        month
)
SELECT
    TO_CHAR(month,'YYYY-MM') AS month,
    ROUND(SUM(order_total),2) AS revenue,
    COUNT(*) AS total_orders,
    ROUND(AVG(order_total),2) AS average_order_value
FROM order_totals
GROUP BY month;


DROP VIEW IF EXISTS analytics.vw_sales_by_state;
CREATE VIEW analytics.vw_sales_by_state AS
WITH order_totals AS (
    SELECT
        o.order_id,
        c.customer_state,
        SUM(op.payment_value) AS order_total
    FROM customers c
    INNER JOIN orders o
        ON c.customer_id=o.customer_id
    INNER JOIN order_payments op
        ON o.order_id=op.order_id
    GROUP BY
        o.order_id,
        c.customer_state
)
SELECT
    customer_state,
    ROUND(SUM(order_total),2) revenue,
    COUNT(*) total_orders,
    ROUND(AVG(order_total),2) average_order_value
FROM order_totals
GROUP BY customer_state;


DROP VIEW IF EXISTS analytics.vw_sales_by_category;
CREATE VIEW analytics.vw_sales_by_category AS
SELECT
    p.product_category_name,
    ROUND(SUM(oi.price),2) revenue,
    COUNT(*) items_sold,
    ROUND(AVG(oi.price),2) average_price
FROM products p
INNER JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.product_category_name;


DROP VIEW IF EXISTS analytics.vw_payment_methods;
CREATE VIEW analytics.vw_payment_methods AS
SELECT
    payment_type,
    COUNT(*) total_transactions,
    ROUND(SUM(payment_value),2) revenue,
    ROUND(AVG(payment_value),2) average_payment
FROM order_payments
GROUP BY payment_type;


DROP VIEW IF EXISTS analytics.vw_top_sellers;
CREATE VIEW analytics.vw_top_sellers AS
SELECT
    seller_id,
    ROUND(SUM(price),2) revenue,
    COUNT(DISTINCT order_id) total_orders,
    ROUND(AVG(price),2) average_item_price
FROM order_items
GROUP BY seller_id;



/*
===============================================================================
CUSTOMERS
===============================================================================
*/

DROP VIEW IF EXISTS analytics.vw_customer_ltv;
CREATE VIEW analytics.vw_customer_ltv AS
WITH order_totals AS (
    SELECT
        order_id,
        SUM(payment_value) order_total
    FROM order_payments
    GROUP BY order_id
)
SELECT
    c.customer_unique_id,
    ROUND(SUM(order_total),2) lifetime_value,
    COUNT(DISTINCT o.order_id) total_orders,
    ROUND(AVG(order_total),2) average_order_value
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
INNER JOIN order_totals ot
ON o.order_id=ot.order_id
GROUP BY customer_unique_id;


DROP VIEW IF EXISTS analytics.vw_customer_distribution;
CREATE VIEW analytics.vw_customer_distribution AS
SELECT
    customer_state,
    COUNT(*) total_customers
FROM customers
GROUP BY customer_state;


DROP VIEW IF EXISTS analytics.vw_repeat_customers;
CREATE VIEW analytics.vw_repeat_customers AS
SELECT
    customer_unique_id,
    COUNT(o.order_id) total_orders
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY customer_unique_id;


/*
===============================================================================
PRODUCTS
===============================================================================
*/

DROP VIEW IF EXISTS analytics.vw_top_products;
CREATE VIEW analytics.vw_top_products AS
SELECT
    p.product_id,
    p.product_category_name,
    ROUND(SUM(oi.price),2) revenue,
    COUNT(*) total_sales,
    ROUND(AVG(oi.price),2) average_price
FROM products p
INNER JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY
    p.product_id,
    p.product_category_name;


DROP VIEW IF EXISTS analytics.vw_category_reviews;
CREATE VIEW analytics.vw_category_reviews AS
SELECT
    p.product_category_name,
    ROUND(AVG(r.review_score),2) average_review,
    COUNT(*) total_reviews
FROM products p
INNER JOIN order_items oi
ON p.product_id=oi.product_id
INNER JOIN order_reviews r
ON oi.order_id=r.order_id
GROUP BY p.product_category_name;


/*
===============================================================================
LOGISTICS
===============================================================================
*/

DROP VIEW IF EXISTS analytics.vw_delivery_performance;
CREATE VIEW analytics.vw_delivery_performance AS
SELECT
    CASE
        WHEN order_delivered_customer_date IS NULL
            THEN 'Not Delivered'
        WHEN order_delivered_customer_date >
             order_estimated_delivery_date
            THEN 'Delayed'
        ELSE 'On Time'
    END AS delivery_status,
    COUNT(*) total_orders
FROM orders
GROUP BY delivery_status;


DROP VIEW IF EXISTS analytics.vw_delivery_time;
CREATE VIEW analytics.vw_delivery_time AS
SELECT
    ROUND(
        AVG(
            order_delivered_customer_date
            -
            order_purchase_timestamp
        ),
        2
    ) average_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;


DROP VIEW IF EXISTS analytics.vw_late_deliveries;
CREATE VIEW analytics.vw_late_deliveries AS
SELECT
    c.customer_state,
    COUNT(*) delayed_orders
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id
WHERE
    o.order_delivered_customer_date
    >
    o.order_estimated_delivery_date
GROUP BY customer_state;