def product_details(name,pro_id,quantity,price):
    result = (
        f"Product Name : {name}\n"
        f"Product ID : {pro_id}\n"
        f"Quantity : {quantity}\n"
        f"Price : {price}"
    )
    return result

if __name__ == "__main__":
    name= "Mobile"
    pro_id="524761"
    quantity ="10"
    price= 80000
    print(product_details(name,pro_id,quantity,price))