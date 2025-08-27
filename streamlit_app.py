import streamlit as st
import openai

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="TribalDesk AI",
    page_icon="🌐",
    layout="wide"
)

# -------------------------
# LANDING PAGE
# -------------------------
st.title("🌐 TribalDesk AI")
st.write("Your interactive AI assistant for grants, tribal governance, and small business support.")

st.markdown("""
Welcome to **TribalDesk AI** — a platform designed to help tribes, nonprofits, and small businesses 
access funding, resources, and tools for growth.  

👉 Use the navigation sidebar to explore features like:
- **Grant Generator** – draft tailored proposals  
- **Funding Database** – explore current opportunities  
- **Peacekeeping Program Tools** – support tribal court mediation  
- **Business Resources** – documents, contracts, and guides  
""")

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Grant Generator", "Funding Database", "AI Assistant"])

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":
    st.subheader("Welcome to TribalDesk AI")
    st.write("Select a tool from the sidebar to get started.")

# -------------------------
# GRANT GENERATOR
# -------------------------
elif page == "Grant Generator":
    st.subheader("Grant Proposal Generator")
    grant_topic = st.text_input("Enter your project focus (e.g., Tribal Health, Animal Control, Mediation)")
    
    if st.button("Generate Proposal Draft"):
        if grant_topic:
            st.success(f"Here’s a draft for your project: **{grant_topic}**")
            st.write("🔹 [AI-generated proposal draft will appear here once we connect OpenAI.]")
        else:
            st.warning("Please enter a project focus.")

# -------------------------
# FUNDING DATABASE
# -------------------------
elif page == "Funding Database":
    st.subheader("Funding Opportunities")
    st.write("🔍 Here you’ll be able to search tribal, federal, foundation, and corporate grants.")
    st.info("Database integration coming soon!")

# -------------------------
# AI ASSISTANT
# -------------------------
elif page == "AI Assistant":
    st.subheader("Chat with TribalDesk AI")
    user_input = st.text_area("Ask a question:")
    
    if st.button("Ask"):
        if user_input:
            st.write("🤖 AI Response:")
            st.write("🔹 [AI-generated response will appear here once we connect OpenAI.]")
        else:
            st.warning("Please enter a question.")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.caption("🚀 Powered by Streamlit | TribalDesk AI © 2025")
