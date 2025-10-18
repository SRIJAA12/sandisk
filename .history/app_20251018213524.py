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
    
    # Architecture diagram - FIXED VERSION
    st.subheader("📐 System Architecture")
    
    # Create architecture diagram with proper data structure
    fig = go.Figure()
    
    # Define layers
    layers = [
        {"name": "Application Layer", "y": 0.85, "color": "#95A5A6"},
        {"name": "AURA Intelligence Layer", "y": 0.55, "color": "#E31E24"},
        {"name": "SanDisk Controller", "y": 0.25, "color": "#003366"},
        {"name": "Physical Hardware", "y": 0.05, "color": "#2C3E50"}
    ]
    
    for layer in layers:
        # Add rectangle
        fig.add_shape(
            type="rect",
            x0=0.1, y0=layer["y"]-0.12,
            x1=0.9, y1=layer["y"]+0.12,
            line=dict(color="white", width=2),
            fillcolor=layer["color"]
        )
        
        # Add text
        fig.add_annotation(
            x=0.5, y=layer["y"],
            text=f"<b>{layer['name']}</b>",
            showarrow=False,
            font=dict(size=16, color="white")
        )
    
    # Add arrows between layers
    arrow_positions = [0.73, 0.43, 0.13]
    for y_pos in arrow_positions:
        fig.add_annotation(
            x=0.5, y=y_pos,
            ax=0.5, ay=y_pos+0.05,
            xref="x", yref="y",
            axref="x", ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=3,
            arrowcolor="#00D4FF"
        )
    
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0, 1]),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0, 1]),
        height=450,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Key features - SIMPLIFIED
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
    
    # Simulation controls
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📹 Drone Flight Simulation")
        num_frames = st.slider("Number of frames:", 100, 1000, 500)
        
        if st.button("🚀 Start Classification", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate classification
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
            
            st.success("✅ Complete!")
            
            # Calculate metrics
            total_raw = num_frames * 4.0
            total_stored = sum(data_sizes)
            reduction = ((total_raw - total_stored) / total_raw) * 100
            
            # Display results
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Raw Data", f"{total_raw/1000:.1f} GB")
            col_b.metric("Stored", f"{total_stored/1000:.1f} GB", f"-{reduction:.0f}%")
            col_c.metric("Lifespan", f"{100/(100-reduction):.1f}x")
            
            # Pie chart
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
            
            st.plotly_chart(fig, width='stretch')
    
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
    
    if st.button("🔍 Analyze", type="primary"):
        with st.spinner("Analyzing..."):
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
            col_a.metric("Healthy", num_blocks - len(failing_blocks))
            col_b.metric("Failing", len(failing_blocks))
            col_c.metric("Avg Health", f"{np.mean([b['health'] for b in blocks_data]):.0f}%")
            
            # Plot
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
            
            st.plotly_chart(fig, width='stretch')
            
            if len(failing_blocks) > 0:
                st.warning(f"⚠️ {len(failing_blocks)} blocks need attention within 14-21 days")


def show_module4():
    st.header("🔋 Module 4: Adaptive Power Controller")
    
    device_type = st.selectbox("Device:", ["Drone", "IoT Sensor", "Trail Camera", "Surveillance"])
    
    col1, col2 = st.columns(2)
    with col1:
        battery_capacity = st.slider("Battery (Wh):", 10, 100, 50)
    with col2:
        simulation_hours = st.slider("Duration (hrs):", 12, 48, 24)
    
    if st.button("⚡ Simulate", type="primary"):
        with st.spinner("Simulating..."):
            time.sleep(1)
            
            hours = np.arange(0, simulation_hours, 0.25)
            traditional_power = np.ones(len(hours)) * 3.2
            
            aura_power = []
            states = []
            
            for hour in hours:
                hour_of_day = hour % 24
                
                if device_type == "Drone":
                    if 9 <= hour_of_day < 17:
                        power, state = 2.3, "Active"
                    elif 8 <= hour_of_day < 9 or 17 <= hour_of_day < 18:
                        power, state = 1.2, "Idle"
                    elif 18 <= hour_of_day < 22:
                        power, state = 2.4, "Charging"
                    else:
                        power, state = 0.1, "Deep Sleep"
                
                elif device_type == "IoT Sensor":
                    if hour_of_day % 1 == 0:
                        power, state = 2.0, "Active"
                    else:
                        power, state = 0.1, "Deep Sleep"
                
                elif device_type == "Trail Camera":
                    if 6 <= hour_of_day < 20:
                        power, state = 2.3, "Active"
                    else:
                        power, state = 0.1, "Deep Sleep"
                
                else:
                    power, state = 2.3, "Active"
                
                aura_power.append(power + np.random.uniform(-0.1, 0.1))
                states.append(state)
            
            aura_power = np.array(aura_power)
            
            traditional_energy = np.trapz(traditional_power, dx=0.25)
            aura_energy = np.trapz(aura_power, dx=0.25)
            savings = ((traditional_energy - aura_energy) / traditional_energy) * 100
            
            traditional_runtime = battery_capacity / 3.2
            aura_runtime = battery_capacity / np.mean(aura_power)
            
            st.success("✅ Complete!")
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Traditional", f"{np.mean(traditional_power):.1f}W")
            col_b.metric("AURA", f"{np.mean(aura_power):.1f}W", f"-{savings:.0f}%")
            col_c.metric("Runtime", f"{aura_runtime:.1f}h", f"+{((aura_runtime/traditional_runtime-1)*100):.0f}%")
            
            # Graph
            st.subheader("📊 Power Profile")
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=hours, y=traditional_power,
                mode='lines', name='Traditional',
                line=dict(color='#95A5A6', width=2, dash='dash')
            ))
            
            fig.add_trace(go.Scatter(
                x=hours, y=aura_power,
                mode='lines', name='AURA',
                line=dict(color='#E31E24', width=3),
                fill='tonexty'
            ))
            
            fig.update_layout(
                xaxis_title="Hours",
                yaxis_title="Power (W)",
                height=400,
                hovermode='x unified'
            )
            
            st.plotly_chart(fig, width='stretch')


# ============= MAIN CODE =============

st.markdown('<p class="main-header">🧠 AURA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Edge Storage Intelligence</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.image("https://via.placeholder.com/300x100/E31E24/FFFFFF?text=SanDisk+AURA", width='stretch')
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Demo:", 
                         ["Overview", 
                          "Module 1: Data Manager", 
                          "Module 2: Health Engine",
                          "Module 4: Power Control"])

st.sidebar.markdown("---")
st.sidebar.info("**Team AURA**\nPSG Institute\nCerebrum 2025")

# Route to pages
if page == "Overview":
    show_overview()
elif page == "Module 1: Data Manager":
    show_module1()
elif page == "Module 2: Health Engine":
    show_module2()
elif page == "Module 4: Power Control":
    show_module4()
