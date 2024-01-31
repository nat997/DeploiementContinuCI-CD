import streamlit as st
from . import streamlit as main # Import your Streamlit app's main function

def test_streamlit_app():
    # Create a Streamlit testing context
    with st.beta_container():
        # Call your Streamlit app's main function
        main()

        # You can use Streamlit's st functions to interact with your app and make assertions
        # For example, you can check if a specific title is displayed
        assert st.title("Degree vs Timestamp Chart") is not None

        # You can also check if a plot is displayed
        assert st.pyplot() is not None
