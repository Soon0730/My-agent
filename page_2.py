import streamlit as st

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state.messages

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "ai", "content": "Hello! How can I help you today?"})

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


