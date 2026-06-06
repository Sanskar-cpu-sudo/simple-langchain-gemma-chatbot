import os
from dotenv import load_dotenv

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()

# LangSmith Configuration
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

if LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

if LANGCHAIN_PROJECT:
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="LangChain Gemma Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("⚙️ Configuration")
st.sidebar.info(
    """
    **Model:** Gemma 2B
    
    **Framework:** LangChain
    
    **Frontend:** Streamlit
    
    **Backend:** Ollama
    """
)

st.sidebar.markdown("---")
st.sidebar.write("Make sure Ollama is running locally.")

# --------------------------------------------------
# Main Title
# --------------------------------------------------
st.title("🤖 LangChain Demo with Gemma 2B")
st.write("Ask any question and get a response from the Gemma model running through Ollama.")

# --------------------------------------------------
# Prompt Template
# --------------------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Provide clear, concise, and accurate answers."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)

# --------------------------------------------------
# Initialize LLM
# --------------------------------------------------
try:
    llm = Ollama(model="gemma:2b")
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

except Exception as e:
    st.error(f"Failed to initialize model: {e}")
    st.stop()

# --------------------------------------------------
# User Input
# --------------------------------------------------
input_text = st.text_input(
    "💬 Enter your question:",
    placeholder="Example: What is Artificial Intelligence?"
)

# --------------------------------------------------
# Generate Response
# --------------------------------------------------
if st.button("Generate Response"):

    if not input_text.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Generating response..."):
                response = chain.invoke(
                    {"question": input_text}
                )

            st.success("Response Generated Successfully!")

            st.subheader("📌 Answer")
            st.write(response)

        except Exception as e:
            st.error(
                f"Error while generating response.\n\nDetails: {str(e)}"
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Built using Streamlit, LangChain, Ollama, and Gemma 2B"
)
