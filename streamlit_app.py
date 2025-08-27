import streamlit as st
import openai

# --- Page Config ---
st.set_page_config(
    page_title="TribalDesk AI",
    page_icon="🌿",
    layout="centered"
)

# --- Sidebar Navigation ---
st.sidebar.title("🌿 TribalDesk AI")
page = st.sidebar.radio("Go to:", ["Home", "AI Assistant"])

# --- Home / Landing Page ---
if page == "Home":
    st.title("🌿 Welcome to TribalDesk AI")
    st.subheader("Your AI-powered partner for Tribal Grants, Business, and Mediation Tools")

    st.markdown(
        """
        ### What TribalDesk AI Does:
        - 📑 Generate and organize **grant proposals**
        - ⚖️ Support **Tribal Peacekeeping Mediation Programs**
        - 📊 Build tools for **tribal businesses and governments**
        - 💡 Provide **AI-powered insights** for your projects

        ---
        **Getting Started:**
        - Use the sidebar to switch to the **AI Assistant**
        - Ask questions, draft documents, and explore grant opportunities
        """
    )

    st.success("Tip: Add more pages later (Grants, Mediation, Business Tools).")

# --- AI Assistant Page ---
elif page == "AI Assistant":
    st.title("🤖 TribalDesk AI Assistant")

    # User input
    user_input = st.text_area("Ask me anything about grants, mediation, or tribal business:")

    if st.button("Send"):
        if not user_input.strip():
            st.warning("Please enter a question first.")
        else:
            try:
                # Call OpenAI API
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are TribalDesk AI, an expert in grants, mediation, and tribal business support."},
                        {"role": "user", "content": user_input}
                    ]
                )
                ai_reply = response.choices[0].message.content
                st.markdown(f"**AI Response:**\n\n{ai_reply}")

            except Exception as e:
                st.error(f"Error: {e}")
