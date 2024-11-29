from openai import OpenAI
import streamlit as st
from langdetect import detect

model_options = [
    "gpt-3.5-turbo",
    "gpt-4",
    "gpt-4-turbo",
    "gpt-4o",
    "gpt-4o-mini",
]
selected_model = st.selectbox("Select Model", model_options, index=3)

inp = st.text_input("Prompt")
but = st.button("Send")

if but and inp != "":
    try:
        lang = detect(inp)
    except:
        lang = "en"  

    text_direction = "rtl" if lang == "fa" else "ltr"

    client = OpenAI(
        api_key="NotNeededAnyAPIKey",
        base_url="http://localhost:1337/v1",
    )

    response = client.chat.completions.create(
        model=selected_model,
        messages=[
            {
                "role": "user",
                "content": inp
            }
        ],
    )

    st.markdown(
        f'<div style="direction: {text_direction};">{response.choices[0].message.content}</div>',
        unsafe_allow_html=True
    )
