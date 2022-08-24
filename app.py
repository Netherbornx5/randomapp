import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Riley's Website", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_tno6cg2w.json")
lottie_coding2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ngzwzxib.json")

with st.container():
    st.subheader("Hi, I'm a 12 year old programer.")
    st.title("Im a python coder")
    st.write("I like to code games with python, a will consider suggestions, and \n i will sometimes do suggested projects and post them on my github.")
    # how to create links:
    st.write("[python documentary ](https://www.python.org/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("i like to code games that are remakes of old retro-style games.")
        st.write("[My Github ](https://github.com/Netherbornx5)")
    with right_column:
        st_lottie(lottie_coding1, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("Links to my projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.write("Links:")
    with text_column:
        st.write("[Snake ](https://github.com/Netherbornx5/snake-game)")
        st.write("[Mine-Sweeper ](https://github.com/Netherbornx5/mine-sweeper)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_coding2, height=300, key="code")
    with text_column:
        st.write("[Space invaders ](https://github.com/Netherbornx5/Space-Invaders)")
        st.write("[Hangman ](https://github.com/Netherbornx5/Hangman/tree/main)")
with st.container():
    st.write("---")
    st.header("Get In Touch!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/mchughr009@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" placeholder="Your name" required>
        <input type="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Message  goes here"required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns((1, 3))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.write("      ")
