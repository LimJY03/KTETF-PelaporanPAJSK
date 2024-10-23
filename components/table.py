import streamlit as st
from components.constants import (
    JAWATAN_KELAB,
    PERINGKAT_KELAB,
    PENCAPAIAN_KELAB,
    JAWATAN_PROJEK,
    PERINGKAT_PROJEK,
    EXTRA_KOKO_PERKHIDMATAN,
    EXTRA_KOKO_ANUGERAH,
)

def show_table(data):

    def get_total(type):

        return (data[f'{type}_kehadiran'] / 20 * 50 + 
            JAWATAN_KELAB[data[f'{type}_jawatan']] +
            PERINGKAT_KELAB[data[f'{type}_peringkat']] +
            PENCAPAIAN_KELAB[data[f'{type}_pencapaian']] + 
            JAWATAN_PROJEK[data[f'{type}_jawatan_p']] + 
            PERINGKAT_PROJEK[data[f'{type}_peringkat_p']])

    st.html(f'''<table style="width: 100%;">
        <tr>
            <th style="border: 1px solid grey; padding: 10px;">ELEMEN</th>
            <th style="border: 1px solid grey; padding: 10px;">ASPEK</th>
            <th style="border: 1px solid grey; padding: 10px;" colspan=2>SUKAN/PERMAINAN</th>
            <th style="border: 1px solid grey; padding: 10px;" colspan=2>KELAB/PERSATUAN</th>
            <th style="border: 1px solid grey; padding: 10px;" colspan=2>BADAN BERUNIFORM</th>
            <th style="border: 1px solid grey; padding: 10px;">EKSTRA KURIKULUM</th>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;" rowspan=4>PENGLIBATAN</td>
            <td style="border: 1px solid grey; padding: 10px;">Kehadiran</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_kehadiran']} / 20</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_kehadiran'] / 20 * 50}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_kehadiran']} / 20</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_kehadiran'] / 20 * 50}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_kehadiran']} / 20</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_kehadiran'] / 20 * 50}</td>
            <td style="border: 1px solid grey; padding: 10px;" rowspan=4>{data['ek_perkhidmatan']}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;">Jawatan</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_jawatan']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[data['s_jawatan']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_jawatan']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[data['p_jawatan']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_jawatan']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[data['b_jawatan']]}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;">Peringkat</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_peringkat']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[data['s_peringkat']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_peringkat']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[data['p_peringkat']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_peringkat']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[data['b_peringkat']]}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;">Pencapaian</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_pencapaian']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[data['s_pencapaian']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_pencapaian']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[data['p_pencapaian']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_pencapaian']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[data['b_pencapaian']]}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;" rowspan=3>PENGURUSAN PROJEK</td>
            <td style="border: 1px solid grey; padding: 10px;">Nama Projek</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{data['s_nama_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{data['p_nama_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{data['b_nama_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;" rowspan=3>{data['ek_anugerah']}</td>
        </tr>    
        <tr>
            <td style="border: 1px solid grey; padding: 10px;">Jawatan</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_jawatan_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[data['s_jawatan_p']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_jawatan_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[data['p_jawatan_p']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_jawatan_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[data['b_jawatan_p']]}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;">Peringkat</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['s_peringkat_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[data['s_peringkat_p']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['p_peringkat_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[data['p_peringkat_p']]}</td>
            <td style="border: 1px solid grey; padding: 10px;">{data['b_peringkat_p']}</td>
            <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[data['b_peringkat_p']]}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>SKOR</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total('s')}</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total('p')}</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total('b')}</td>
            <td style="border: 1px solid grey; padding: 10px;">{max(
                EXTRA_KOKO_PERKHIDMATAN[data['ek_perkhidmatan']],
                EXTRA_KOKO_ANUGERAH[data['ek_anugerah']],
            )}</td>
        </tr>
        <tr>
            <td style="border: 1px solid grey; padding: 10px;" colspan=2>JUMLAH SKOR (%)</td>
            <td style="border: 1px solid grey; padding: 10px;" colspan=7>{sum(
                sorted([get_total('s'), get_total('p'), get_total('b')], reverse=True)[:2]
            ) / 2 + max(
                EXTRA_KOKO_PERKHIDMATAN[data['ek_perkhidmatan']],
                EXTRA_KOKO_ANUGERAH[data['ek_anugerah']],
            )}</td>
        </tr>
    </table>
    ''')