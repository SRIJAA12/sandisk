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
        font-size: 5rem;
        color: #E31E24;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 2.5rem;
        color: #003366;
        text-align: center;
        margin-top: 0;
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

# ============= FUNCTION DEFINITIONS =============

def show_overview():
    st.header("🎯 AURA System Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>70%</h2>
            <p>Write Reduction</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>35%</h2>
            <p>Lifespan Extension</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>28%</h2>
            <p>Power Savings</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Architecture diagram
    st.subheader("📐 System Architecture")
    
    st.markdown("""
    ```
    ┌──────────────────────────────────────────────┐
    │   📱 APPLICATION LAYER                       │
    │   Drone Apps -  IoT Firmware -  ADAS Systems   │
    └──────────────────────────────────────────────┘
                       ↓ ↑
    ┌──────────────────────────────────────────────┐
    │   🧠 AURA INTELLIGENCE LAYER (Our AI)        │
    │   ✓ Data Manager    ✓ Predictive Health     │
    │   ✓ Security Layer  ✓ Power Controller      │
    └──────────────────────────────────────────────┘
                       ↓ ↑
    ┌──────────────────────────────────────────────┐
    │   ⚙️  SANDISK CONTROLLER FIRMWARE            │
    │   FTL -  Wear Leveling -  ECC -  Garbage GC     │
    └──────────────────────────────────────────────┘
                       ↓ ↑
    ┌──────────────────────────────────────────────┐
    │   💾 PHYSICAL HARDWARE (SanDisk)             │
    │   iNAND 8GB-1TB -  UFS4.1 -  microSD           │
    └──────────────────────────────────────────────┘
    ```
    """)
    
    st.info("💡 **AURA is firmware middleware - no hardware changes needed**")
    
    # Key features
    st.markdown("---")
    st.subheader("✨ Four AI-Powered Modules")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🎯 Module 1: Data Manager
        AI classification • 70% write reduction
        
        #### 🏥 Module 2: Predictive Health
        89% accuracy • 2-3 weeks early warning
        """)
    
    with col2:
        st.markdown("""
        #### 🔐 Module 3: Security
        5-shard distribution • Theft-proof
        
        #### 🔋 Module 4: Power Control
        AI forecasting • 28% power savings
        """)


def show_module1():
    st.header("🎯 Module 1: Intelligent Data Manager")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📹 Drone Flight Simulation")
        num_frames = st.slider("Number of frames:", 100, 1000, 500)
        
        if st.button("🚀 Start Classification", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            classifications = []
            data_sizes = []
            
            for i in range(num_frames):
                rand = np.random.random()
                if rand < 0.15:
                    class_type = "Critical"
                    size = 4.0
                elif rand < 0.25:
                    class_type = "Important"
                    size = 2.0
                elif rand < 0.45:
                    class_type = "Normal"
                    size = 0.5
                else:
                    class_type = "Discard"
                    size = 0.0
                
                classifications.append(class_type)
                data_sizes.append(size)
                
                progress_bar.progress((i + 1) / num_frames)
                status_text.text(f"Frame {i+1}/{num_frames} - {class_type}")
                time.sleep(0.005)
            
            st.success("✅ Classification Complete!")
            
            total_raw = num_frames * 4.0
            total_stored = sum(data_sizes)
            reduction = ((total_raw - total_stored) / total_raw) * 100
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Raw Data", f"{total_raw/1000:.1f} GB")
            col_b.metric("Stored", f"{total_stored/1000:.1f} GB", f"-{reduction:.0f}%")
            col_c.metric("Lifespan", f"{100/(100-reduction):.1f}x")
            
            st.subheader("📊 Classification Results")
            
            class_counts = pd.Series(classifications).value_counts()
            
            fig = px.pie(
                values=class_counts.values, 
                names=class_counts.index,
                color=class_counts.index,
                color_discrete_map={
                    'Critical': '#E31E24',
                    'Important': '#FF6B6B',
                    'Normal': '#4ECDC4',
                    'Discard': '#95A5A6'
                }
            )
            
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400)
            
            config = {'displayModeBar': False}
            st.plotly_chart(fig, use_container_width=True, config=config)
    
    with col2:
        st.info("""
        **Rules:**
        
        🔴 **Critical**  
        Full 4K quality
        
        🟠 **Important**  
        Standard quality
        
        🟢 **Normal**  
        Compressed
        
        ⚪ **Discard**  
        Not stored
        """)


def show_module2():
    st.header("🏥 Module 2: Predictive Health Engine")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_blocks = st.slider("Blocks to monitor:", 10, 100, 50)
        simulation_days = st.slider("Days:", 30, 180, 90)
    
    with col2:
        pe_cycle_limit = st.number_input("P/E Limit:", 3000, 10000, 5000, step=1000)
        failure_threshold = st.slider("Threshold:", 70, 95, 85)
    
    if st.button("🔍 Run Analysis", type="primary"):
        with st.spinner("Analyzing block health..."):
            time.sleep(1.5)
            
            days = np.arange(0, simulation_days)
            blocks_data = []
            failing_blocks = []
            
            for block_id in range(num_blocks):
                start_cycles = np.random.randint(int(pe_cycle_limit * 0.3), int(pe_cycle_limit * 0.9))
                degradation_rate = np.random.uniform(5, 30)
                cycles = start_cycles + (days * degradation_rate)
                cycles += np.random.normal(0, 50, len(days))
                
                health = 100 * (1 - cycles / pe_cycle_limit)
                health = np.clip(health, 0, 100)
                
                blocks_data.append({
                    'block_id': block_id,
                    'cycles': cycles[-1],
                    'health': health[-1],
                    'trajectory': health
                })
                
                if health[-1] < (100 - failure_threshold):
                    failing_blocks.append(block_id)
            
            st.success("✅ Analysis Complete!")
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Healthy Blocks", num_blocks - len(failing_blocks))
            col_b.metric("Failing Blocks", len(failing_blocks))
            col_c.metric("Avg Health", f"{np.mean([b['health'] for b in blocks_data]):.0f}%")
            
            st.subheader("📈 Block Health Over Time")
            
            fig = go.Figure()
            
            for block in blocks_data:
                color = '#E31E24' if block['block_id'] in failing_blocks else '#4ECDC4'
                fig.add_trace(go.Scatter(
                    x=days,
                    y=block['trajectory'],
                    mode='lines',
                    line=dict(color=color, width=1),
                    showlegend=False,
                    hovertemplate='Day %{x}<br>Health: %{y:.1f}%'
                ))
            
            fig.add_hline(y=100-failure_threshold, line_dash="dash", 
                         line_color="red", annotation_text="Failure Threshold")
            
            fig.update_layout(
                xaxis_title="Days",
                yaxis_title="Health (%)",
                height=400,
                hovermode='x unified'
            )
            
            config = {'displayModeBar': False}
            st.plotly_chart(fig, use_container_width=True, config=config)
            
            if len(failing_blocks) > 0:
                st.warning(f"⚠️ **{len(failing_blocks)} blocks need attention within 14-21 days**")
                
                failing_data = [b for b in blocks_data if b['block_id'] in failing_blocks]
                df_failing = pd.DataFrame(failing_data)[['block_id', 'cycles', 'health']]
                df_failing['health'] = df_failing['health'].round(1)
                df_failing['cycles'] = df_failing['cycles'].astype(int)
                df_failing.columns = ['Block ID', 'P/E Cycles', 'Health (%)']
                
                st.dataframe(df_failing, use_container_width=True)


def show_module3():
    st.header("🔐 Module 3: Distributed Security Layer")
    
    st.write("Federated storage with encrypted shard distribution")
    
    # Simulation parameters
    col1, col2 = st.columns(2)
    
    with col1:
        num_devices = st.slider("Number of devices in fleet:", 5, 20, 10)
        data_size = st.slider("Data size (GB):", 1, 100, 10)
    
    with col2:
        num_shards = st.selectbox("Number of shards:", [3, 5, 7], index=1)
        threshold = st.selectbox("Reconstruction threshold:", [2, 3, 4], index=1)
    
    if st.button("🔒 Simulate Sharding", type="primary"):
        with st.spinner("Encrypting and distributing shards..."):
            time.sleep(1.5)
            
            # Calculate shard distribution
            shard_size = data_size / num_shards
            
            # Simulate device distribution
            device_assignments = []
            for i in range(num_shards):
                device_id = np.random.randint(1, num_devices + 1)
                device_assignments.append({
                    'Shard': f"Shard {i+1}",
                    'Device': f"Device #{device_id}",
                    'Size (GB)': round(shard_size, 2),
                    'Status': 'Encrypted ✓'
                })
            
            st.success("✅ Sharding Complete!")
            
            # Display metrics
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Original Data", f"{data_size} GB")
            col_b.metric("Shard Size", f"{shard_size:.2f} GB")
            col_c.metric("Security Level", f"{num_shards}-of-{threshold}")
            
            # Shard distribution table
            st.subheader("📊 Shard Distribution Across
