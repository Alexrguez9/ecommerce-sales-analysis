DATASETS = [
    {
        "table": "customers",
        "file": "data/raw/customers_dataset.csv",
        "dates": []
    },
    {
        "table": "sellers",
        "file": "data/raw/sellers_dataset.csv",
        "dates": []
    },
    {
        "table": "products",
        "file": "data/raw/products_dataset.csv",
        "dates": []
    },
    {
        "table": "orders",
        "file": "data/raw/orders_dataset.csv",
        "dates": [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    },
    {
        "table": "order_items",
        "file": "data/raw/order_items_dataset.csv",
        "dates": [
            "shipping_limit_date"
        ]
    },
    {
        "table": "order_payments",
        "file": "data/raw/order_payments_dataset.csv",
        "dates": []
    },
    {
        "table": "order_reviews",
        "file": "data/raw/order_reviews_dataset.csv",
        "dates": [
            "review_creation_date",
            "review_answer_timestamp"
        ]
    }
]