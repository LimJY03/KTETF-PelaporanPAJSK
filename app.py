import streamlit as st

# Page config
st.set_page_config(
    page_title='Pengiraan PAJSK KTETF',
    # page_icon='maths',
    layout='wide',
)

# Page title
st.title('Pengiraan PAJSK KTETF')
st.markdown('---')

# Page input: [sukan, kelab, uniform]
user_data = {
    'Kehadiran Kelab': [0, 0, 0],
    'Jawatan Kelab': ['', '', ''],
    'Peringkat Kelab': ['', '', ''],
    'Peringkat Pencapaian Kelab': ['', '', ''],
    'Pencapaian Kelab': ['', '', ''],
    'Nama Projek': ['', '', ''],
    'Jawatan Projek': ['', '', ''],
    'Peringkat Projek': ['', '', ''],
    'Ekstra Kokurikulum': [0, 0, 0]
}

# Constants
JAWATAN_KELAB = {
    'Pengerusi': 10,
    'Timbalan Pengerusi / Naib Pengerusi': 8,
    'Setiausaha / Bendahari': 7,
    'Penolong Setiausaha / Penolong Bendahari': 6,
    'Ahli Jawatankuasa': 5,
    'Ahli Aktif': 4
}

PERINGKAT_KELAB = {
    'Kebangsaan': 10,
    'Negeri': 8,
    'Daerah': 6,
    'Sekolah': 4
}

PENCAPAIAN = {
    'Johan': 0,
    'Naib Johan': -1,
    'Ketiga': -2
}

JAWATAN_PROJEK = {
    'Pengerusi Projek': 10,
    'Timbalan Pengerusi / Naib Pengerusi / Setiausaha Projek': 9,
    'Bendahari Projek': 8,
    'Penolong Setiausaha / Penolong Bendahari Projek': 7,
    'Ahli Jawatankuasa Projek': 6,
    'Ahli': 5
}

PERINGKAT_PROJEK = {
    'Negeri': 10,
    'Daerah': 8,
    'PTE/KTE': 6
}

EXTRA_KOKO = {
    '': 0,
}

# Logic
tab1, tab2, tab3 = st.tabs(['SUKAN/PERMAINAN', 'KELAB/PERSATUAN', 'BADAN BERUNIFORM'])

with tab1:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][0] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 0')
        user_data['Jawatan Kelab'][0] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 0')
        user_data['Peringkat Kelab'][0] = st.selectbox('Peringkat Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 0')
        user_data['Peringkat Pencapaian Kelab'][0] = st.selectbox('Peringkat Pencapaian Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Pencapaian Kelab 0')
        user_data['Pencapaian Kelab'][0] = st.selectbox('Pencapaian Kelab', options=PENCAPAIAN.keys(), key='Pencapaian Kelab 0')
    with col2:
        user_data['Nama Projek'][0] = st.text_input('Nama Projek', key='Nama Projek 0')
        user_data['Jawatan Projek'][0] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 0')
        user_data['Peringkat Projek'][0] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 0')
        user_data['Ekstra Kokurikulum'][0] = st.selectbox('Ekstra Kokurikulum', options=EXTRA_KOKO.keys(), key='Ekstra Kokurikulum 0')

with tab2:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][1] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 1')
        user_data['Jawatan Kelab'][1] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 1')
        user_data['Peringkat Kelab'][1] = st.selectbox('Peringkat Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 1')
        user_data['Peringkat Pencapaian Kelab'][1] = st.selectbox('Peringkat Pencapaian Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Pencapaian Kelab 1')
        user_data['Pencapaian Kelab'][1] = st.selectbox('Pencapaian Kelab', options=PENCAPAIAN.keys(), key='Pencapaian Kelab 1')
    with col2:
        user_data['Nama Projek'][1] = st.text_input('Nama Projek', key='Nama Projek 1')
        user_data['Jawatan Projek'][1] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 1')
        user_data['Peringkat Projek'][1] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 1')
        user_data['Ekstra Kokurikulum'][1] = st.selectbox('Ekstra Kokurikulum', options=EXTRA_KOKO.keys(), key='Ekstra Kokurikulum 1')

with tab3:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][2] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 2')
        user_data['Jawatan Kelab'][2] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 2')
        user_data['Peringkat Kelab'][2] = st.selectbox('Peringkat Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 2')
        user_data['Peringkat Pencapaian Kelab'][2] = st.selectbox('Peringkat Pencapaian Kelab', options=PERINGKAT_KELAB.keys(), key='Peringkat Pencapaian Kelab 2')
        user_data['Pencapaian Kelab'][2] = st.selectbox('Pencapaian Kelab', options=PENCAPAIAN.keys(), key='Pencapaian Kelab 2')
    with col2:
        user_data['Nama Projek'][2] = st.text_input('Nama Projek', key='Nama Projek 2')
        user_data['Jawatan Projek'][2] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 2')
        user_data['Peringkat Projek'][2] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 2')
        user_data['Ekstra Kokurikulum'][2] = st.selectbox('Ekstra Kokurikulum', options=EXTRA_KOKO.keys(), key='Ekstra Kokurikulum 2')

# Table Display

st.markdown('---')

st.html(f'''<table style="width: 100%;">
    <tr>
        <th style="border: 1px solid white">ELEMEN</th>
        <th style="border: 1px solid white">ASPEK</th>
        <th style="border: 1px solid white" colspan=2>SUKAN/PERMAINAN</th>
        <th style="border: 1px solid white" colspan=2>KELAB/PERSATUAN</th>
        <th style="border: 1px solid white" colspan=2>BADAN BERUNIFORM</th>
        <th style="border: 1px solid white">EKSTRA KURIKULUM</th>
    </tr>
    <tr>
        <td style="border: 1px solid white" rowspan=4>PENGLIBATAN</td>
        <td style="border: 1px solid white">Kehadiran</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][0]} / 20</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][0] / 20 * 50}</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][1]} / 20</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][1] / 20 * 50}</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][2]} / 20</td>
        <td style="border: 1px solid white">{user_data['Kehadiran Kelab'][2] / 20 * 50}</td>
        <td style="border: 1px solid white">Jawatan</td>
    </tr>
    <tr>
        <td style="border: 1px solid white">Jawatan</td>
        <td style="border: 1px solid white">{user_data['Jawatan Kelab'][0]}</td>
        <td style="border: 1px solid white">{JAWATAN_KELAB[user_data['Jawatan Kelab'][0]]}</td>
        <td style="border: 1px solid white">{user_data['Jawatan Kelab'][1]}</td>
        <td style="border: 1px solid white">{JAWATAN_KELAB[user_data['Jawatan Kelab'][1]]}</td>
        <td style="border: 1px solid white">{user_data['Jawatan Kelab'][2]}</td>
        <td style="border: 1px solid white">{JAWATAN_KELAB[user_data['Jawatan Kelab'][2]]}</td>
        <td style="border: 1px solid white" rowspan=3></td>
    </tr>
    <tr>
        <td style="border: 1px solid white">Peringkat</td>
        <td style="border: 1px solid white">{user_data['Peringkat Kelab'][0]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][0]]}</td>
        <td style="border: 1px solid white">{user_data['Peringkat Kelab'][1]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][1]]}</td>
        <td style="border: 1px solid white">{user_data['Peringkat Kelab'][2]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid white">Pencapaian</td>
        <td style="border: 1px solid white">{user_data['Peringkat Pencapaian Kelab'][0]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Pencapaian Kelab'][0]] + PENCAPAIAN[user_data["Pencapaian Kelab"][0]]}</td>
        <td style="border: 1px solid white">{user_data['Peringkat Pencapaian Kelab'][1]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Pencapaian Kelab'][1]] + PENCAPAIAN[user_data["Pencapaian Kelab"][1]]}</td>
        <td style="border: 1px solid white">{user_data['Peringkat Pencapaian Kelab'][2]}</td>
        <td style="border: 1px solid white">{PERINGKAT_KELAB[user_data['Peringkat Pencapaian Kelab'][2]] + PENCAPAIAN[user_data["Pencapaian Kelab"][2]]}</td>
    </tr>
</table>
''')