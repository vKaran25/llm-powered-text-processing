from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field
import streamlit as st

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    api_key=api_key
)  

#1.remove white spacing and formatting
#2.identify and separate headline from body content
#3.Extract key elements: dates, names, locations, statistics
#4.Language detection for multilingual support
class Text_preprocessing_model(BaseModel):
    whitespacing_remover:str = Field(description='Remove excessive whitespace and formatting')
    headline_separater:str = Field(description='identify and separate headline from body content')
    extract_key_elements:str = Field(description='Extract key elements: dates, names, locations, statistics')
    language_detection:str = Field(description='Identify the language the text is provided in')

with open("system_prompt.txt",mode='r',encoding="utf-8") as f:
    system = f.read()

    structured_llm = llm.with_structured_output(Text_preprocessing_model)
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", "{input}")])
    chain = prompt | structured_llm

sentence_input = st.text_area('Paste the text you want to process',key='user_input')
if st.button('process text',type='primary'):
    if not sentence_input:
        st.warning("Please enter a valid input")
        st.stop()
    with st.spinner('processing your request'):
        try:
            result = chain.invoke({'input':sentence_input})
            st.success('Processing complete')
            st.subheader('Extracting data')
            st.json(result.dict(),expanded=True)
        except:
            st.error

# use this as input
#   **NEW DELHI** - A shocking new scam has emerged targeting elderly citizens. Reports indicate that over 500 people, primarily in the National Capital Region (NCR), have lost their life savings. The perpetrators, reportedly part of an international syndicate, contact victims claiming the government is converting old currency to the new Digital Rupee. They trick victims into sharing bank details on a fake government website. The first cases were reported on September 15, 2025, with total losses estimated at ₹50 lakh. Police are advising everyone to be cautious. The main suspect, **Rakesh Sharma**, is believed to be the mastermind.
