"""
Configuration settings for the Mining Production Dashboard
"""

# Application Settings
APP_NAME = "Mining Production Excellence Dashboard"
APP_VERSION = "2.0.0"
COMPANY_NAME = "Global Mining Corporation"
SUPPORT_EMAIL = "operations@globalmining.com"
HELP_DESK_PHONE = "+1-800-MINING"

# Dashboard Settings
DEFAULT_DATE_RANGE = ("2025-01-01", "2025-12-31")
REFRESH_INTERVAL = 300  # Seconds (5 minutes)
CACHE_DURATION = 600  # Seconds (10 minutes)

# Data Generation Settings
DATA_SEED = 42  # Random seed for reproducible data
EQUIPMENT_COUNT = 30
MIN_EQUIPMENT_CAPACITY = 50  # Tons per hour
MAX_EQUIPMENT_CAPACITY = 1000  # Tons per hour
OPERATIONAL_RATE = 0.75  # 75% of equipment operational
MAINTENANCE_RATE = 0.15  # 15% in maintenance
IDLE_RATE = 0.10  # 10% idle

# Mining Sites
MINING_SITES = [
    "North Pit",
    "South Pit", 
    "East Pit",
    "West Pit",
    "Processing Plant"
]

# Equipment Types
EQUIPMENT_TYPES = [
    "Excavator",
    "Haul Truck", 
    "Crusher",
    "Loader",
    "Drill Rig",
    "Dozer",
    "Grader"
]

# Material Types
MATERIAL_TYPES = [
    "Iron Ore",
    "Copper Ore",
    "Coal",
    "Gold Ore",
    "Waste Rock"
]

# Quality Grades
QUALITY_GRADES = ["High", "Medium", "Low"]
QUALITY_WEIGHTS_HIGH = [0.8, 0.15, 0.05]
QUALITY_WEIGHTS_MEDIUM = [0.5, 0.4, 0.1]
QUALITY_WEIGHTS_LOW = [0.3, 0.5, 0.2]

# Shift Settings
SHIFTS = ["Day", "Night"]
SHIFT_HOURS = {
    "Day": (6, 18),  # 6 AM to 6 PM
    "Night": (18, 6)  # 6 PM to 6 AM
}

# Downtime Settings
DOWNTIME_TYPES = [
    "Mechanical",
    "Electrical", 
    "Hydraulic",
    "Operational",
    "Planned Maintenance",
    "Weather"
]

# KPI Thresholds
OEE_THRESHOLDS = {
    "WORLD_CLASS": 85,
    "GOOD": 70,
    "POOR": 60,
    "CRITICAL": 50
}

UTILIZATION_THRESHOLDS = {
    "EXCELLENT": 85,
    "GOOD": 70,
    "POOR": 50
}

# Cost Settings (USD)
OPERATIONAL_COST_PER_TON = 15.0
MAINTENANCE_COST_HOURLY = 150.0
FUEL_COST_PER_LITER = 1.2

# Alert Settings
PREDICTIVE_ALERTS = [
    {
        "equipment": "Excavator",
        "metric": "engine_hours",
        "threshold": 10000,
        "severity": "High"
    },
    {
        "equipment": "Haul Truck", 
        "metric": "brake_wear",
        "threshold": 85,
        "severity": "High"
    },
    {
        "equipment": "Crusher",
        "metric": "bearing_temperature",
        "threshold": 120,
        "severity": "Medium"
    }
]

# Visualization Settings
CHART_COLORS = {
    "primary": "#FF6B00",
    "secondary": "#4A90E2", 
    "success": "#38A169",
    "warning": "#D69E2E",
    "danger": "#E53E3E",
    "dark": "#1A202C",
    "light": "#F7FAFC"
}

CHART_TEMPLATE = "plotly_dark"
CHART_HEIGHT = 400

# Export Settings
EXPORT_FORMATS = ["Excel", "PDF", "CSV"]
DEFAULT_EXPORT_FORMAT = "Excel"

# Security Settings (for future implementation)
REQUIRE_AUTHENTICATION = False
ALLOWED_USERS = ["admin", "operator", "manager"]
SESSION_TIMEOUT = 3600  # 1 hour

# Logging Settings
LOG_LEVEL = "INFO"
LOG_FILE = "mining_dashboard.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Database Settings (for future implementation)
DATABASE_CONFIG = {
    "type": "postgresql",  # postgresql, mysql, sqlite
    "host": "localhost",
    "port": 5432,
    "database": "mining_production",
    "username": "mining_user",
    "password": "secure_password"
}

# API Settings (for future implementation)
API_ENABLED = False
API_PORT = 8000
API_HOST = "0.0.0.0"
API_VERSION = "v1"

# Email Notification Settings
EMAIL_NOTIFICATIONS = {
    "enabled": False,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "dashboard@globalmining.com",
    "recipients": ["operations@globalmining.com", "maintenance@globalmining.com"]
}

# Performance Settings
MAX_ROWS_TO_DISPLAY = 10000
ENABLE_DATA_SAMPLING = True
SAMPLE_SIZE = 1000

def get_quality_weights(operator_skill):
    """Get quality weights based on operator skill level"""
    if operator_skill == "High":
        return QUALITY_WEIGHTS_HIGH
    elif operator_skill == "Medium":
        return QUALITY_WEIGHTS_MEDIUM
    else:
        return QUALITY_WEIGHTS_LOW

def get_shift_hours(shift):
    """Get shift hours based on shift type"""
    return SHIFT_HOURS.get(shift, (0, 24))

def get_oee_status(oee_value):
    """Get OEE status based on value"""
    if oee_value >= OEE_THRESHOLDS["WORLD_CLASS"]:
        return "World Class", "success"
    elif oee_value >= OEE_THRESHOLDS["GOOD"]:
        return "Good", "warning"
    elif oee_value >= OEE_THRESHOLDS["POOR"]:
        return "Poor", "danger"
    else:
        return "Critical", "danger"

def get_utilization_status(utilization_value):
    """Get utilization status based on value"""
    if utilization_value >= UTILIZATION_THRESHOLDS["EXCELLENT"]:
        return "Excellent", "success"
    elif utilization_value >= UTILIZATION_THRESHOLDS["GOOD"]:
        return "Good", "warning"
    else:
        return "Poor", "danger"
