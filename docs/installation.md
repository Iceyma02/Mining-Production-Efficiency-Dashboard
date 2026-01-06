# 🛠️ Installation Guide

Complete setup guide for the Mining Production Efficiency Dashboard.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, Ubuntu 18.04+
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: 500MB free space
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

### Software Requirements
- **Python**: 3.9 or higher
- **pip**: Latest version
- **Git**: For version control

## 🚀 Quick Installation (5 Minutes)

### Windows
```powershell
# 1. Open PowerShell as Administrator
# 2. Clone the repository
git clone https://github.com/yourusername/mining-production-dashboard.git

# 3. Navigate to project folder
cd mining-production-dashboard

# 4. Create virtual environment
python -m venv venv

# 5. Activate virtual environment
venv\Scripts\activate

# 6. Install dependencies
pip install -r requirements.txt

# 7. Run the dashboard
streamlit run app.py
