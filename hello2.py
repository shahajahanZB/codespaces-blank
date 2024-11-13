from langchain_groq import ChatGroq
import streamlit as st
from langchain.prompts import ChatPromptTemplate
st.title("zhan bot/custom gpt")
llm=ChatGroq(model = 'llama-3.1-70b-versatile', api_key = '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')

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a programming teacher, so you have to give technical answers to the users, pls help users with respect to query"),
        ("user","{query}")
    ]
)
query=st.text_input("ask me anything :")
if query:
    formatted_prompt = prompt.format(query=query)
    # After invoking the model and getting the response
    response = llm.invoke(formatted_prompt)

# Limit the response to 20 words, for example
    max_words = 100
    response_text = response.content
    response_words = response_text.split()

# Take the first `max_words` words
    short_response = " ".join(response_words[:max_words])

    st.write(short_response)