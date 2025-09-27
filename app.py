import streamlit as st
from agent import agent

st.set_page_config(page_title="🏃 Fitness & Nutrition AI", page_icon="🏋️‍♂️", layout="centered")

st.markdown(
    """
    <div style='text-align: center;'>
        <h1>🏃 Fitness & Nutrition Assistant</h1>
        <p>Ask me about workouts, meals, motivation, or the Starting Strength book!</p>
    </div>
    """,
    unsafe_allow_html=True
)

user_input = st.text_input("💬 Enter your question here:")

if user_input:
    with st.spinner("Thinking..."):
        response = agent.run(user_input)
    st.markdown(
        f"""
        <div style='background-color:#f0f2f6;color:#000000;padding:10px;border-radius:8px;margin-top:10px;'>
            <strong>Answer:</strong><br>{response}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div style='text-align:center;margin-top:40px;color:gray;'>
        Made by <strong>Manan Ch</strong>
    </div>
    """,
    unsafe_allow_html=True
)


