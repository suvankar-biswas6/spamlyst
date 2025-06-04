import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
# Download necessary NLTK resources
nltk.download('punkt_tab')
nltk.download('stopwords')

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model_mnb.pkl', 'rb'))

st.set_page_config(
    page_title="Spamlyst", 
    page_icon="📩",   
)
st.title("Spamlyst - Email Spam Classifier")
input_mail = st.text_area("Enter the email message")


#steps


def transform_text(text):
    text = text.lower()  # convert to lowercase
    text = nltk.word_tokenize(text)  # tokenize the text eg- ['hello', 'how', 'are', 'you']
    
    y = []
    # stopwords and puntuation removal
    for i in text:
        # if i not in stopwords.words('english') and i not in string.punctuation:
        if i not in string.punctuation:
            # if the word is not a stopword and not a punctuation, keep it
            y.append(i)
            
    text = y[:]
    y.clear()  # clear the list for reuse
    for i in text:
        if i.isalnum():
            y.append(i)  # keep only alphanumeric characters
            
    text = y[:]
    y.clear()
    # lemmatization
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)

if st.button("Predict"):

    #1. Preprocess the input email
    cleaned_mail = transform_text(input_mail)

    #2. Vectorize using tfidf
    vector_input = tfidf.transform([cleaned_mail])  # Vectorize the cleaned email

    #3. predict using the model
    result = model.predict(vector_input)[0]  # Predict using the trained model

    #4. Display the result
    if(result == 1):
        st.header("Spam")
    else:
        st.header("Not Spam")
        
        
        
footer_html = """
<hr style="margin-top: 3em; margin-bottom: 1em;">
<div style="text-align:center; font-size:0.85em; color:gray;">
 Spamlyst  © 2025  • All rights reserved <a href="https://www.linkedin.com/in/suvankarbiswasju/" target="_blank">LinkedIN</a> • <a href="https://github.com/suvankar-biswas6" target="_blank">GitHub</a>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
