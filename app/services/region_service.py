from app.models.region import Region

def get_region(region_id):
    region = Region.query.get(region_id)
    return region

def search_region(region_name):
    regions = Region.query.filter(Region.name.ilike(f"%{region_name}%")).all()
    return regions
