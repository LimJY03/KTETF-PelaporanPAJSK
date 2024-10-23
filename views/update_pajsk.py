import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from components.constants import (
    JAWATAN_KELAB,
    PERINGKAT_KELAB,
    PENCAPAIAN_KELAB,
    JAWATAN_PROJEK,
    PERINGKAT_PROJEK,
    EXTRA_KOKO_PERKHIDMATAN,
    EXTRA_KOKO_ANUGERAH,
)
from components.table import show_table

def update_pajsk():

    user_data_st = st.session_state['user_data_db'].iloc[0].to_dict()

    if st.session_state['next_page'] == 'update_pajsk':

        # Page title
        st.title('Update PAJSK KTETF')
        st.markdown('---')

        # Logic
        tab1, tab2, tab3, tab4 = st.tabs(['SUKAN/PERMAINAN', 'KELAB/PERSATUAN', 'BADAN BERUNIFORM', 'EKSTRA KURIKULUM'])

        with tab1:
            col1, col2 = st.columns(2)
            with col1: 
                user_data_st['s_jawatan'] = st.selectbox(
                    'Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 0',
                    index=list(JAWATAN_KELAB.keys()).index(user_data_st['s_jawatan'])
                )
                user_data_st['s_peringkat'] = st.selectbox(
                    'Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 0',
                    index=list(PERINGKAT_KELAB.keys()).index(user_data_st['s_peringkat'])
                )
                user_data_st['s_pencapaian'] = st.selectbox(
                    'Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 0',
                    index=list(PENCAPAIAN_KELAB.keys()).index(user_data_st['s_pencapaian'])
                )
            with col2:
                user_data_st['s_nama_p'] = st.text_input(
                    'Nama Projek', key='Nama Projek 0',
                    value=user_data_st['s_nama_p']
                )
                user_data_st['s_jawatan_p'] = st.selectbox(
                    'Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 0',
                    index=list(JAWATAN_PROJEK.keys()).index(user_data_st['s_jawatan_p'])
                )
                user_data_st['s_peringkat_p'] = st.selectbox(
                    'Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 0',
                    index=list(PERINGKAT_PROJEK.keys()).index(user_data_st['s_peringkat_p'])
                )

        with tab2:
            col1, col2 = st.columns(2)
            with col1: 
                user_data_st['p_jawatan'] = st.selectbox(
                    'Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 1',
                    index=list(JAWATAN_KELAB.keys()).index(user_data_st['p_jawatan'])
                )
                user_data_st['p_peringkat'] = st.selectbox(
                    'Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 1',
                    index=list(PERINGKAT_KELAB.keys()).index(user_data_st['p_peringkat'])
                )
                user_data_st['p_pencapaian'] = st.selectbox(
                    'Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 1',
                    index=list(PENCAPAIAN_KELAB.keys()).index(user_data_st['p_pencapaian'])
                )
            with col2:
                user_data_st['p_nama_p'] = st.text_input(
                    'Nama Projek', key='Nama Projek 1',
                    value=user_data_st['p_nama_p']
                )
                user_data_st['p_jawatan_p'] = st.selectbox(
                    'Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 1',
                    index=list(JAWATAN_PROJEK.keys()).index(user_data_st['p_jawatan_p'])
                )
                user_data_st['p_peringkat_p'] = st.selectbox(
                    'Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 1',
                    index=list(PERINGKAT_PROJEK.keys()).index(user_data_st['p_peringkat_p'])
                )

        with tab3:
            col1, col2 = st.columns(2)
            with col1: 
                user_data_st['b_jawatan'] = st.selectbox(
                    'Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 2',
                    index=list(JAWATAN_KELAB.keys()).index(user_data_st['b_jawatan'])
                )
                user_data_st['b_peringkat'] = st.selectbox(
                    'Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 2',
                    index=list(PERINGKAT_KELAB.keys()).index(user_data_st['b_peringkat'])
                )
                user_data_st['b_pencapaian'] = st.selectbox(
                    'Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 2',
                    index=list(PENCAPAIAN_KELAB.keys()).index(user_data_st['b_pencapaian'])
                )
            with col2:
                user_data_st['b_nama_p'] = st.text_input(
                    'Nama Projek', key='Nama Projek 2',
                    value=user_data_st['b_nama_p']
                )
                user_data_st['b_jawatan_p'] = st.selectbox(
                    'Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 2',
                    index=list(JAWATAN_PROJEK.keys()).index(user_data_st['b_jawatan_p'])
                )
                user_data_st['b_peringkat_p'] = st.selectbox(
                    'Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 2',
                    index=list(PERINGKAT_PROJEK.keys()).index(user_data_st['b_peringkat_p'])
                )

        with tab4:
            user_data_st['ek_perkhidmatan'] = st.selectbox(
                'Ekstra Kurikulum Perkhidmatan', options=EXTRA_KOKO_PERKHIDMATAN.keys(),
                index=list(EXTRA_KOKO_PERKHIDMATAN.keys()).index(user_data_st['ek_perkhidmatan'])
            )
            user_data_st['ek_anugerah'] = st.selectbox(
                'Ekstra Kurikulum Anugerah Khas', options=EXTRA_KOKO_ANUGERAH.keys(),
                index=list(EXTRA_KOKO_ANUGERAH.keys()).index(user_data_st['ek_anugerah'])
            )

        left, _, right = st.columns([1, 3, 1])

        if left.button('<- Back', use_container_width=True):

            st.session_state['next_page'] = 'main'
            st.rerun()

        if right.button('Next ->', use_container_width=True):

            st.session_state['next_page'] = 'confirm_update'
            st.session_state['user_data_st'] = user_data_st
            st.rerun()

    else:
        
        show_table(st.session_state['user_data_st'])

        left, _, right = st.columns([1, 3, 1])

        if left.button('<- Back', use_container_width=True):

            st.session_state['next_page'] = 'update_data_st'
            st.rerun()

        if right.button('Confirm Submit', use_container_width=True):

            # Update Session State
            st.session_state['user_data_db'].loc[st.session_state['user_data_db'].index[0]] = pd.Series(
                st.session_state['user_data_st'],
                index=st.session_state['user_data_db'].columns
            )

            # Update Database
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
            worksheet.update(f"C{st.session_state['user_data_db'].index[0] + 2}", [list(st.session_state['user_data_st'].values())])

            # Redirect to main
            st.session_state['next_page'] = 'main'
            st.rerun()