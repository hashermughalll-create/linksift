import streamlit as st
from stage1 import parse_url
from analyzer import analyze_url, calculate_score, risk_level

st.title("LinkSift")

user_url = st.text_input("URL to check")

if st.button("Analyze"):
    try:
        parts = parse_url(user_url)
        warnings = analyze_url(parts)
        score = calculate_score(warnings)

        st.write("Risk level:", risk_level(score), "| Score:", score)

        for warning in warnings:
            st.warning(warning["message"])
    except ValueError as error:
        st.error(str(error))