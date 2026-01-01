from product import product_details

def test_product_details():
    expected_output = (
        "Product Name : Mobile\n"
        "Product ID : 524761\n"
        "Quantity : 10\n"
        "Price : 80000"
    )

    assert product_details("Mobile", "524761", "10", 80000) == expected_output

    assert product_details("Mobile","524761","10",80000) == expected_output