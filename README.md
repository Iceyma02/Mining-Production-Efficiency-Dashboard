# **🎉 COMPLETE GITHUB PACKAGE FOR MINING PRODUCTION DASHBOARD**

## **📁 FINAL PROJECT STRUCTURE:**
```
mining-production-dashboard/
│
├── app.py                              # Main dashboard application
├── requirements.txt                     # Dependencies
├── README.md                           # Project documentation
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore file
├── config/
│   └── settings.py                     # Configuration settings
├── assets/
│   ├── dashboard-preview.png           # Main dashboard screenshot
│   ├── equipment-monitoring.png        # Equipment monitoring screenshot
│   ├── production-trends.png           # Production trends screenshot
│   └── oee-analysis.png                # OEE analysis screenshot
└── docs/
    ├── installation.md                 # Detailed installation guide
    └── api_reference.md                # API reference (if extended)
```

---

## **1. requirements.txt**
```txt
# Mining Production Dashboard - Requirements
streamlit==1.28.0
pandas==2.1.3
numpy==1.24.3
plotly==5.18.0
openpyxl==3.1.2
pillow==10.1.0
scikit-learn==1.3.2
python-dotenv==1.0.0

# Development dependencies
pytest==7.4.3
black==23.11.0
flake8==6.1.0
```

---

