import streamlit as st

st.title("🎈link gacor")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import datetime
import streamlit as st

bils = st.date_input("When's your birthday", datetime.date(2007, 3, 4))
st.write("Your birthday is:", bils)
