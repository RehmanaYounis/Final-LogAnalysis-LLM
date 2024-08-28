import nest_asyncio
import streamlit as st

# Apply necessary asyncio patches for Streamlit
nest_asyncio.apply()

# Configuration for the Streamlit web page
st.set_page_config(
    page_title="Log AI Analyzer",  # Set your desired page title
    page_icon=":orange_heart:",  # Set your desired favicon using emoji or a URL to an image
)

# Inject custom CSS for sidebar color and table styling
st.markdown(
    """
    <style>
    /* Target the sidebar directly with its internal Streamlit structure */
    div[data-testid="stSidebar"] {
        background-color: #007BFF;  /* Your desired blue color */
        color: #ffffff;  /* Ensuring text is white for better readability */
    }
    /* Adjust link colors in the sidebar */
    div[data-testid="stSidebar"] a {
        color: #ffffff;
    }
    /* Adjust button colors in the sidebar */
    div[data-testid="stSidebar"] .stButton > button {
        color: #ffffff;
        background-color: #0056b3;  /* Darker blue for buttons */
    }
    /* Adjust main title */
    .title {
        font-size: 3em;
        text-align: center;
        padding-bottom: 20px;
        animation: glow 2s linear infinite alternate;
        text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
    }
    /* Animation for glowing effect */
    @keyframes glow {
        from {
            text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
        }
        to {
            text-shadow: 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3, 0 0 200px #0056b3, 0 0 300px #0056b3;
        }
    }
    /* Beautify table */
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 20px;
    }
    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
        color: #333;
    }
    tr:hover {
        background-color: #f5f5f5;
        border: 3px solid #ccc; /* Light gray border color */
    }
    tr:hover td {
        color: #000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the banner image
st.image('background.jpg', width=500)  # Adjust the width as necessary

# Main title of the application with emojis and paragraph
st.markdown("<h1 class='title'>💡 Log AI Analyzer 💡</h1>", unsafe_allow_html=True)
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
            <td>Search and analyze log exceptions</td>
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














# import nest_asyncio
# import streamlit as st

# # Apply necessary asyncio patches for Streamlit
# nest_asyncio.apply()

# # Configuration for the Streamlit web page
# st.set_page_config(
#     page_title="Log AI Analyzer",  # Set your desired page title
#     page_icon=":orange_heart:",  # Set your desired favicon using emoji or a URL to an image
# )

# # Inject custom CSS for sidebar color
# st.markdown(
#     """
#     <style>
#     /* Target the sidebar directly with its internal Streamlit structure */
#     div[data-testid="stSidebar"] {
#         background-color: #007BFF;  /* Your desired blue color */
#         color: #ffffff;  /* Ensuring text is white for better readability */
#     }
#     /* Adjust link colors in the sidebar */
#     div[data-testid="stSidebar"] a {
#         color: #ffffff;
#     }
#     /* Adjust button colors in the sidebar */
#     div[data-testid="stSidebar"] .stButton > button {
#         color: #ffffff;
#         background-color: #0056b3;  /* Darker blue for buttons */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Main title of the application
# st.title("Log AI Analyzer")  # Change the title as required

# # Main function to structure the page
# def main() -> None:
#     st.markdown("---")  # Separator for visual appeal
#     st.markdown("### Select an AI App from the sidebar:")  # Instruction or headline for the sidebar
#     # Descriptions for each app or function in the sidebar
#     st.markdown("#### 1. Searching Log Exceptions")  # Describe the first app
#     st.markdown("#### 2. RAG Research for Errors")  # Describe the second app
#     st.markdown("#### 3. Analyzing Dashboards")  # Describe the third app

#     # Sidebar interface for user selection
#     st.sidebar.success("Select App from above")  # Prompt or call to action in the sidebar

# # Execute the main function to run the app
# main()
