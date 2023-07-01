from app.services.region_service import get_region, search_region

def get_region_by_id(region_id):
    region = get_region(region_id)
    if region:
        
        return region.serialize()
    else:
        
        return {'error': 'Region not found'}, 404

def search_region_by_name(region_name):
    regions = search_region(region_name)
    if regions:
        
        return [region.serialize() for region in regions]
    else:
        
        return {'error': 'No regions found'}, 404
