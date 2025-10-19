import streamlit as st
import pandas as pd
from utils.parser import parse_query
from utils.search import search_properties
from utils.summarizer import generate_summary
from utils.helpers import format_card

# Load data
@st.cache_data
def load_data():
    variant_df = pd.read_csv(r'C:\Users\kulka\nobrokerage-ai\data\ProjectConfigurationVariant.csv')
    config_df = pd.read_csv(r'C:\Users\kulka\nobrokerage-ai\data\ProjectConfiguration.csv')
    project_df = pd.read_csv(r'C:\Users\kulka\nobrokerage-ai\data\project.csv')
    address_df = pd.read_csv(r'C:\Users\kulka\nobrokerage-ai\data\ProjectAddress.csv')

    for df in [variant_df, config_df, project_df, address_df]:
        df.columns = df.columns.str.strip().str.lower()

    merged = variant_df.merge(config_df, how='left', left_on='configurationid', right_on='id', suffixes=('', '_config'))
    merged = merged.merge(project_df, how='left', left_on='projectid', right_on='id', suffixes=('', '_project'))
    merged.drop(columns=['id_config', 'id_project'], inplace=True, errors='ignore')
    address_df = address_df.rename(columns={'id': 'address_id'})
    merged = merged.merge(address_df, how='left', on='projectid')

    merged['projectname'] = merged['projectname'].fillna('Unknown')
    merged['custombhk'] = merged['custombhk'].fillna(merged['type'])
    merged['bhk'] = merged['custombhk'].fillna(merged['type'])
    merged['price'] = pd.to_numeric(merged['price'], errors='coerce').fillna(0)
    merged['carpetarea'] = pd.to_numeric(merged['carpetarea'], errors='coerce').fillna(0)
    merged['fulladdress'] = merged['fulladdress'].fillna('NA')
    merged['possessiondate'] = merged['possessiondate'].fillna('NA')
    merged['status'] = merged['status'].fillna('NA')
    merged['slug'] = merged['slug'].fillna('unknown')

    return merged

df = load_data()

# UI setup
st.set_page_config(page_title="NoBrokerage AI", layout="wide")

# Inject custom styles
st.markdown(
    """
    <style>
        .stApp {
            background-color: rgb(97,64,2);
        }
        h1 {
            color: #FFD700 !important;
        }
        .styled-subtext {
            color: #ffffff !important;
            font-size: 18px;
            margin-bottom: 10px;
        }
        label, .stTextInput > div > input {
            color: #ffffff !important;
        }
        .stTextInput > div > input::placeholder {
            color: #dddddd !important;
        }
        .stMarkdown, .stDataFrame, .stSubheader, .stText, .stContainer, .stTable {
            color: #ffffff !important;
        }
        div[data-testid="stVerticalBlock"] {
            color: #ffffff !important;
        }
        .stButton button {
            color: #000000 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtext
st.markdown("<h1>🏡 NoBrokerage AI Chat</h1>", unsafe_allow_html=True)
st.markdown('<div class="styled-subtext">Ask me something like: <b>3BHK in Pune under ₹1.2 Cr</b></div>', unsafe_allow_html=True)

# Search bar with submit button
with st.form("query_form"):
    query = st.text_input("Your query", placeholder="e.g. 2BHK in Mumbai under ₹90L near Chembur")
    submitted = st.form_submit_button("🔍 Submit")

# Handle query
if submitted and query:
    filters = parse_query(query)

    if filters.get('invalid_city'):
        st.warning("🚫 Sorry, we currently support only Pune and Mumbai. Try searching in those cities!")
    else:
        results = search_properties(df, filters)
        summary = generate_summary(results, filters)

        st.markdown("### 📊 Summary")
        st.markdown(f"<div style='color:#ffffff'>{summary}</div>", unsafe_allow_html=True)

        if not results.empty:
            st.markdown("### 🏘️ Matching Properties")
            for _, row in results.iterrows():
                card = format_card(row)
                with st.container():
                    st.markdown(f"<h3 style='color:#ffffff'>{card['title']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<div style='color:#ffffff'><b>BHK:</b> {card['bhk']}<br>"
                                f"<b>Price:</b> {card['price']}<br>"
                                f"<b>Location:</b> {card['address']}<br>"
                                f"<b>Possession:</b> {card['possession']}<br>"
                                f"<a href='{card['cta']}' style='color:#FFD700'>🔗 View Project</a></div>",
                                unsafe_allow_html=True)
                    st.markdown("<hr>", unsafe_allow_html=True)
