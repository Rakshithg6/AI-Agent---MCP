import streamlit as st
import requests

st.title("AI Customer Support Agent with Ollama RAG")

# Session ID handling
session_id = st.session_state.get("session_id", "user_123")
st.session_state["session_id"] = session_id

# Chat Interface
user_input = st.text_input("Enter your query:")
if st.button("Send"):
    try:
        res = requests.post("http://localhost:8000/chat", data={
            "session_id": session_id,
            "message": user_input
        })
        res.raise_for_status()
        st.success(res.json()["reply"])
    except Exception as e:
        st.error(f"Chat request failed: {e}")

# PDF Upload Interface
st.write("---")
st.subheader("Upload PDF for Knowledge Base")
file = st.file_uploader("Upload PDF", type=["pdf"])
if file:
    try:
        res = requests.post(
            "http://localhost:8000/upload/",
            files={"file": (file.name, file, "application/pdf")}
        )
        res.raise_for_status()
        res_json = res.json()
        st.success(res_json["status"])
    except Exception as e:
        st.error("❌ Failed to upload or parse response from backend.")
        st.text(f"Error: {e}")
