import streamlit as st
import requests
import os

# -----------------------
# TribalDesk AI Grant Generator
# -----------------------

st.set_page_config(page_title="TribalDesk AI", page_icon="🌐", layout="wide")

# Title
st.title("🌐 TribalDesk AI – Grant Generator")

st.markdown("""
Welcome to **TribalDesk AI**!  
This tool helps you **search grants** and **draft proposals** quickly.  
""")

# Sidebar for navigation
menu = st.sidebar.radio("📂 Menu", ["Home", "Find Grants", "Generate Proposal", "About"])

# -----------------------
# Home
# -----------------------
if menu == "Home":
    st.subheader("🏠 Home")
    st.write("""
    - Use **Find Grants** to search open opportunities.  
    - Use **Generate Proposal** to draft a professional grant proposal.  
    - All powered by AI, built for tribal governments, non-profits, and small businesses.
    """)

# -----------------------
# Find Grants
# -----------------------
elif menu == "Find Grants":
    st.subheader("🔍 Find Grants")

    keyword = st.text_input("Enter a keyword (e.g., 'animal control', 'education', 'healthcare')")
    if st.button("Search Grants"):
        if keyword.strip() == "":
            st.warning("Please enter a keyword.")
        else:
            # Placeholder for API call
            st.success(f"Searching grants for: **{keyword}**")
            st.info("👉 In a real version, this would connect to Grants.gov or a funding database.")

            # Example results
            sample_grants = [
                {"title": "Animal Control & Welfare Support", "funder": "USDA", "deadline": "Dec 15, 2025"},
                {"title": "Community Health Initiative", "funder": "HHS", "deadline": "Jan 20, 2026"},
            ]
            for g in sample_grants:
                st.write(f"**{g['title']}**  \nFunder: {g['funder']}  \nDeadline: {g['deadline']}")

# -----------------------
# Generate Proposal
# -----------------------
elif menu == "Generate Proposal":
    st.subheader("📝 Generate Proposal")

    org_name = st.text_input("Organization Name")
    project_name = st.text_input("Project Name")
    project_goal = st.text_area("Project Goal / Description")
    funding_amount = st.text_input("Requested Funding Amount")

    if st.button("Generate Proposal Draft"):
        if not org_name or not project_name or not project_goal or not funding_amount:
            st.warning("Please fill in all fields.")
        else:
            st.success("✅ Proposal Draft Generated")
            st.markdown(f"""
            ### Grant Proposal Draft  

            **Organization:** {org_name}  
            **Project Name:** {project_name}  
            **Requested Funding:** {funding_amount}  

            **Project Goal:**  
            {project_goal}  

            **Expected Impact:**  
            This project will strengthen the community by addressing key needs and creating lasting impact.
            """)

# -----------------------
# About
# -----------------------
elif menu == "About":
    st.subheader("ℹ️ About TribalDesk AI")
    st.write("""
    TribalDesk AI is a platform designed to:
    - Help tribes, nonprofits, and small businesses **find funding**.  
    - Generate **professional proposals** quickly.  
    - Streamline the grant application process.  

    Built with ❤️ using Streamlit + AI.
    """)
