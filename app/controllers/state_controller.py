from app.services.state_service import get_state, search_state

def get_state_by_id(state_id):
    state = get_state(state_id)
    if state:
        
        return state.serialize()
    else:
        
        return {'error': 'State not found'}, 404

def search_state_by_name(state_name):
    states = search_state(state_name)
    if states:
        
        return [state.serialize() for state in states]
    else:
        
        return {'error': 'No states found'}, 404
