import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------------------
# Utility functions
# ---------------------------

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "grants.csv"

def ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)

def load_csv():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Grant Name", "Source", "Deadline", "Status", "Notes"])

def save_csv(df):
    df.to_csv(DATA_FILE, index=False)


# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="Grant Finder", page_icon="🔎", layout="wide")
st.title("🔎 Grant Finder & Tracker")
st.caption("Manually add and track grants. Advanced scraping/search can be added later.")

# Ensure folder exists
ensure_data_dir()

# Load existing grants
df = load_csv()

# ---------------------------
# Add New Grant
# ---------------------------

with st.expander("➕ Add a New Grant"):
    with st.form("grant_form", clear_on_submit=True):
        name = st.text_input("Grant Name")
        source = st.text_input("Funding Source")
        deadline = st.date_input("Deadline")
        status = st.selectbox("Status", ["Not Applied", "In Progress", "Submitted", "Awarded", "Denied"])
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Grant")
        if submitted:
            new_entry = pd.DataFrame([{
                "Grant Name": name,
                "Source": source,
                "Deadline": deadline,
                "Status": status,
                "Notes": notes
            }])
            df = pd.concat([df, new_entry], ignore_index=True)
            save_csv(df)
            st.success(f"✅ Added grant: {name}")


# ---------------------------
# Display Grants
# ---------------------------

st.subheader("📋 Tracked Grants")
if df.empty:
    st.info("No grants added yet. Use the form above to add one.")
else:
    st.dataframe(df, use_container_width=True)

    # Allow download
    st.download_button(
        "📥 Download as CSV",
        df.to_csv(index=False).encode("utf-8"),
        "grants.csv",
        "text/csv"
    )
