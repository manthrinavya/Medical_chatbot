import streamlit as st
import sys

sys.path.append("src")

from chatbot import get_response
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Title */
h1 {
    color: white;
    text-align: center;
    font-size: 42px;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 12px;
    margin: 8px 0;
    backdrop-filter: blur(8px);
}

/* Input Box */
.stChatInput input {
    border-radius: 20px;
}

/* Text Color */
p, label, div {
    color: white;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Medical Chatbot")

st.title("🏥 Medical Q&A Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a medical question...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer, entities = get_response(prompt)

    response = str(answer) if answer else "sorry, i couldn't find the an answer"

    if entities:
        response += "\n\n**Entities Found:**\n"
        for entity_type, entity in entities:
            response += f"- {entity_type}: {entity}\n"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )