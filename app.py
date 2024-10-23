import streamlit as st
from views.login import user_login
from views.update_pajsk import update_pajsk
from components.table import show_table

# Page config
st.set_page_config(
    page_title='Pengiraan PAJSK KTETF',
    page_icon='abacus',
    layout='wide',
)

# App Starts
if not user_login(): st.stop()

if st.button("Log out", use_container_width=True):

    st.session_state.clear()
    st.rerun()

def main():

    # Page title
    st.title('PAJSK KTETF')
    st.markdown('---')

    if st.button('Update PAJSK'):
        st.session_state['next_page'] = 'update_pajsk'
        st.rerun();
    
    show_table(st.session_state['user_data_db'].iloc[0].to_dict())

# Page Navigation
if 'next_page' not in st.session_state or st.session_state['next_page'] == 'main':

    if st.session_state['username'][0] == 'p':
        main()
    elif st.session_state['username'][0] == 'g':
        st.write('hello guru')
    elif st.session_state['username'][0] == 's':
        st.write('hello SU')
elif st.session_state['next_page'] in ['update_pajsk', 'confirm_update']:
    update_pajsk()

# Footer
st.markdown('---')
st.markdown('Copyright © 2024 JYJH. All Rights Reserved')

st.write(st.session_state)