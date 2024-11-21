# Multilingual Translator Chatbot

Multilingual Translator is a Streamlit-based web application that leverages Groq's Mixtral model for accurate translations between multiple languages. Users can input text, select the source and target languages, and receive translations in real-time. This app is designed to provide seamless and efficient language translation using advanced AI models.

## Features

- Multi-language support: Translates text between various languages like English, German, Spanish, French, Chinese, and Hindi.
- Real-time translation: Get instant translations with just a few clicks.
- Customizable model settings: You can adjust parameters such as temperature, max tokens, and retries to suit your needs.
- Simple interface: Built using Streamlit, the interface is intuitive and easy to use.

## Requirements

### Ensure you have the following installed:
    - Python 3.7 or higher

<!--Start code-->
### Install the required dependencies using pip:
    pip install -r requirements.txt
<!-- end code-->


## How It Works

### 1.Initialize the Groq Language Model: 
The app uses the ChatGroq model from the langchain_groq package. The parameters such as temperature and retries are configurable.

### 2.Define a Translation Prompt: 
A custom prompt is defined using ChatPromptTemplate to instruct the model on translating between the selected languages.

<!--start code-->
### 3.Open the app in your browser:
    streamlit run app.py
<!-- end code-->

### 4.Streamlit Interface: 
The app provides an interactive interface where users can:
- Input text to translate.
- Choose the source and target languages.
- Click a button to get the translated text in real-time.

## Example

- Input Text: "I love programming."
- Input Language: "English"
- Output Language: "German"
- Translated Text: "Ich liebe Programmieren."

## Project Structure
- app.py: Streamlit code
- main.py: Main code of project
- requirements.txt: Required Python libraries
- README.md: Project documentation