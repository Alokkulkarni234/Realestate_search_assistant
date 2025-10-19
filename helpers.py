def format_price(price: float) -> str:
    if price >= 1e7:
        return f"₹{round(price / 1e7, 2)} Cr"
    elif price >= 1e5:
        return f"₹{round(price / 1e5, 2)} L"
    else:
        return f"₹{int(price)}"

def format_bhk(bhk: str) -> str:
    return bhk.upper().replace("BHK", " BHK").strip()

def format_possession(date: str) -> str:
    if date == "NA" or not date:
        return "Possession date not available"
    try:
        return f"Possession by {date.split()[0]}"
    except:
        return "Possession date not available"

def format_card(row: dict) -> dict:
    return {
        "title": row.get("projectname", "Unknown Project"),
        "bhk": format_bhk(row.get("bhk", "N/A")),
        "price": format_price(row.get("price", 0)),
        "address": row.get("fulladdress", "Location not available"),
        "possession": format_possession(row.get("possessiondate", "NA")),
        "cta": f"/project/{row.get('slug', 'unknown')}"
    }
