from app.models.state import State

def get_state(state_id):
    state = State.query.get(state_id)
    return state

def search_state(state_name):
    states = State.query.filter(State.name.ilike(f"%{state_name}%")).all()
    return states
