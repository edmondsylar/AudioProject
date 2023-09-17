import streamlit as st
import streamlit_extras as ste

st.title("configuration")


def Main():
    # set the main tabs
    main, configs = st.tabs(["Home Page", "Configurations"])
    
    with main:
        st.markdown(f"""
        ##### Running Configutation.   
        **Replicate KEY**: {st.session_state['replicate_key']} 
        
        """)

    
    with configs:
        st.subheader("Configurations")


Main()