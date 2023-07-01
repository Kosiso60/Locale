from flask import jsonify

from app.controllers.lga_controller import get_lga, search_lga
from app.models import LGA

# Route handler for getting a specific LGA by ID
def get_lga_by_id(lga_id):
    lga = get_lga(lga_id)
    if lga:
        return jsonify(lga.serialize()), 200
    return jsonify({'error': 'LGA not found'}), 404

# Route handler for searching LGAs by name
def search_lga_by_name(lga_name):
    lgas = search_lga(lga_name)
    if lgas:
        serialized_lgas = [lga.serialize() for lga in lgas]
        return jsonify(serialized_lgas), 200
    return jsonify({'message': 'No LGAs found'}), 200

# @app.route('/regions')
# def get_regions():
#     # Get the search query parameter from the request URL
#     search_query = request.args.get('q')

#     # Logic to fetch regions based on the search criteria
#     if search_query:
#         regions = Region.query.filter(Region.name.ilike(f'%{search_query}%')).all()
#     else:
#         regions = Region.query.all()

#     # Convert the regions to a list of dictionaries
#     regions_data = [{'id': region.id, 'name': region.name} for region in regions]

#     # Return the regions as JSON response
#     return jsonify(regions_data)
