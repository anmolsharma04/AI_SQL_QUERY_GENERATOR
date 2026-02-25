import streamlit as st
from data_loader import load_csv, load_api
from llm_engine import generate_sql
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="AI SQL Generator", layout="wide")
st.title("💡 AI SQL Query Generator")

# Initialize session state
if "df" not in st.session_state:
    st.session_state.df = None

source_option = st.radio(
    "Choose Data Source:",
    ("Upload CSV", "Load from API")
)

# ---------------- CSV Upload ----------------
if source_option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        st.session_state.df = load_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(st.session_state.df.head())

# ---------------- API Load ----------------
elif source_option == "Load from API":
    api_url = st.text_input("Enter API URL:")
    
    if st.button("Fetch Data"):
        try:
            st.session_state.df = load_api(api_url)
            st.success("API Data Loaded Successfully!")
            st.dataframe(st.session_state.df.head())
        except:
            st.error("Invalid API or data format.")

# ---------------- SQL Generation ----------------
if st.session_state.df is not None:
    
    columns = st.session_state.df.columns.tolist()
    schema_info = ", ".join(columns)

    st.subheader("Ask Your Question About the Data")
    user_question = st.text_input("Enter your data question:")

    if st.button("Generate SQL"):
        sql_query = generate_sql(schema_info, user_question)
        st.subheader("Generated SQL")
        st.code(sql_query, language="sql")