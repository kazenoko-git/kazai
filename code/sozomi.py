import streamlit as st


st.set_page_config(page_title="Sozomi LLM", page_icon=":tada:", layout="wide") # https://www.webfx.com/tools/emoji-cheat-sheet/

with st.container():
    st.header("sozomi LLM")
    st.subheader("chat with Sozomi!")

with st.container():
    st.text_input("chat with Sozomi!", key="prompt", label_visibility="hidden")
    prompt = str(st.session_state.prompt)
    AI = ai.AI(username="kazenoko", model=1)
    result = AI.ask(prompt)
    st.write(result)