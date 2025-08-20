import pandas as pd
import myquery_db as query_db
import streamlit as st
st.set_page_config(page_title='SPC_ANALYZE_PLATFORM', layout="wide")
#st.header('PROCESS CONTROL SETUP/MAITIAN')
header_text = 'SPC_ANALYZE_PLATFORM'

#st.header('SPC_CONTROL_SETUP')
st.markdown("<div style='text-align: center;'>"
                f"<span style='color:#00008B; font-weight:bold;font-size:50px'>{header_text}"
                "</span>"
            "</div>", 
        unsafe_allow_html=True
        )


   


st.page_link("app_spc.py", label="Home", icon="🏠")
st.page_link(page='./pages/app_maintain_spc_control.py', label='SPC_CONTROL_SETUP',icon="1️⃣" )
st.page_link(page='./pages/app_maintain_spec.py', label='SPEC_MAINTIAN',icon="2️⃣" )

