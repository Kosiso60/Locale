from flask import jsonify

from app.controllers.region_controller import get_region, search_region
from app.models.region import Region
from app import app

# Route handler for getting a specific region by ID
def get_region_by_id(region_id):
    region = get_region(region_id)
    if region:
        return jsonify(region.serialize()), 200
    return jsonify({'error': 'Region not found'}), 404

# Route handler for searching regions by name
def search_region_by_name(region_name):
    regions = search_region(region_name)
    if regions:
        serialized_regions = [region.serialize() for region in regions]
        return jsonify(serialized_regions), 200
    return jsonify({'message': 'No regions found'}), 200
