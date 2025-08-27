import streamlit as st
company_context = ctx_path.read_text(encoding="utf-8") if ctx_path.exists() else ""


# Model selection (defaults)
model_default = st.secrets.get("OPENAI_MODEL", "gpt-4o-mini")
model = st.sidebar.selectbox("Model", [model_default, "gpt-4o", "gpt-4o-mini", "gpt-4.1-mini", "gpt-3.5-turbo"], index=0)


# Initialize
if "chat_history" not in st.session_state:
st.session_state.chat_history = [
{"role": "system", "content": (
"You are TribalDesk AI, an expert assistant for Tribal governments, nonprofits, and Native-owned businesses. "
"Be clear, concise, and culturally respectful. Use the provided company context when helpful.\n\n" + company_context
)}
]


client = get_client()


# Chat UI
for msg in [m for m in st.session_state.chat_history if m["role"] != "system"]:
if msg["role"] == "user":
st.markdown(f"**You:** {msg['content']}")
else:
st.markdown(f"**Assistant:** {msg['content']}")


user_input = st.text_area("Type your question…", placeholder="How do I structure a DOJ CTAS proposal?", height=100)
col_send, col_clear = st.columns([1,1])
if col_send.button("Send"):
if user_input.strip():
st.session_state.chat_history.append({"role": "user", "content": user_input})
try:
stream = client.chat.completions.create(
model=model,
messages=st.session_state.chat_history,
stream=True
)
full = ""
placeholder = st.empty()
for chunk in stream:
delta = chunk.choices[0].delta.get("content", "")
full += delta
placeholder.markdown(f"**Assistant:** {full}")
st.session_state.chat_history.append({"role": "assistant", "content": full})
except Exception as e:
st.error(f"OpenAI error: {e}")
if col_clear.button("Clear Chat"):
st.session_state.chat_history = st.session_state.chat_history[:1] # keep system
st.experimental_rerun()


st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
