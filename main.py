import streamlit as st
from llm import get_response

st.set_page_config(
    page_title="LinkedIn Content Generator",
    page_icon="💻",
    layout="wide"
)

st.title("💻 LinkedIn Content Generator")
st.caption("Your Personalized AI LinkedIn Content Generator")
st.divider()

st.caption(
    "Use this AI according to your needs, powered by Groq."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input(
    "Give the prompt/text on which you need content generation."
)

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user", avatar="👨"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            response = get_response(st.session_state.messages)
            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

# Welcome message
if not st.session_state.messages:
    st.info(
        """
👋 Welcome to the LinkedIn Content Generator!

What is your topic?
"""
    )

# Sidebar
with st.sidebar:
    st.title("Options")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("Model")
    st.code("llama-3.3-70b-versatile")