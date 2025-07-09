#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """
    Checks if a contract exists by ID.
    Returns contract information string for a given contract ID.
    Returns 404 if not found.
    """
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200
    return {"error": "Contract not found"}, 404

@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer(customer_name):
    """
    Checks if a customer exists by name.
    Returns:
        204 No Content: If the customer exists (without returning any data).
        404 Not Found: If the customer does not exist.
    """
    if customer_name.lower() in customers:
        return "", 204
    return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
