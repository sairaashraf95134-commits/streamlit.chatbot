import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

#-------------Page-------------

st.title("Chatbot with Groq API")
st.caption("Ask anything and get instant responses!")

st.divider()

#--------------Chat form-------------------

with st.form("Chat_form"):
    user_input = st.text_area(
        "Your Message",
        placeholder="Type your question here....."
    )

    submittedd = st.form_submit_button("Send")

#---------Answer---------------

if submittedd:

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        api_key=api_key,
    )

    with st.spinner("Thinking..."):

        response = llm.invoke([
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=user_input)
        ])

        st.divider()
        st.subheader("Response:")
        st.write(response.content)