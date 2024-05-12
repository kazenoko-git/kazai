import streamlit as st

st.set_page_config(page_title="Kaz-AI", page_icon=":tada:", layout="wide") # https://www.webfx.com/tools/emoji-cheat-sheet/

with st.container():
    st.subheader("kaz.ai")
    st.title("the worst ai to ever exist")

with st.container():
    st.write("---")
    leftCol, rightCol = st.columns(2)
    with leftCol:
        st.header("What the AI can do:")
        st.write("Can Never Give You Up ✅")
        st.write("Can Never Let You Down ✅")
        st.write("Can Never Run Around✅")
        st.write("And Desert You✅")
    with rightCol:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("not funny?", anchor="right")

with st.container():
    st.write("---")
    st.title("what model do you wanna use?")
    st.text_input("what model do you wanna use?",key="model", label_visibility="hidden")


