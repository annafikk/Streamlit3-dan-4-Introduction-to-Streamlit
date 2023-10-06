def status_widget():
    import streamlit as st
    import time

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    
    def click_button():
        st.session_state.clicked = True
    
    st.button('Mulai Demo', on_click=click_button)

    if st.session_state.clicked:
        with st.status("Downloading data..."):
            st.write("Searching for data...")
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)

        st.button('Rerun')