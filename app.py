import streamlit as st
import welcome
import students
import startup
import ceo
import trends
from PIL import Image

def main():
    # Create a sidebar with panel options
    st.sidebar.header("Team: NULL-BYTE ")
    st.sidebar.write("-" * 10)
    st.sidebar.subheader("Kindly choose a functionality from the list of Lumina's offerings ")

    # Load the image
    image = Image.open(r'a13.png')

    # Display the image
    st.image(image, use_column_width=True)

    # Define the options as a list of strings
    panel_options = ["Homepage", "Student Page", "Startup Aspirant / Investors", "CEO / Entrepreneurs / Owners","Trends Tracker"]

    # Use st.selectbox to create a dropdown with the list of options
    sidebar_selection = st.sidebar.selectbox("Select Functionality", panel_options)

    # Check which panel is selected and call the corresponding main function
    if sidebar_selection == "Homepage":
        welcome.main()
    elif sidebar_selection == "Student Page":
        students.main()
    elif sidebar_selection == "Startup Aspirant / Investors":
        startup.main()
    elif sidebar_selection == "CEO / Entrepreneurs / Owners":
        ceo.main()
    elif sidebar_selection == "Trends Tracker":
        trends.main()

if __name__ == "__main__":
    main()
