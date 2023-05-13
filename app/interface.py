import os
import pinecone
import streamlit as st
from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


# Setup wide layout on streamlit
st.set_page_config(page_title = "QA Dashboard")

# Define API Key from Secret Management Streamlit
OPENAI_KEY = st.secrets['OPENAI_KEY']
PINECONE_KEY = st.secrets['PINECONE_KEY']
ENVIRONMENT_NAME = st.secrets['ENVIRONMENT_NAME']

# Set environment variable of OPENAI Key
os.environ["OPENAI_API_KEY"] = OPENAI_KEY

# Initialize pinecone
pinecone.init(
    api_key = PINECONE_KEY,
    environment = ENVIRONMENT_NAME
)

# Create embedding based on OpenAIEmbedding technique
embeddings = OpenAIEmbeddings()

# Initialize document searching based on available index in Pinecone
index_name = "test-index"
docsearch = Pinecone.from_existing_index(index_name, embeddings)

# define LLM and QA Object
llm = OpenAI(temperature=0.2)
qa = RetrievalQA.from_chain_type(
    llm = llm, 
    chain_type = "stuff", 
    retriever = docsearch.as_retriever(search_kwargs={"k": 2})
)


if __name__ == "__main__":
    st.header("Question-Answering Product Related IoT: ESP32")
    st.image("https://d3n0h9tb65y8q.cloudfront.net/public_assets/assets/000/001/531/original/IOT.png?1635516393")
    text_input = st.text_input("", placeholder = "Input Text Here...")
    if text_input != "":
        result = qa.run(text_input)
        st.success(
            f"Answer: {result}"
        )