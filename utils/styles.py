import streamlit as st

def load_css():
    """
    Loads css styling into application.
    """

    st.markdown("""
    <style>
    
    /* Center headings */
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }
    /* Center normal text */
    p {
        text-align: center;
    }
    /* Center markdown containers */
    div[data-testid="stMarkdownContainer"] {
        text-align: center;
    }
    /* Center labels */
    label {
        text-align: center;
        display: block;
    }
    /* White buttons and black text */
    .stButton > button {
        background-color: white;
        color: black;
    }
    /* Text (Name) input field */
    .stTextInput input {
        background-color: white;
        color: black;
    }

    </style>
    """, unsafe_allow_html=True)