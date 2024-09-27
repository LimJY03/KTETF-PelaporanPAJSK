import hmac
import streamlit as st

def user_login():

    def login_form():
        with st.form("Credentials"):
            st.markdown('## Login to KTETF - Pengiraan PAJSK')
            st.markdown('---')
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)
            st.markdown('---')
            st.markdown('Copyright © 2024 JYJH. All Rights Reserved')

    def password_entered():
        if st.session_state["username"] == st.secrets["username"] and hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # The username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False