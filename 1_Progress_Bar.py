def progress_bar():
    import streamlit as st
    import time

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    
    def click_button():
        st.session_state.clicked = True
    
    st.button('Mulai Demo', on_click=click_button)

    if st.session_state.clicked:
        'Starting a long computation ...'
    
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i+1)
            time.sleep(0.02)
        
        '... and now we\'re done!'