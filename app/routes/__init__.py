from flask import Blueprint

# Create a Blueprint object for the routes
routes_bp = Blueprint('routes', __name__)

# Import the route handlers from individual files
from .region_routes import *
from .state_routes import *
from .lga_routes import *

# Register the route handlers with the Blueprint
# routes_bp.add_url_rule('/regions', view_func=get_all_regions, methods=['GET'])
# routes_bp.add_url_rule('/states', view_func=get_all_states, methods=['GET'])
# routes_bp.add_url_rule('/lgas', view_func=get_all_lgas, methods=['GET'])
routes_bp.add_url_rule('/search/region/<region_name>', view_func=search_region, methods=['GET'])
routes_bp.add_url_rule('/search/state/<state_name>', view_func=search_state, methods=['GET'])
routes_bp.add_url_rule('/search/lga/<lga_name>', view_func=search_lga, methods=['GET'])
