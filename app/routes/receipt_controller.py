from flask import Flask, app


@app.route('/receipts/<id>/points')
def get_points(id):
    """
    Returns the points awarded for a receipt
    :param id: The ID of the receipt
    :return: The number of points awarded.
    """
    # from cache fetch total point value of a receipt
    return f' Point Total order # {id}'


@app.route('receipts/process')
def process_receipt():
    """
    Submits a receipt for processing.

    :return:
    """
    # use point_evalulator to calculate point total