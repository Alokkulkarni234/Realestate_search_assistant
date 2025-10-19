import re

def parse_query(query: str) -> dict:
    query = query.lower()

    # Supported cities
    city_map = {
        'pune': 'cmf6nu3ru000gvcxspxarll3v',
        'mumbai': 'cmf50r5a00000vcj0k1iuocuu'
    }

    city_name = next((c for c in city_map if c in query), None)
    city_id = city_map.get(city_name)

    # If city not supported
    if not city_id:
        return {
            'bhk': None,
            'budget': None,
            'city': None,
            'readiness': None,
            'locality': None,
            'invalid_city': True
        }

    # BHK
    bhk_match = re.search(r'(\d+)\s*bhk', query)
    bhk = f"{bhk_match.group(1)}BHK" if bhk_match else None

    # Budget
    budget_match = re.search(r'under\s*₹?\s*([\d\.]+)\s*(cr|l|lakhs|crore)?', query)
    budget = None
    if budget_match:
        amount = float(budget_match.group(1))
        unit = budget_match.group(2)
        if unit in ['cr', 'crore']:
            budget = int(amount * 1e7)
        elif unit in ['l', 'lakhs']:
            budget = int(amount * 1e5)
        else:
            budget = int(amount)

    # Readiness
    readiness = None
    if 'ready to move' in query or 'ready' in query:
        readiness = 'READY_TO_MOVE'
    elif 'under construction' in query or 'construction' in query:
        readiness = 'UNDER_CONSTRUCTION'

    # Locality
    locality_match = re.search(r'near\s+([\w\s]+)', query)
    locality = locality_match.group(1).strip() if locality_match else None

    return {
        'bhk': bhk,
        'budget': budget,
        'city': city_id,
        'readiness': readiness,
        'locality': locality,
        'invalid_city': False
    }
