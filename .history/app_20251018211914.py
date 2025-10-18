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
    
    # Create simple architecture visualization
    fig = go.Figure()
    
    # Add boxes for each layer
    layers = ["Application Layer", "AURA Intelligence Layer", 
              "SanDisk Controller", "Physical Hardware"]
    y_positions = [0.8, 0.5, 0.2, 0]
    
    for i, layer in enumerate(layers):
        fig.add_shape(type="rect",
            x0=0.2, y0=y_positions[i]-0.08, x1=0.8, y1=y_positions[i]+0.08,
            line=dict(color="#E31E24", width=2),
            fillcolor="#003366" if i == 1 else "lightgray"
        )
        fig.add_annotation(x=0.5, y=y_positions[i],
            text=f"<b>{layer}</b>",
            showarrow=False,
            font=dict(size=14, color="white" if i == 1 else "black")
        )
    
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Key features
    st.subheader("✨ Key Capabilities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Module 1: Intelligent Data Manager**
        - Real-time AI classification
        - Variable compression (H.265, LZ4)
        - 70% write reduction
        
        **🏥 Module 2: Predictive Health Engine**
        - LSTM-based failure prediction
        - 89% accuracy (2-3 weeks early warning)
        - 35% lifespan extension
        """)
    
    with col2:
        st.markdown("""
        **🔐 Module 3: Distributed Security**
        - 5-shard encrypted distribution
        - Blockchain audit trail
        - Theft-proof data protection
        
        **🔋 Module 4: Adaptive Power Controller**
        - AI workload forecasting
        - Dynamic 4-level sleep states
        - 28% power reduction
        """)
def show_module1():
    st.header("🎯 Module 1: Intelligent Data Manager")
    st.write("Simulates real-time data classification and compression")
    
    # Simulation controls
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📹 Drone Flight Simulation")
        
        # Simulate video frames
        num_frames = st.slider("Number of frames to process:", 100, 1000, 500)
        
        if st.button("🚀 Start Classification", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate classification
            classifications = []
            data_sizes = []
            
            for i in range(num_frames):
                # Simulate AI classification (random for demo)
                rand = np.random.random()
                if rand < 0.15:  # 15% critical
                    class_type = "Critical"
                    size = 4.0  # MB (full quality)
                elif rand < 0.25:  # 10% important
                    class_type = "Important"
                    size = 2.0  # MB (standard)
                elif rand < 0.45:  # 20% normal
                    class_type = "Normal"
                    size = 0.5  # MB (compressed)
                else:  # 55% discard
                    class_type = "Discard"
                    size = 0.0  # MB (deleted)
                
                classifications.append(class_type)
                data_sizes.append(size)
                
                # Update progress
                progress_bar.progress((i + 1) / num_frames)
                status_text.text(f"Processing frame {i+1}/{num_frames} - {class_type}")
                time.sleep(0.01)  # Small delay for visualization
            
            # Results
            st.success("✅ Classification Complete!")
            
            # Calculate metrics
            total_raw = num_frames * 4.0  # Assuming 4MB per frame
            total_stored = sum(data_sizes)
            reduction = ((total_raw - total_stored) / total_raw) * 100
            
            # Display results
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Raw Data", f"{total_raw/1000:.1f} GB")
            col_b.metric("Stored Data", f"{total_stored/1000:.1f} GB", 
                        f"-{reduction:.0f}%", delta_color="inverse")
            col_c.metric("Lifespan Extension", f"{100/(100-reduction):.1f}x", 
                        delta_color="normal")
            
            # Classification breakdown
            st.subheader("📊 Classification Breakdown")
            
            df = pd.DataFrame({
                'Classification': classifications
            })
            
            class_counts = df['Classification'].value_counts()
            
            fig = px.pie(values=class_counts.values, 
                        names=class_counts.index,
                        color=class_counts.index,
                        color_discrete_map={
                            'Critical': '#E31E24',
                            'Important': '#FF6B6B',
                            'Normal': '#4ECDC4',
                            'Discard': '#95A5A6'
                        })
            
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400)
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📋 Classification Rules")
        st.markdown("""
        **CRITICAL** 🔴
        - Person detected
        - Anomaly/accident
        - GPS waypoints
        - Full 4K quality
        
        **IMPORTANT** 🟠
        - Vehicle detected
        - Activity present
        - Standard quality
        
        **NORMAL** 🟢
        - Routine flight
        - Background scenery
        - H.265 compressed
        
        **DISCARD** ⚪
        - Empty frames
        - Duplicates
        - Not stored
        """)
def show_module2():
    st.header("🏥 Module 2: Predictive Health Engine")
    st.write("LSTM-based block failure prediction system")
    
    # Simulation parameters
    st.subheader("⚙️ Block Health Simulation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_blocks = st.slider("Number of blocks to monitor:", 10, 100, 50)
        simulation_days = st.slider("Simulation period (days):", 30, 180, 90)
    
    with col2:
        pe_cycle_limit = st.number_input("P/E Cycle Limit:", 3000, 10000, 5000, step=1000)
        failure_threshold = st.slider("Failure prediction threshold:", 70, 95, 85)
    
    if st.button("🔍 Run Health Analysis", type="primary"):
        with st.spinner("Analyzing block health patterns..."):
            time.sleep(2)  # Simulate processing
            
            # Generate synthetic block health data
            days = np.arange(0, simulation_days)
            
            # Simulate different block health trajectories
            blocks_data = []
            failing_blocks = []
            
            for block_id in range(num_blocks):
                # Random starting cycle count
                start_cycles = np.random.randint(pe_cycle_limit * 0.3, pe_cycle_limit * 0.9)
                
                # Simulate degradation (some blocks degrade faster)
                degradation_rate = np.random.uniform(5, 30)
                cycles = start_cycles + (days * degradation_rate)
                
                # Add some noise
                cycles += np.random.normal(0, 50, len(days))
                
                # Health percentage
                health = 100 * (1 - cycles / pe_cycle_limit)
                health = np.clip(health, 0, 100)
                
                blocks_data.append({
                    'block_id': block_id,
                    'cycles': cycles[-1],
                    'health': health[-1],
                    'trajectory': health
                })
                
                # Check if failing
                if health[-1] < (100 - failure_threshold):
                    failing_blocks.append(block_id)
            
            # Display summary metrics
            st.success("✅ Analysis Complete!")
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Healthy Blocks", num_blocks - len(failing_blocks), 
                        f"{((num_blocks - len(failing_blocks))/num_blocks*100):.0f}%")
            col_b.metric("Predicted Failures", len(failing_blocks), 
                        delta_color="inverse")
            col_c.metric("Avg Health", f"{np.mean([b['health'] for b in blocks_data]):.0f}%")
            
            # Plot block health over time
            st.subheader("📈 Block Health Trajectories")
            
            fig = go.Figure()
            
            for block in blocks_data:
                color = '#E31E24' if block['block_id'] in failing_blocks else '#4ECDC4'
                fig.add_trace(go.Scatter(
                    x=days,
                    y=block['trajectory'],
                    mode='lines',
                    name=f"Block {block['block_id']}",
                    line=dict(color=color, width=1),
                    showlegend=False
                ))
            
            # Add failure threshold line
            fig.add_hline(y=100-failure_threshold, line_dash="dash", 
                         line_color="red", annotation_text="Failure Threshold")
            
            fig.update_layout(
                title="Block Health Over Time",
                xaxis_title="Days",
                yaxis_title="Health (%)",
                height=400,
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Failing blocks table
            if len(failing_blocks) > 0:
                st.subheader("⚠️ Blocks Requiring Attention")
                
                failing_data = [b for b in blocks_data if b['block_id'] in failing_blocks]
                df_failing = pd.DataFrame(failing_data)[['block_id', 'cycles', 'health']]
                df_failing['health'] = df_failing['health'].round(1)
                df_failing['cycles'] = df_failing['cycles'].astype(int)
                df_failing.columns = ['Block ID', 'P/E Cycles', 'Health (%)']
                
                st.dataframe(df_failing, use_container_width=True)
                
                st.info(f"💡 **Recommendation:** Migrate data from {len(failing_blocks)} blocks within 14-21 days to prevent failure.")
def show_module4():
    st.header("🔋 Module 4: Adaptive Power Controller")
    st.write("AI-driven power optimization for edge devices")
    
    # Device selection
    device_type = st.selectbox("Select Device Type:", 
                               ["Drone", "IoT Sensor", "Trail Camera", "Surveillance Camera"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        battery_capacity = st.slider("Battery Capacity (Wh):", 10, 100, 50)
    
    with col2:
        simulation_hours = st.slider("Simulation Duration (hours):", 12, 48, 24)
    
    if st.button("⚡ Run Power Simulation", type="primary"):
        with st.spinner("Simulating power consumption..."):
            time.sleep(1.5)
            
            # Generate 24-hour power profile
            hours = np.arange(0, simulation_hours, 0.25)  # 15-minute intervals
            
            # Traditional (always-on) power consumption
            traditional_power = np.ones(len(hours)) * 3.2  # 3.2W constant
            
            # AURA-optimized power consumption
            aura_power = []
            states = []
            
            for hour in hours:
                hour_of_day = hour % 24
                
                # Define usage patterns based on device type
                if device_type == "Drone":
                    if 9 <= hour_of_day < 17:  # Active during business hours
                        power = 2.3  # Active (AURA-optimized)
                        state = "Active"
                    elif 8 <= hour_of_day < 9 or 17 <= hour_of_day < 18:
                        power = 1.2  # Idle
                        state = "Idle"
                    elif 18 <= hour_of_day < 22:
                        power = 2.4  # Charging + GC
                        state = "Charging"
                    else:
                        power = 0.1  # Deep sleep
                        state = "Deep Sleep"
                
                elif device_type == "IoT Sensor":
                    if hour_of_day % 1 == 0:  # Hourly readings
                        power = 2.0
                        state = "Active"
                    else:
                        power = 0.1
                        state = "Deep Sleep"
                
                elif device_type == "Trail Camera":
                    if 6 <= hour_of_day < 20:  # Daylight hours
                        power = 2.3
                        state = "Active"
                    else:
                        power = 0.1
                        state = "Deep Sleep"
                
                else:  # Surveillance Camera
                    power = 2.3  # Always active
                    state = "Active"
                
                aura_power.append(power + np.random.uniform(-0.1, 0.1))
                states.append(state)
            
            aura_power = np.array(aura_power)
            
            # Calculate energy consumption
            traditional_energy = np.trapz(traditional_power, dx=0.25)
            aura_energy = np.trapz(aura_power, dx=0.25)
            savings = ((traditional_energy - aura_energy) / traditional_energy) * 100
            
            # Calculate runtime
            traditional_runtime = battery_capacity / 3.2
            aura_runtime = battery_capacity / np.mean(aura_power)
            
            # Display metrics
            st.success("✅ Simulation Complete!")
            
            col_a, col_b, col_c, col_d = st.columns(4)
            col_a.metric("Traditional Power", f"{np.mean(traditional_power):.1f}W")
            col_b.metric("AURA Power", f"{np.mean(aura_power):.1f}W", 
                        f"-{savings:.0f}%", delta_color="inverse")
            col_c.metric("Runtime Increase", f"+{((aura_runtime/traditional_runtime-1)*100):.0f}%", 
                        delta_color="normal")
            col_d.metric("Battery Life", f"{aura_runtime:.1f}h", 
                        delta_color="normal")
            
            # Power consumption graph
            st.subheader("📊 Power Consumption Over Time")
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=hours,
                y=traditional_power,
                mode='lines',
                name='Traditional (Always-On)',
                line=dict(color='#95A5A6', width=2, dash='dash')
            ))
            
            fig.add_trace(go.Scatter(
                x=hours,
                y=aura_power,
                mode='lines',
                name='AURA-Optimized',
                line=dict(color='#E31E24', width=3),
                fill='tonexty',
                fillcolor='rgba(227, 30, 36, 0.1)'
            ))
            
            fig.update_layout(
                title=f"{device_type} - {simulation_hours}-Hour Power Profile",
                xaxis_title="Time (hours)",
                yaxis_title="Power Consumption (W)",
                height=400,
                hovermode='x unified',
                legend=dict(x=0.7, y=0.98)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # State breakdown
            st.subheader("🔄 Power State Distribution")
            
            state_counts = pd.Series(states).value_counts()
            
            fig2 = px.bar(x=state_counts.index, y=state_counts.values,
                         color=state_counts.index,
                         color_discrete_map={
                             'Active': '#E31E24',
                             'Idle': '#FF6B6B',
                             'Charging': '#4ECDC4',
                             'Deep Sleep': '#003366'
                         },
                         labels={'x': 'Power State', 'y': 'Time Periods'})
            
            fig2.update_layout(showlegend=False, height=300)
            
            st.plotly_chart(fig2, use_container_width=True)
            
            # Savings summary
            st.info(f"""
            💡 **AURA Impact for {device_type}:**
            - Power savings: {savings:.0f}%
            - Extended runtime: {aura_runtime - traditional_runtime:.1f} hours
            - Annual energy saved: {(traditional_energy - aura_energy) * 365:.0f} Wh
            - CO₂ reduction: {((traditional_energy - aura_energy) * 365 * 0.5)/1000:.1f} kg/year
            """)
