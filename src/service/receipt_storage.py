from typing import Dict

receipt_storage: Dict[str, int] = {}

def save_receipt_evaluation(receipt_id, point_total):
    """
    Store off receipts that have processed their receipts
    :param receipt_id: the uuid of a processed receipt
    :param point_total: total points in a processed receipt
    :return:
    """
    receipt_storage[receipt_id] = point_total

def get_total_points(receipt_id):
    """
    Using the receipt_id get the total points for that receipt
    :param receipt_id:
    :return: total points
    """
    return receipt_storage[receipt_id]