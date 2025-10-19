🏡 NoBrokerage AI Chatbot
An AI-powered property search assistant built with Streamlit. Users can ask natural-language queries like:

3BHK in Pune under ₹1.2 Cr

and instantly get smart summaries and matching properties from preloaded datasets.

📁 Project Structure
Code
nobrokerage-ai/
├── app1.py                      # Main Streamlit frontend
├── utils/                       # Modular backend components
│   ├── parser.py               # Parses user queries into structured filters
│   ├── search.py               # Applies filters to the property dataset
│   ├── summarizer.py           # Generates summary of search results
│   └── helpers.py              # Formats property cards for display
├── data/                        # Raw property data
│   ├── ProjectConfigurationVariant.csv
│   ├── ProjectConfiguration.csv
│   ├── project.csv
│   └── ProjectAddress.csv
└── README.md                   # Project documentation
🚀 Getting Started
1. Install dependencies
bash
pip install streamlit pandas
2. Run the app
bash
streamlit run app1.py
🔍 How the System Works (with Examples)
✅ app1.py — Main App
This is the entry point. It:

Loads and merges all CSVs

Displays the UI (search bar, title, results)

Calls backend functions

Example:

python
query = "2BHK in Mumbai under ₹90L"
filters = parse_query(query)
results = search_properties(df, filters)
summary = generate_summary(results, filters)
✅ parser.py — Query Parser
Converts user input into structured filters.

Function: parse_query(query: str) → dict

Example:

python
query = "2BHK in Mumbai under ₹90L near Chembur"
filters = parse_query(query)
Output:

python
{
  "city": "Mumbai",
  "bhk": "2",
  "budget": 9000000,
  "location_keywords": ["Chembur"]
}
✅ search.py — Property Search
Filters the merged dataset using parsed filters.

Function: search_properties(df: pd.DataFrame, filters: dict) → pd.DataFrame

Example:

python
results = search_properties(df, {
  "city": "Mumbai",
  "bhk": "2",
  "budget": 9000000,
  "location_keywords": ["Chembur"]
})
Output: A filtered DataFrame with matching properties.

✅ summarizer.py — Result Summary
Generates a short summary of the search results.

Function: generate_summary(results: pd.DataFrame, filters: dict) → str

Example:

python
summary = generate_summary(results, filters)
Output:

Found 12 properties in Mumbai matching 2BHK under ₹90L. Prices range from ₹75L to ₹89L. Popular areas include Chembur and Kurla.

✅ helpers.py — Card Formatter
Formats each property row into a display-friendly dictionary.

Function: format_card(row: pd.Series) → dict

Example:

python
card = format_card(results.iloc[0])
Output:

python
{
  "title": "Sunshine Residency",
  "bhk": "2BHK",
  "price": "₹85L",
  "address": "Chembur, Mumbai",
  "possession": "Dec 2025",
  "cta": "https://nobrokerage.com/project/sunshine-residency"
}
📊 Data Files
These CSVs are merged to form the full property dataset:

ProjectConfigurationVariant.csv: Unit-level details (BHK, carpet area, price)

ProjectConfiguration.csv: Configuration metadata

project.csv: Project-level info (name, status, slug)

ProjectAddress.csv: Full address for each project

💬 Example Queries
Try asking:

3BHK in Pune under ₹1.2 Cr

2BHK in Mumbai near Chembur under ₹90L

1BHK in Pune ready to move

🎨 UI Styling
Background: rgb(97,64,2) (dark brown)

Title: gold (#FFD700)

Text: white (#FFFFFF)

Placeholder: light gray (#DDDDDD)

📌 Notes
Currently supports Pune and Mumbai

All data is static and loaded from CSVs

No external APIs or databases required

Easily extendable to other cities or data sources

👨‍💻 Author
Built by Alok Kulkarni AI Engineer & Data Scientist Focused on real-world AI applications and polished frontend design