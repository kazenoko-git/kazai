import streamlit as st
import ai
st.set_page_config(page_title="Sozomi LLM", page_icon=":tada:", layout="wide") # https://www.webfx.com/tools/emoji-cheat-sheet/
with st.container():
    global AI
    st.header("sozomi LLM")
    st.text_input("your username: ", key="username")
    name = str(st.session_state.username)
    AI = ai.AI(username=name, model=1)

with st.container():
    if "username" not in st.session_state:
        st.write("please enter your username first.")
    else:
        st.write("---")
        st.subheader("chat with Sozomi!")
        st.text_input("chat with Sozomi!", key="prompt", label_visibility="hidden")
        if "prompt" not in st.session_state:
            pass
        else:
            prompt = str(st.session_state.prompt)
            result = AI.ask(prompt)
            st.write(f"Sozomi: {result}")