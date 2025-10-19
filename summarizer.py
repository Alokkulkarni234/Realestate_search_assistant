import pandas as pd

def generate_summary(results: pd.DataFrame, filters: dict) -> str:
    if results.empty:
        available_cities = {
            'cmf6nu3ru000gvcxspxarll3v': 'Pune',
            'cmf50r5a00000vcj0k1iuocuu': 'Mumbai'
        }
        city_names = ', '.join(set(available_cities.values()))
        city_label = filters.get('city')
        city_display = city_label if city_label else "your selected city"
        return (
            f"No matching properties found for {filters.get('bhk')} in {city_display}. "
            f"Currently, listings are available only in {city_names}. Try searching there!"
        )

    total = len(results)
    bhk = filters.get('bhk', 'various configurations')
    city_label = filters.get('city')
    city_display = city_label.title() if city_label else "your selected city"
    budget = filters.get('budget')
    budget_str = f"under ₹{round(budget / 1e7, 2)} Cr" if budget else "your budget"

    localities = results['fulladdress'].dropna().apply(lambda x: x.split(',')[0].strip())
    top_localities = localities.value_counts().head(3).index.tolist()
    locality_str = ', '.join(top_localities)

    min_price = results['price'].min()
    max_price = results['price'].max()
    price_range = f"₹{round(min_price / 1e7, 2)} Cr to ₹{round(max_price / 1e7, 2)} Cr"

    possession = results['possessiondate'].dropna().unique()
    possession_str = f"with possession by {possession[0]}" if len(possession) == 1 else "with varied possession timelines"

    return (
        f"Found {total} properties in {city_display} matching {bhk} {budget_str}. "
        f"Popular localities include {locality_str}. Prices range from {price_range}, "
        f"{possession_str}."
    )
