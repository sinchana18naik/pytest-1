def product_details(name, pid, qty, price):
    return (
        f"Product Name : {name}\n"
        f"Product ID : {pid}\n"
        f"Quantity : {qty}\n"
        f"Price : {price}"
    )

if __name__ == "__main__":
    name= "Mobile"
    pro_id="524761"
    quantity ="10"
    price= 80000
    print(product_details(name,pro_id,quantity,price))