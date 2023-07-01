from app.services.lga_service import get_lga, search_lga

def get_lga_by_id(lga_id):
    lga = get_lga(lga_id)
    if lga:
        
        return lga.serialize()
    else:
        
        return {'error': 'LGA not found'}, 404

def search_lga_by_name(lga_name):
    lgas = search_lga(lga_name)
    if lgas:
        
        return [lga.serialize() for lga in lgas]
    else:
       
        return {'error': 'No LGAs found'}, 404
