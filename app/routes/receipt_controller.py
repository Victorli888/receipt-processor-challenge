from flask import Blueprint, jsonify, request
from app.models.receipt_model import ReceiptDTO
from app.service.point_evaluator import calculate_points
from app.service.receipt_storage import save_receipt_evaluation, get_total_points
import uuid

receipt_bp = Blueprint('receipts', __name__)

@receipt_bp.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    """
    Returns the points awarded for a receipt
    :param id: The ID of the receipt
    :return: The number of points awarded.
    """

    points = get_total_points(id)
    if points is None:
        return jsonify({"error": "No Receipt Found for that ID"})
    return jsonify({"points": points}), 200


@receipt_bp.route('/receipts/process', methods=['POST'])
def process_receipt():
    """
    Submits a receipt for processing.
    :return: json object {"id": uuid generated receipt id}
    """

    try:
        receipt_json = request.get_json()
        receipt = ReceiptDTO(**receipt_json)

        points = calculate_points(receipt)

        receipt_id = str(uuid.uuid4())

        save_receipt_evaluation(receipt_id, points)

        return jsonify({"id": receipt_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