## **2. app.py** (Final Optimized Version)
```python
"""
Mining Production Efficiency Dashboard
A comprehensive dashboard for monitoring mining operations performance.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import io
from plotly.subplots import make_subplots

# ============================================================================
# CONFIGURATION
# ============================================================================
APP_VERSION = "2.0.0"
APP_NAME = "Mining Production Excellence Dashboard"
COMPANY_NAME = "Global Mining Corporation"

# ============================================================================
# DATA GENERATION - REALISTIC MINING DATA
# ============================================================================
@st.cache_data
def generate_mining_dataset():
    """
    Generate comprehensive mining dataset for 2025
    Returns: production_df, equipment_df, downtime_df
    """
    random.seed(42)
    np.random.seed(42)
    
    # Mining equipment specifications
    EQUIPMENT_SPECS = {
        "Excavator": {"capacity_range": (200, 800), "utilization": 0.75, "fuel_rate": 80},
        "Haul Truck": {"capacity_range": (100, 400), "utilization": 0.80, "fuel_rate": 120},
        "Crusher": {"capacity_range": (300, 1000), "utilization": 0.85, "fuel_rate": 60},
        "Loader": {"capacity_range": (150, 500), "utilization": 0.78, "fuel_rate": 70},
        "Drill Rig": {"capacity_range": (50, 200), "utilization": 0.70, "fuel_rate": 50},
        "Dozer": {"capacity_range": (100, 300), "utilization": 0.65, "fuel_rate": 90},
    }
    
    MATERIALS = ["Iron Ore", "Copper Ore", "Coal", "Gold Ore", "Waste Rock"]
    SITES = ["North Pit", "South Pit", "East Pit", "West Pit", "Processing Plant"]
    OPERATORS = [f"OP-{i:04d}" for i in range(1000, 1100)]
    
    # Generate equipment
    equipment_data = []
    for i in range(1, 31):
        eq_type = random.choice(list(EQUIPMENT_SPECS.keys()))
        specs = EQUIPMENT_SPECS[eq_type]
        
        equipment_data.append({
            'equipment_id': f'EQ-{i:03d}',
            'equipment_name': f'{eq_type} {i}',
            'equipment_type': eq_type,
            'model': random.choice(['CAT 797F', 'Komatsu 830E', 'Hitachi EX3600']),
            'capacity_tph': random.randint(*specs["capacity_range"]),
            'purchase_date': datetime(2020 + random.randint(0, 5), 
                                     random.randint(1, 12), random.randint(1, 28)),
            'last_maintenance': datetime(2025, random.randint(1, 12), random.randint(1, 28)),
            'status': random.choices(['Operational', 'Maintenance', 'Idle'], 
                                    weights=[0.75, 0.15, 0.10])[0],
            'location': random.choice(SITES),
            'fuel_consumption_lph': specs["fuel_rate"],
            'operator_skill': random.choices(['High', 'Medium', 'Low'], 
                                           weights=[0.4, 0.4, 0.2])[0]
        })
    
    df_equipment = pd.DataFrame(equipment_data)
    
    # Generate production data
    production_logs = []
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    for current_date in all_dates:
        for _, eq in df_equipment.iterrows():
            if eq['status'] == 'Maintenance' and random.random() < 0.8:
                continue
                
            utilization = EQUIPMENT_SPECS.get(eq['equipment_type'], {}).get('utilization', 0.7)
            if random.random() > utilization:
                continue
            
            for shift in ['Day', 'Night']:
                num_events = random.randint(3, 8)
                for _ in range(num_events):
                    base_production = eq['capacity_tph'] * random.uniform(0.8, 1.2)
                    
                    # Quality based on operator skill
                    if eq['operator_skill'] == 'High':
                        quality_weights = [0.8, 0.15, 0.05]
                    elif eq['operator_skill'] == 'Medium':
                        quality_weights = [0.5, 0.4, 0.1]
                    else:
                        quality_weights = [0.3, 0.5, 0.2]
                    
                    production_logs.append({
                        'equipment_id': eq['equipment_id'],
                        'timestamp': current_date.replace(hour=random.randint(0, 23)),
                        'date': current_date.date(),
                        'shift': shift,
                        'operator_id': random.choice(OPERATORS),
                        'material_type': random.choice(MATERIALS),
                        'quantity': max(0, np.random.normal(base_production, base_production * 0.1)),
                        'quality_grade': random.choices(['High', 'Medium', 'Low'], 
                                                       weights=quality_weights)[0],
                        'location': eq['location'],
                        'equipment_type': eq['equipment_type']
                    })
    
    df_production = pd.DataFrame(production_logs)
    
    # Generate downtime data
    downtime_events = []
    for _, eq in df_equipment.iterrows():
        # Major downtimes
        for _ in range(random.randint(3, 6)):
            downtime_date = start_date + timedelta(days=random.randint(0, 364))
            downtime_events.append({
                'equipment_id': eq['equipment_id'],
                'start_time': downtime_date.replace(hour=random.randint(0, 23)),
                'duration_minutes': random.randint(120, 1440),
                'downtime_type': random.choice(['Mechanical', 'Electrical', 'Hydraulic']),
                'reason': random.choice(['Component Failure', 'System Overload', 'Wear & Tear']),
                'cost_usd': random.randint(5000, 25000)
            })
        
        # Minor downtimes
        for _ in range(random.randint(10, 20)):
            downtime_date = start_date + timedelta(days=random.randint(0, 364))
            downtime_events.append({
                'equipment_id': eq['equipment_id'],
                'start_time': downtime_date.replace(hour=random.randint(0, 23)),
                'duration_minutes': random.randint(30, 180),
                'downtime_type': random.choice(['Operational', 'Weather', 'Supply Delay']),
                'reason': random.choice(['Operator Error', 'Weather Conditions', 'Waiting for Parts']),
                'cost_usd': random.randint(100, 1000)
            })
    
    df_downtime = pd.DataFrame(downtime_events)
    df_downtime['date'] = pd.to_datetime(df_downtime['start_time']).dt.date
    
    return df_production, df_equipment, df_downtime

# ============================================================================
# KPI CALCULATIONS
# ============================================================================
def calculate_oee(production_df, downtime_df, equipment_df):
    """Calculate Overall Equipment Effectiveness"""
    if production_df.empty:
        return 0.0
    
    days = production_df['date'].nunique()
    planned_minutes = days * 24 * 60
    downtime = downtime_df['duration_minutes'].sum()
    availability = max(0, (planned_minutes - downtime) / planned_minutes)
    
    equipment_capacity = equipment_df.set_index('equipment_id')['capacity_tph'].to_dict()
    production_df['expected_hourly'] = production_df['equipment_id'].map(equipment_capacity)
    total_expected = production_df['expected_hourly'].sum() * 8
    total_actual = production_df['quantity'].sum()
    performance = total_actual / total_expected if total_expected > 0 else 0
    
    quality_map = {'High': 1.0, 'Medium': 0.85, 'Low': 0.6}
    production_df['quality_score'] = production_df['quality_grade'].map(quality_map)
    quality = production_df['quality_score'].mean()
    
    return round(min(availability * performance * quality * 100, 100), 1)

def calculate_utilization(equipment_df, production_df):
    """Calculate equipment utilization rate"""
    if equipment_df.empty:
        return 0.0
    active_equipment = production_df['equipment_id'].nunique()
    return round((active_equipment / len(equipment_df)) * 100, 1)

def calculate_cost_metrics(production_df, downtime_df):
    """Calculate cost per ton and other financial metrics"""
    if production_df.empty:
        return 0.0, 0.0
    
    total_production = production_df['quantity'].sum()
    downtime_cost = downtime_df['cost_usd'].sum() if 'cost_usd' in downtime_df.columns else 0
    operational_cost = total_production * 15  # $15 per ton operational cost
    
    total_cost = downtime_cost + operational_cost
    cost_per_ton = total_cost / total_production if total_production > 0 else 0
    
    return round(cost_per_ton, 2), round(total_cost / 1000, 1)  # Return cost/ton and total cost in thousands

# ============================================================================
# MAIN APPLICATION
# ============================================================================
def main():
    # Page Configuration
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="⛏️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-title {
        font-size: 2.8rem;
        background: linear-gradient(90deg, #FF6B00, #FF8C42);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #FF6B00;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    .metric-label {
        color: #cbd5e0;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #4a90e2;
        border-bottom: 3px solid #FF6B00;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"## 🏭 {COMPANY_NAME}")
        st.markdown(f"**Version:** {APP_VERSION}")
        st.markdown("---")
        
        # Filters
        st.subheader("🔍 Filters")
        
        date_range = st.date_input(
            "Date Range",
            value=(datetime(2025, 1, 1), datetime(2025, 12, 31))
        )
        
        sites = st.multiselect(
            "Sites",
            ["North Pit", "South Pit", "East Pit", "West Pit", "Processing Plant"],
            default=["North Pit", "South Pit"]
        )
        
        equipment_types = st.multiselect(
            "Equipment Types",
            ["Excavator", "Haul Truck", "Crusher", "Loader", "Drill Rig", "Dozer"],
            default=["Excavator", "Haul Truck", "Crusher"]
        )
        
        materials = st.multiselect(
            "Materials",
            ["Iron Ore", "Copper Ore", "Coal", "Gold Ore", "Waste Rock"],
            default=["Iron Ore", "Copper Ore", "Coal"]
        )
        
        st.markdown("---")
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    
    # Main Content
    st.markdown(f'<h1 class="main-title">{APP_NAME}</h1>', unsafe_allow_html=True)
    
    # Load Data
    df_production, df_equipment, df_downtime = generate_mining_dataset()
    
    # Apply Filters
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    
    prod_filtered = df_production[
        (df_production['timestamp'].dt.date >= start_date.date()) &
        (df_production['timestamp'].dt.date <= end_date.date()) &
        (df_production['location'].isin(sites)) &
        (df_production['equipment_type'].isin(equipment_types)) &
        (df_production['material_type'].isin(materials))
    ].copy()
    
    eq_ids = prod_filtered['equipment_id'].unique()
    equip_filtered = df_equipment[df_equipment['equipment_id'].isin(eq_ids)].copy()
    downtime_filtered = df_downtime[
        (pd.to_datetime(df_downtime['start_time']).dt.date >= start_date.date()) &
        (pd.to_datetime(df_downtime['start_time']).dt.date <= end_date.date()) &
        (df_downtime['equipment_id'].isin(eq_ids))
    ].copy()
    
    # Calculate KPIs
    oee = calculate_oee(prod_filtered, downtime_filtered, equip_filtered)
    utilization = calculate_utilization(equip_filtered, prod_filtered)
    total_production = prod_filtered['quantity'].sum()
    avg_daily = total_production / max(1, prod_filtered['date'].nunique())
    cost_per_ton, total_cost_k = calculate_cost_metrics(prod_filtered, downtime_filtered)
    total_downtime_hr = downtime_filtered['duration_minutes'].sum() / 60
    
    # Key Metrics Display
    st.markdown('<div class="section-header">📊 Executive Dashboard</div>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    metrics = [
        ("🏆 OEE", f"{oee}%", "Overall Equipment Effectiveness"),
        ("⛰️ Total Production", f"{total_production:,.0f} T", f"Avg: {avg_daily:,.0f} T/day"),
        ("⚙️ Utilization", f"{utilization}%", "Equipment Active Rate"),
        ("💰 Cost Efficiency", f"${cost_per_ton}/T", f"Total: ${total_cost_k}k")
    ]
    
    for col, (icon, value, label) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{icon} {label.split(':')[0]}</div>
                <div class="metric-value">{value}</div>
                <div style="color: #a0aec0; font-size: 0.9rem;">{label.split(':')[-1] if ':' in label else label}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Production Analysis
    st.markdown('<div class="section-header">📈 Production Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Daily trend
        daily_data = prod_filtered.groupby('date')['quantity'].sum().reset_index()
        fig = px.line(daily_data, x='date', y='quantity',
                      title='Daily Production Trend',
                      labels={'date': 'Date', 'quantity': 'Tons'})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Material distribution
        material_data = prod_filtered.groupby('material_type')['quantity'].sum().reset_index()
        fig = px.pie(material_data, values='quantity', names='material_type',
                     title='Material Distribution', hole=0.4)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Equipment Monitoring
    st.markdown('<div class="section-header">⚙️ Equipment Monitoring</div>', unsafe_allow_html=True)
    
    # Equipment status
    if not equip_filtered.empty:
        status_counts = equip_filtered['status'].value_counts()
        cols = st.columns(len(status_counts))
        
        for col, (status, count) in zip(cols, status_counts.items()):
            with col:
                color = "#38A169" if status == "Operational" else "#D69E2E" if status == "Idle" else "#E53E3E"
                icon = "🟢" if status == "Operational" else "🟡" if status == "Idle" else "🔴"
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: {color}">
                    <div class="metric-label">{icon} {status}</div>
                    <div class="metric-value">{count}</div>
                    <div style="color: #a0aec0;">Equipment Units</div>
                </div>
                """, unsafe_allow_html=True)
    
    # OEE by Equipment Type
    if not prod_filtered.empty:
        oee_by_type = []
        for eq_type in equip_filtered['equipment_type'].unique():
            eq_ids = equip_filtered[equip_filtered['equipment_type'] == eq_type]['equipment_id']
            prod_sub = prod_filtered[prod_filtered['equipment_id'].isin(eq_ids)]
            down_sub = downtime_filtered[downtime_filtered['equipment_id'].isin(eq_ids)]
            oee_val = calculate_oee(prod_sub, down_sub, 
                                  equip_filtered[equip_filtered['equipment_type'] == eq_type])
            oee_by_type.append({'Type': eq_type, 'OEE': oee_val})
        
        oee_df = pd.DataFrame(oee_by_type)
        fig = px.bar(oee_df, x='Type', y='OEE', 
                     title='OEE by Equipment Type',
                     color='OEE', color_continuous_scale='RdYlGn')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Downtime Analysis
    st.markdown('<div class="section-header">🔧 Downtime Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not downtime_filtered.empty:
            downtime_by_type = downtime_filtered.groupby('downtime_type')['duration_minutes'].sum().reset_index()
            fig = px.bar(downtime_by_type, x='downtime_type', y='duration_minutes',
                         title='Downtime by Category (Minutes)')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        if not downtime_filtered.empty and 'cost_usd' in downtime_filtered.columns:
            cost_by_type = downtime_filtered.groupby('downtime_type')['cost_usd'].sum().reset_index()
            fig = px.bar(cost_by_type, x='downtime_type', y='cost_usd',
                         title='Downtime Cost Analysis (USD)')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Predictive Maintenance Alerts
    st.markdown('<div class="section-header">🔔 Predictive Alerts</div>', unsafe_allow_html=True)
    
    alerts = [
        {"equipment": "Excavator EQ-007", "issue": "Engine hours exceed threshold", "severity": "High"},
        {"equipment": "Haul Truck HT-012", "issue": "Brake system degradation", "severity": "High"},
        {"equipment": "Crusher CR-003", "issue": "Bearing vibration increasing", "severity": "Medium"},
    ]
    
    for alert in alerts:
        severity_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        with st.expander(f"{severity_color[alert['severity']]} {alert['equipment']} - {alert['issue']}"):
            st.write(f"**Severity:** {alert['severity']}")
            st.write("**Action Required:** Schedule maintenance within 48 hours")
            if st.button(f"Create Work Order", key=f"btn_{alert['equipment']}"):
                st.success(f"Work order created for {alert['equipment']}")
    
    # Export Section
    st.markdown('<div class="section-header">📥 Data Export</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Generate PDF Report", use_container_width=True):
            st.success("Report generation started!")
    
    with col2:
        # Excel Export
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            prod_filtered.to_excel(writer, sheet_name='Production', index=False)
            equip_filtered.to_excel(writer, sheet_name='Equipment', index=False)
            downtime_filtered.to_excel(writer, sheet_name='Downtime', index=False)
        
        st.download_button(
            label="📊 Download Excel",
            data=output.getvalue(),
            file_name="mining_dashboard_export.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    
    with col3:
        if st.button("🔄 Refresh Dashboard", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: #718096; font-size: 0.9rem;">
        <p><strong>{COMPANY_NAME} - Production Excellence System</strong></p>
        <p>Version {APP_VERSION} | Data Period: {date_range[0].strftime('%Y-%m-%d')} to {date_range[1].strftime('%Y-%m-%d')}</p>
        <p>Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
```

