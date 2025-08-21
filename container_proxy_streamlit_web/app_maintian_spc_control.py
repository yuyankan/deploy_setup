import pandas as pd
import myquery_db as query_db
import streamlit as st
st.set_page_config(page_title='SPC_CONTROL SET UP', layout="wide")
st.page_link(page='pages/app_maintain_spc_control', label='SPC_CONTROL_SETUP')

tables={
    'meta_parameters':'ks_project_yyk.ods.spc_meta_test_parameters',
    'meta_spec':'ks_project_yyk.ods.meta_receipt_value'
}

def read_data():
    query = f'''
    select mp.*
    from {tables['meta_parameters']} mp
    --eft join {tables['meta_spec']} ms on ms.id=mp.receiptid

    '''
    df = query_db.query_ksdata(query=query)
    return df

