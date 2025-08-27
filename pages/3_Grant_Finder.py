import streamlit as st
import pandas as pd
from utils.storage import ensure_data_dir, load_csv, save_csv
from pathlib import Path


st.set_page_config(page_title="Grant Finder", page_icon="🔎", layout="wide")
st.title("🔎 Grant Finder & Tracker")
st.caption("Manually add and track grants. Advanced scraping/search can be added later.")


ensure_data_dir()
DATA_FILE = Path("data/grants.csv")


# Load
