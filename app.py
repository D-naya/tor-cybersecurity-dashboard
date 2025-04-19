import os
import streamlit as st
from utils.auth import login, check_role
from utils.threats import generate_fake_threats
from utils.visualization import plot_threats, plot_sample_bar_chart

# Set up the page - MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="TOR Cybersecurity Dashboard", layout="wide")

def load_css():
    css_path = os.path.join("assets", "styles.css")
    try:
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file not found. Using default styles.")

def load_logo():
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.sidebar.image(
            logo_path,
            use_container_width=True,  # Updated parameter
            output_format="PNG"  # Ensures proper rendering
        )
    else:
        st.sidebar.markdown("""
        <div style="text-align:center; padding:10px; border:1px dashed #4CC9F0; border-radius:5px;">
            <h4>TOR Cybersecurity</h4>
        </div>
        """, unsafe_allow_html=True)

# Load assets
load_css()
load_logo()


# User authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None  # Initialize username in session state

# Login section
if not st.session_state.logged_in:
    st.title("Login to TOR Cybersecurity Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username  # Store username in session state
            st.success("Logged in successfully!")
            st.rerun()  # Refresh to show dashboard
        else:
            st.error("Invalid credentials.")
else:
    # Retrieve the username from session state
    username = st.session_state.username
    role = check_role(username)
    st.title(f"Welcome to the TOR Cybersecurity Dashboard - {role}")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Threat Overview", "Sample Bar Chart", "Logout"])

    if page == "Threat Overview":
        # Real-time threat monitoring
        threats = generate_fake_threats()
        st.subheader("Current Threats")
        st.dataframe(threats)

        # Visualize threats
        st.subheader("Threat Visualization")
        plot_threats(threats)

        # Action buttons
        st.subheader("Actions")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Block IP"):
                st.success("IP Blocked!")
        with col2:
            if st.button("Isolate Device"):
                st.success("Device Isolated!")
        with col3:
            if st.button("Escalate to SOC"):
                st.success("Escalated to SOC!")

    elif page == "Sample Bar Chart":
        # Show Sample Bar Chart
        plot_sample_bar_chart()

    elif page == "Logout":
        if st.button("Confirm Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.success("Logged out successfully!")
            st.rerun()