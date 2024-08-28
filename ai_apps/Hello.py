import streamlit as st

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="SmartLog Solutions",  # Set your desired page title
    page_icon="💡",  # Set your desired favicon using emoji or a URL to an image
)


# Display the banner image
st.image('background.jpg', width=700)  # Adjust the width as necessary

# Main title of the application with emojis and paragraph
st.markdown("<h1 class='title'>💡 SmartLog Solutions 💡</h1>", unsafe_allow_html=True)
st.markdown(
    """
    Analyze logs and errors with ease using our powerful AI tools. 
    Our platform provides comprehensive analysis capabilities to help you gain insights and optimize your workflows.
    """
)

# Main function to structure the page
def main() -> None:
    st.markdown("---")  # Separator for visual appeal
    st.markdown("### Select an AI App from the sidebar to get started.")  # Instruction or headline for the sidebar

    # Beautified table
    st.markdown(
        """
        <table>
          <tr>
            <th>App Name</th>
            <th>Description</th>
          </tr>
          <tr>
            <td>Search Log Exceptions</td>
            <td>Search and analyze log exceptions, and their possible remedial actions</td>
          </tr>
          <tr>
            <td>RAG Research for Errors</td>
            <td>Research and analyze errors with RAG</td>
          </tr>
          <tr>
            <td>Analyzing Dashboards</td>
            <td>Analyze and optimize dashboard performance</td>
          </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

# Execute the main function to run the app
main()



