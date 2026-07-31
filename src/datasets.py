DATASETS = [
    {
        "table": "customers",
        "file": "data/raw/customers_dataset.csv",
        "dates": [],
        "primary_key": [
        "customer_id"
        ]
    },
    {
        "table": "sellers",
        "file": "data/raw/sellers_dataset.csv",
        "dates": [],
        "primary_key": [
            "seller_id"
        ]
    },
    {
        "table": "products",
        "file": "data/raw/products_dataset.csv",
        "dates": [],
        "primary_key": [
            "product_id"
        ]
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
        ],
        "primary_key": [
            "order_id"
        ]
    },
    {
        "table": "order_items",
        "file": "data/raw/order_items_dataset.csv",
        "dates": [
            "shipping_limit_date"
        ],
        "primary_key": [
            "order_id",
            "order_item_id"
        ]
    },
    {
        "table": "order_payments",
        "file": "data/raw/order_payments_dataset.csv",
        "dates": [],
        "primary_key": [
            "order_id",
            "payment_sequential"
        ]
    },
    {
        "table": "order_reviews",
        "file": "data/raw/order_reviews_dataset.csv",
        "dates": [
            "review_creation_date",
            "review_answer_timestamp"
        ],
        "primary_key": [
            "review_id",
            "order_id"
        ]
    }
]