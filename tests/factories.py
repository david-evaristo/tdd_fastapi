def product_data():
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


def product_data_bad_request():
    return {
        "name": "",
        "quantity": 10,
        "price": 0,
        "status": True,
    }


def products_data():
    return [
        {"name": "Iphone 11 Pro Max", "quantity": 20, "price": 6.497, "status": True},
        {"name": "Iphone 12 Pro Max", "quantity": 15, "price": 6.498, "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": 6.500, "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": 6.700, "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": 6.650, "status": True},
        {"name": "Iphone 13 Pro Max", "quantity": 5, "price": 6.800, "status": True},
        {
            "name": "Iphone 15 Pro Max",
            "quantity": 3,
            "price": 6.501,
            "status": False,
        },
    ]
