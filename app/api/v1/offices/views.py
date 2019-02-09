from flask import  request, jsonify, make_response 
from app.api.v1 import api
from app.api.v1.offices.models import Office


@api.route('/offices', methods=['GET'], strict_slashes=False)
def get_offices():
    """Fetch all political offices records."""
    offices = Office.get_offices()
    return make_response(jsonify({
        "status":200,
        "data":offices
    }), 200)

@api.route('/offices/<int:office_id>', methods=['GET'], strict_slashes=False)
def get_office(office_id):
    """Fetch a specific political office record."""
    office = Office.get_office(office_id)
    if office == None:
        return make_response(jsonify({
        "status":404,
        "error":"The office does not exist on the Politico platform."
        }), 404)
    return make_response(jsonify({
        "status":200,
        "data":office
    }), 200)

@api.route('/offices', methods=['POST'], strict_slashes=False)
def create_office():
    """Create a political office ."""
    data =request.get_json(force=True)
    try:    
        office = Office(data["type"], data["name"])    

        return make_response(jsonify({
            "status":201,
            "data": [{"id":office.id,
                    "name":office.name }]
        }), 201)
    except AssertionError as exception_message:
        return make_response(jsonify({
                                        "status":400,
                                        "error": "{}".format(exception_message)
                                        }), 400)
        