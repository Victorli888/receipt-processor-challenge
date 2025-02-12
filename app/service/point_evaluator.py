import math
from app.models.receipt_model import ReceiptDTO

def calculate_points(receipt: ReceiptDTO):
    """
    Calculate the total points awarded by breaking down the receipt by each item
    :param receipt: DTO of Receipt
    :return: total Points awarded
    """

    #TODO: Break down each rule into its own method and provide unit tests for each

    total = 0
    cash_total = float(receipt.total)
    item_count = len(receipt.items)
    day_of_purchase = receipt.purchaseDate.split("-")[2]
    hour_of_purchase = receipt.purchaseTime.split(":")[0]

    # One Point for each alphanumeric character
    for c in receipt.retailer:
        if c.isalnum():
            total += 1

    # 50 points for every whole dollar amount

    if cash_total.is_integer():
        total += 50

    # 25 points if the receipt cash total is a multiple of 25 cents
    if cash_total % .25 == 0:
        total += 25

    # 5 points for every two items in the receipt
    total += (item_count // 2) * 5

    # For each short description of an item, if length is a multiple of 3 multiply item price by .02  round up
    # and award it to the pont total
    for item in receipt.items:
            description_length = len(item.shortDescription.strip())
            if description_length % 3 == 0:
                item_price = float(item.price)
                total += math.ceil(item_price * 0.2)

    # If date of purchase is odd 5 points
    if int(day_of_purchase) % 2 == 1:
        total += 6

    # 10 points if the time of purchase is between 14:00 and 16:00
    if 14 <= int(hour_of_purchase) < 16:
        total += 10

    return total









