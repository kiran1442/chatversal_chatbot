import streamlit as st
from main import *


# Streamlit UI
st.title("Multilingual Translator Chatbot")
st.markdown("""
This app uses **Groq's Mixtral model** to provide accurate translations between languages.
Simply type your text, choose the source and target languages, and get your translation!
""")

# Input text
input_text = st.text_area("Enter text to translate:", placeholder="Type here...")

# Language selection
LANGUAGES = {
    "English": "English",
    "German": "German",
    "Spanish": "Spanish",
    "French": "French",
    "Chinese": "Chinese",
    "Hindi": "Hindi",
}

input_language = st.selectbox("Select the input language:", options=list(LANGUAGES.keys()))
output_language = st.selectbox("Select the output language:", options=list(LANGUAGES.keys()))
# Translate button
if st.button("Translate"):
    if input_text.strip():
        try:
            # Create the translation chain
            chain = prompt | llm
            response = chain.invoke(
                {
                    "input_language": input_language,
                    "output_language": output_language,
                    "input": input_text,
                }
            )
            response_content = response.content
            print(response_content)
        
            # Display the result
            st.success("Translation completed!")
            st.write(f"**Translated Text:** {response.content}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter text to translate.")
