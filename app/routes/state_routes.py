from flask import jsonify

from app.controllers.state_controller import get_state, search_state
from app.models.state import State

# Route handler for getting a specific state by ID
def get_state_by_id(state_id):
    state = get_state(state_id)
    if state:
        return jsonify(state.serialize()), 200
    return jsonify({'error': 'State not found'}), 404

# # Route handler for searching states by name
def search_state_by_name(state_name):
    states = search_state(state_name)
    if states:
        serialized_states = [state.serialize() for state in states]
        return jsonify(serialized_states), 200
    return jsonify({'message': 'No states found'}), 200


# @app.route('/states')
# def get_states():
#     region_id = request.args.get('region_id')
#     search_query = request.args.get('q')

#     if region_id:
#         # Filter states by region ID if provided
#         states_query = State.query.filter_by(region_id=region_id)
#     else:
#         # Get all states if region ID is not provided
#         states_query = State.query

#     if search_query:
#         # Apply search filter based on the search query
#         states = states_query.filter(State.name.ilike(f'%{search_query}%')).all()
#     else:
#         # Fetch all states
#         states = states_query.all()

#     states_data = [{'id': state.id, 'name': state.name, 'region_id': state.region_id} for state in states]
#     return jsonify(states_data)
