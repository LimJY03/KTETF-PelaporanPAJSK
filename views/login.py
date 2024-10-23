import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

def user_login():

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    skey = st.secrets["gcp_service_account"]
    credentials = Credentials.from_service_account_info(
        skey,
        scopes=scopes,
    )
    client = gspread.authorize(credentials)

    url = st.secrets['sheet_url']
    sh = client.open_by_url(url)
    worksheet = sh.worksheet('Student')  

    df_credential = pd.DataFrame(worksheet.get_all_records())

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Function to check credentials
    def get_user_data(username, password):
        valid_user = df_credential[(df_credential["username"] == username) & (df_credential["password"] == password)]
        return valid_user

    if not st.session_state['logged_in']:

        with st.form("Credentials"):

            st.markdown('## Login to KTETF - Pengiraan PAJSK')
            st.markdown('---')
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Log in")

            if submit_button:
                
                valid_user = get_user_data(username, password)

                if not valid_user.empty:

                    st.session_state['username'] = valid_user['username'].iloc[0]

                    valid_user.drop(columns=['username', 'password'], inplace=True)

                    for col in valid_user.columns:
                        if col[2:] == 'kehadiran':
                            valid_user[col].replace('', 0, inplace=True)
                        elif col[2:] == 'nama_p':
                            continue
                        else:
                            valid_user[col].replace('', 'Tiada', inplace=True)

                    st.session_state['user_data_db'] = valid_user
                    st.session_state['logged_in'] = True
                    st.success("Logged in successfully!")
                    st.cache_data.clear()
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
                    st.cache_data.clear()
        
            st.markdown('---')
            st.markdown('Copyright © 2024 JYJH. All Rights Reserved')

    if st.session_state['logged_in']:
        return True

    return False