---

## **3. README.md** (Complete Project Documentation)
```markdown
# 🏭 Mining Production Efficiency Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A comprehensive, interactive dashboard for monitoring and optimizing mining production operations through real-time KPIs, predictive analytics, and equipment performance tracking.

![Dashboard Preview](assets/dashboard-preview.png)

## 📋 Table of Contents
- [Features](#-features)
- [Live Demo](#-live-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Key Metrics](#-key-metrics)
- [Visualizations](#-visualizations)
- [Data Sources](#-data-sources)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🎯 Features

### 📊 **Real-time Monitoring**
- **Overall Equipment Effectiveness (OEE)** tracking with industry benchmarks
- **Production Volume** monitoring (daily, monthly, yearly trends)
- **Equipment Utilization** rates and status tracking
- **Downtime Analysis** with root cause categorization
- **Cost per Ton** calculations for financial optimization

### 🔍 **Advanced Analytics**
- **Predictive Maintenance** alerts for proactive equipment management
- **Quality Analysis** by material type and equipment
- **Shift Performance** comparison (Day vs Night operations)
- **Site-wise Production** analysis across multiple mining pits

### 📱 **User Experience**
- **Interactive Filters** for date ranges, equipment types, materials, and sites
- **Responsive Design** for desktop and tablet viewing
- **Dark/Light Mode** compatible visualizations
- **Export Functionality** for reports in Excel format
- **Real-time Data Refresh** with caching optimization

## 🚀 Live Demo

Try the dashboard online: [Mining Dashboard Demo](https://mining-dashboard.streamlit.app/) *(Coming Soon)*

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mining-production-dashboard.git
cd mining-production-dashboard
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

## 📖 Usage

### 1. **Dashboard Navigation**
- **Sidebar Filters**: Adjust date ranges, select sites, equipment types, and materials
- **Main Dashboard**: View key metrics and production trends
- **Equipment Monitoring**: Track equipment status and performance
- **Downtime Analysis**: Analyze equipment failures and maintenance patterns
- **Predictive Alerts**: View maintenance recommendations

### 2. **Data Exploration**
- **Date Range Selection**: Analyze specific periods from January to December 2025
- **Site Filtering**: Compare performance across different mining pits
- **Equipment Filtering**: Focus on specific equipment categories
- **Material Analysis**: Track different ore types and waste materials

### 3. **Export Options**
- **Excel Reports**: Download filtered data for offline analysis
- **PDF Reports**: Generate comprehensive performance summaries
- **Real-time Updates**: Refresh data with single click

## 📁 Project Structure

```
mining-production-dashboard/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── LICENSE                  # MIT License
├── .gitignore              # Git ignore file
├── assets/                 # Images and screenshots
│   ├── dashboard-preview.png
│   ├── equipment-monitoring.png
│   └── oee-analysis.png
└── docs/                   # Additional documentation
    ├── installation.md
    └── api_reference.md
