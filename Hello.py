import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=st.secrets["api_key"])

# Set up the model and generation config
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)



#---------------------------------------------


st.set_page_config(page_title="Generative ai app",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Jagan's app")

prompt=st.text_input("Enter the Text here")


    
submit=st.button("Generate")

## Final response
if submit:
    response=model.generate_content(prompt)
    st.write(response.text)