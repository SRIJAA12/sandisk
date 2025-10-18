import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import time

# Page config
st.set_page_config(
    page_title="AURA - AI Storage Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for SanDisk branding
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #E31E24;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #003366;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #E31E24 0%, #003366 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🧠 AURA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Adaptive Unified Resource Architecture for Edge Storage</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.image("https://via.placeholder.com/300x100/E31E24/FFFFFF?text=SanDisk+AURA", use_container_width=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Module Demo:", 
                         ["Overview", 
                          "Module 1: Data Manager", 
                          "Module 2: Predictive Health",
                          "Module 4: Power Controller"])

st.sidebar.markdown("---")
st.sidebar.info("""
**Team AURA**  
PSG Institute of Technology  
Cerebrum 2025 Competition
""")

# Main content based on selection
if page == "Overview":
    show_overview()
elif page == "Module 1: Data Manager":
    show_module1()
elif page == "Module 2: Predictive Health":
    show_module2()
elif page == "Module 4: Power Controller":
    show_module4()