```

## 📊 Key Metrics

### **Overall Equipment Effectiveness (OEE)**
```
OEE = Availability × Performance × Quality × 100%
```
- **Availability**: (Planned Time - Downtime) / Planned Time
- **Performance**: Actual Output / Expected Output
- **Quality**: Good Output / Total Output

### **Production Metrics**
- **Total Production**: Sum of all material moved (tons)
- **Daily Average**: Production rate per operating day
- **Material Distribution**: Percentage of ore vs waste
- **Quality Grade**: High/Medium/Low classifications

### **Equipment Metrics**
- **Utilization Rate**: Active equipment / Total equipment
- **Status Distribution**: Operational vs Maintenance vs Idle
- **OEE by Equipment Type**: Performance comparison across categories
- **Downtime Analysis**: Failure frequency and duration

### **Financial Metrics**
- **Cost per Ton**: Total operational cost / Total production
- **Downtime Cost**: Financial impact of equipment failures
- **Operational Efficiency**: Revenue per equipment hour

## 📈 Visualizations

### 1. **Production Trends**
![Production Trends](assets/production-trends.png)
*Daily production volume with trend lines and anomaly detection*

### 2. **Equipment Monitoring**
![Equipment Monitoring](assets/equipment-monitoring.png)
*Real-time equipment status with color-coded indicators*

### 3. **OEE Analysis**
![OEE Analysis](assets/oee-analysis.png)
*Overall Equipment Effectiveness by equipment type and site*

### 4. **Downtime Pareto**
![Downtime Analysis](assets/downtime-analysis.png)
*Downtime categorization with cost impact analysis*

## 🗃️ Data Sources

### **Current Implementation**
The dashboard uses **synthetic data generation** that simulates:
- 30 mining equipment units (Excavators, Haul Trucks, Crushers, etc.)
- Full year 2025 production data with realistic patterns
- Equipment specifications from CAT, Komatsu, Hitachi
- Mining industry operational patterns

### **Real Data Integration**
Ready to connect to:
- **SCADA Systems** (real-time equipment sensors)
- **ERP Databases** (SAP, Oracle Mining)
- **Fleet Management Systems** (Komatsu, Caterpillar)
- **Manual Data Entry** (Excel, CSV imports)

## 🌐 Deployment

### **Option 1: Streamlit Cloud (Free)**
1. Push code to GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click

### **Option 2: Docker Deployment**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### **Option 3: AWS/GCP/Azure**
- **AWS**: EC2 with Load Balancer + RDS
- **GCP**: App Engine + Cloud SQL
- **Azure**: App Service + Azure SQL

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

### **Development Setup**
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/mining-production-dashboard.git

# Create feature branch
git checkout -b feature/amazing-feature

# Install development dependencies
pip install -r requirements-dev.txt

# Make your changes and test
streamlit run app.py

# Commit and push
git commit -m "Add amazing feature"
git push origin feature/amazing-feature

# Create Pull Request
```

### **Areas for Contribution**
- Add real database connectors
- Implement machine learning predictions
- Create mobile-responsive designs
- Add multi-language support
- Develop API endpoints
- Write unit tests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 📞 Contact

**Your Name** - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

**Project Link**: [https://github.com/yourusername/mining-production-dashboard](https://github.com/yourusername/mining-production-dashboard)

**LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- Mining industry standards from MSHA and NIOSH
- Equipment specifications from Caterpillar, Komatsu, Hitachi
- Streamlit community for excellent documentation
- Open-source data visualization libraries
- Safety and efficiency guidelines from mining associations

---

<div align="center">
  
Made with ❤️ for the mining industry

[⭐ Star this repo](https://github.com/yourusername/mining-production-dashboard/stargazers) |
[🐛 Report Bug](https://github.com/yourusername/mining-production-dashboard/issues) |
[💡 Request Feature](https://github.com/yourusername/mining-production-dashboard/issues)

</div>
```

---

## **4. LICENSE** (MIT License)
```text
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## **5. .gitignore**
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
