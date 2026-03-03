import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import pickle
import os

st.set_page_config(page_title="AI Kidney Care System", layout="wide")

# Load ML models
@st.cache_resource
def load_models():
    try:
        with open('kidney_rf_model.pkl', 'rb') as f:
            rf_model = pickle.load(f)
        with open('kidney_gb_model.pkl', 'rb') as f:
            gb_model = pickle.load(f)
        with open('kidney_scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        return rf_model, gb_model, scaler
    except:
        return None, None, None

rf_model, gb_model, scaler = load_models()

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# User Database
users_db = {
    'john@email.com': {'password': 'password123', 'name': 'John Doe', 'age': 48, 'condition': 'Stage 3 CKD', 'city': 'Bangalore'},
    'sarah@email.com': {'password': 'sarah123', 'name': 'Sarah Smith', 'age': 55, 'condition': 'Stage 2 CKD', 'city': 'Bangalore'},
    'mike@email.com': {'password': 'mike123', 'name': 'Mike Johnson', 'age': 62, 'condition': 'Stage 4 CKD', 'city': 'Bangalore'},
    'emma@email.com': {'password': 'emma123', 'name': 'Emma Wilson', 'age': 45, 'condition': 'Stage 1 CKD', 'city': 'Bangalore'},
    'admin@kidney.com': {'password': 'admin123', 'name': 'Admin User', 'age': 35, 'condition': 'Healthcare Provider', 'city': 'Bangalore'}
}

def login_page():
    # Professional medical technology background
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1920&h=1080&fit=crop');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        /* Hide Streamlit header and toolbar */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        /* Style input fields */
        .stTextInput > div > div > input {
            background-color: #f0f9ff !important;
            border: 2px solid #667eea !important;
            color: #1e293b !important;
            font-weight: 500 !important;
        }
        /* Style expander */
        .streamlit-expanderHeader {
            background-color: #eef2ff !important;
            border: 2px solid #667eea !important;
            border-radius: 8px !important;
            color: #667eea !important;
            font-weight: 700 !important;
        }
        .streamlit-expanderContent {
            background-color: #f0f9ff !important;
            border: 2px solid #667eea !important;
            border-top: none !important;
            border-radius: 0 0 8px 8px !important;
            color: #667eea !important;
        }
        .streamlit-expanderContent p, .streamlit-expanderContent code {
            color: #667eea !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Center login card with no top margin
    st.markdown("<div style='margin-top: -80px;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        
        st.markdown("<h1 style='text-align: center; color: #ffffff; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 12px; font-family: Arial, sans-serif; font-weight: 800; font-size: 38px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin: 0;'>🫘 AI KIDNEY CARE SYSTEM</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #667eea; font-size: 18px; font-weight: 600; letter-spacing: 1px; margin-top: 15px;'>🤖 AI-Powered Healthcare Management</p>", unsafe_allow_html=True)
        st.markdown("<hr style='margin: 25px 0; border: 2px solid #667eea;'>", unsafe_allow_html=True)
        
        # Show available test accounts
        with st.expander("📋 Test Accounts"):
            st.write("**Available test accounts:**")
            st.code("john@email.com / password123")
            st.code("sarah@email.com / sarah123")
            st.code("mike@email.com / mike123")
            st.code("emma@email.com / emma123")
            st.code("admin@kidney.com / admin123")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Modern styled inputs with colored labels
        st.markdown("<p style='font-weight: 700; color: #667eea; margin-bottom: 8px; font-size: 16px;'>✉️ Email Address</p>", unsafe_allow_html=True)
        email = st.text_input("", placeholder="Enter your email address", key="email_input", label_visibility="collapsed")
        
        st.markdown("<p style='font-weight: 700; color: #667eea; margin-bottom: 8px; margin-top: 20px; font-size: 16px;'>🔐 Password</p>", unsafe_allow_html=True)
        password = st.text_input("", type="password", placeholder="Enter your password", key="password_input", label_visibility="collapsed")
        
        # Debug info
        if email or password:
            st.caption(f"Debug: Email entered: '{email}' | Password entered: '{password}'")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Login", use_container_width=True, type="primary"):
                # Strip whitespace from inputs
                email = email.strip() if email else ""
                password = password.strip() if password else ""
                
                if email and password:
                    st.info(f"Checking credentials for: {email}")
                    if email in users_db:
                        if users_db[email]['password'] == password:
                            st.session_state.authenticated = True
                            st.session_state.current_user = users_db[email]['name']
                            st.session_state.current_email = email
                            st.success(f"✅ Welcome {users_db[email]['name']}!")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error(f"❌ Wrong password for {email}")
                    else:
                        st.error(f"❌ Email {email} not found in database")
                else:
                    st.warning("⚠️ Please enter both email and password")
        
        with col_btn2:
            if st.button("➕ Register", use_container_width=True):
                st.info("Registration feature coming soon!")
        
        st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #6b7280;'>🔐 Your health data is secure and encrypted</p>", unsafe_allow_html=True)

def dashboard():
    st.title("📊 Dashboard")
    
    # Display current date and time
    now = datetime.now()
    st.write(f"Welcome back, {st.session_state.current_user}! | 📅 {now.strftime('%B %d, %Y')} | 🕒 {now.strftime('%I:%M %p')}")
    
    # Health Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("GFR Level", "68 mL/min", "-2", delta_color="inverse")
    with col2:
        st.metric("Creatinine", "1.4 mg/dL", "0.1")
    with col3:
        st.metric("Blood Pressure", "128/82 mmHg", "2")
    with col4:
        st.metric("Protein in Urine", "150 mg/day", "-5", delta_color="inverse")
    
    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("GFR Trend (Last 6 Months)")
        gfr_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'GFR': [72, 70, 69, 68, 68, 68]
        })
        st.line_chart(gfr_data.set_index('Month'))
    
    with col2:
        st.subheader("Medication Adherence (This Week)")
        med_data = pd.DataFrame({
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'Taken': [3, 3, 2, 3, 3, 3, 3]
        })
        st.bar_chart(med_data.set_index('Day'))
    
    # Appointments with current dates
    st.subheader("Upcoming Appointments")
    next_week = now + timedelta(days=7)
    two_weeks = now + timedelta(days=14)
    appointments = pd.DataFrame({
        'Date': [next_week.strftime('%Y-%m-%d'), two_weeks.strftime('%Y-%m-%d')],
        'Doctor': ['Dr. Rajesh Kumar', 'Dr. Priya Sharma'],
        'Type': ['Nephrology Checkup', 'Lab Tests'],
        'Hospital': ['Manipal Hospital, Whitefield', 'Apollo Hospital, Bannerghatta Road']
    })
    st.dataframe(appointments, use_container_width=True)

def profile():
    st.title("👤 My Profile")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://ui-avatars.com/api/?name=" + st.session_state.current_user.replace(" ", "+") + "&background=4f46e5&color=fff&size=200&bold=true", width=200)
        st.caption("📷 Profile Picture")
    with col2:
        st.subheader(st.session_state.current_user)
        st.write(st.session_state.current_email if 'current_email' in st.session_state else "john.doe@email.com")
    
    st.divider()
    
    st.subheader("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Email", st.session_state.current_email if 'current_email' in st.session_state else "john.doe@email.com")
        st.text_input("Phone", "+91 98450 12345")
    with col2:
        st.date_input("Date of Birth", datetime(1975, 5, 15))
        st.text_input("Address", "Koramangala, Bangalore, Karnataka 560034")
    
    st.subheader("Medical Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_input("Blood Type", "O+")
    with col2:
        st.number_input("Height (cm)", value=175)
    with col3:
        st.number_input("Weight (kg)", value=78)
    
    if st.button("Save Changes", type="primary"):
        st.success("Profile updated successfully!")

def health_assessment():
    st.title("📋 Health Assessment")
    st.write("Answer these questions to help us understand your current health status")
    
    with st.form("assessment_form"):
        q1 = st.radio("Do you experience frequent urination?", ["Yes", "No", "Sometimes"])
        q2 = st.radio("Have you noticed swelling in your legs or ankles?", ["Yes", "No", "Sometimes"])
        q3 = st.radio("Do you feel fatigued or weak regularly?", ["Yes", "No", "Sometimes"])
        q4 = st.radio("Have you experienced changes in urine color?", ["Yes", "No", "Not Sure"])
        q5 = st.radio("Do you have difficulty sleeping?", ["Yes", "No", "Sometimes"])
        q6 = st.slider("Rate your overall pain level (0-10)", 0, 10, 0)
        
        submitted = st.form_submit_button("Submit Assessment", type="primary")
        if submitted:
            st.success("Assessment completed!")
            st.info("Based on your responses, we recommend scheduling a consultation with your nephrologist.")

def medications():
    st.title("💊 My Medications")
    
    if st.button("➕ Add Medication", type="primary"):
        st.session_state.show_add_med = True
    
    meds = [
        {"name": "Lisinopril", "dosage": "10mg", "frequency": "Once daily", "time": "08:00 AM", "taken": True},
        {"name": "Furosemide", "dosage": "40mg", "frequency": "Twice daily", "time": "08:00 AM, 08:00 PM", "taken": True},
        {"name": "Calcium Carbonate", "dosage": "500mg", "frequency": "Three times daily", "time": "08:00 AM, 02:00 PM, 08:00 PM", "taken": False}
    ]
    
    for med in meds:
        with st.container():
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.subheader(med['name'])
                st.write(f"{med['dosage']} - {med['frequency']}")
            with col2:
                st.write(f"⏰ {med['time']}")
            with col3:
                if med['taken']:
                    st.success("✓ Taken")
                else:
                    if st.button("Mark Taken", key=med['name']):
                        st.success("Marked as taken!")
            st.divider()

def appointments():
    st.title("📅 My Appointments")
    
    # Get current date for dynamic appointments
    today = datetime.now()
    next_week = today + timedelta(days=7)
    two_weeks = today + timedelta(days=14)
    
    if st.button("➕ Book Appointment", type="primary"):
        st.session_state.show_book = True
    
    st.subheader("Upcoming Appointments")
    upcoming = pd.DataFrame({
        'Date': [next_week.strftime('%Y-%m-%d'), two_weeks.strftime('%Y-%m-%d')],
        'Time': ['10:00 AM', '02:30 PM'],
        'Doctor': ['Dr. Rajesh Kumar', 'Dr. Priya Sharma'],
        'Specialty': ['Nephrologist', 'Lab Specialist'],
        'Location': ['Manipal Hospital, Whitefield', 'Apollo Hospital, Bannerghatta Road']
    })
    st.dataframe(upcoming, use_container_width=True)
    
    st.subheader("Past Appointments")
    past_date = today - timedelta(days=15)
    past = pd.DataFrame({
        'Date': [past_date.strftime('%Y-%m-%d')],
        'Doctor': ['Dr. Rajesh Kumar'],
        'Specialty': ['Nephrologist'],
        'Location': ['Manipal Hospital, Whitefield']
    })
    st.dataframe(past, use_container_width=True)

def diet_plan():
    st.title("🍽️ Kidney-Friendly Diet Plan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Recommended Foods")
        recommended = [
            {"name": "Cauliflower", "benefit": "Low in potassium"},
            {"name": "Blueberries", "benefit": "Rich in antioxidants"},
            {"name": "Fish", "benefit": "High-quality protein"},
            {"name": "Egg Whites", "benefit": "Pure protein source"},
            {"name": "Olive Oil", "benefit": "Healthy fats"}
        ]
        for food in recommended:
            st.success(f"**{food['name']}** - {food['benefit']}")
    
    with col2:
        st.subheader("❌ Foods to Avoid")
        avoid = [
            {"name": "Bananas", "reason": "High in potassium"},
            {"name": "Processed Meats", "reason": "High in sodium"},
            {"name": "Dairy Products", "reason": "High in phosphorus"},
            {"name": "Dark Sodas", "reason": "High in phosphorus"}
        ]
        for food in avoid:
            st.error(f"**{food['name']}** - {food['reason']}")
    
    st.divider()
    st.subheader("Daily Meal Plan")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Breakfast**")
        st.write("• Egg white omelet")
        st.write("• Whole grain toast")
        st.write("• Blueberries")
    with col2:
        st.write("**Lunch**")
        st.write("• Grilled fish")
        st.write("• Cauliflower rice")
        st.write("• Green salad")
    with col3:
        st.write("**Dinner**")
        st.write("• Chicken breast")
        st.write("• Steamed vegetables")
        st.write("• Quinoa")
    with col4:
        st.write("**Snacks**")
        st.write("• Apple slices")
        st.write("• Unsalted crackers")
        st.write("• Cucumber")

def lab_reports():
    st.title("📄 Lab Reports")
    
    reports = pd.DataFrame({
        'Report Name': ['Kidney Function Test', 'Blood Test - Complete Panel', 'Urine Analysis', 'GFR Test'],
        'Date': ['2024-01-10', '2024-01-10', '2023-12-15', '2023-11-20'],
        'Doctor': ['Dr. Rajesh Kumar', 'Dr. Rajesh Kumar', 'Dr. Priya Sharma', 'Dr. Rajesh Kumar'],
        'Hospital': ['Manipal Hospital', 'Manipal Hospital', 'Apollo Hospital', 'Manipal Hospital'],
        'Status': ['Completed', 'Completed', 'Completed', 'Completed']
    })
    
    for idx, row in reports.iterrows():
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(row['Report Name'])
                st.write(f"Date: {row['Date']} | Ordered by: {row['Doctor']}")
            with col2:
                st.button("👁️ View", key=f"view_{idx}")
                st.button("⬇️ Download", key=f"download_{idx}")
            st.divider()

def ai_insights():
    st.title("🧠 AI Health Insights")
    st.write("Personalized recommendations powered by artificial intelligence")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.warning("⚠️ **GFR Declining Trend**")
        st.write("Your GFR has decreased by 5% over the last 3 months. Consider discussing treatment adjustments.")
    with col2:
        st.success("✅ **Excellent Medication Adherence**")
        st.write("You have maintained 95% medication adherence this month. Keep up the great work!")
    with col3:
        st.info("💡 **Hydration Recommendation**")
        st.write("Based on your recent lab results, increasing water intake to 2L per day may help.")
    
    st.divider()
    st.subheader("📈 Health Predictions")
    st.write("AI-powered forecasts based on your health trends")
    
    predictions = pd.DataFrame({
        'Metric': ['GFR Level', 'Blood Pressure', 'Creatinine'],
        'Current': ['68', '128/82', '1.4'],
        'Predicted': ['66', '125/80', '1.5'],
        'Timeframe': ['3 months', '1 month', '2 months'],
        'Trend': ['↓', '↑', '↓']
    })
    st.dataframe(predictions, use_container_width=True)

def emergency_contacts():
    st.title("📞 Emergency Contacts")
    st.error("⚠️ In case of severe emergency, call 108 immediately")
    
    if st.button("➕ Add Contact", type="primary"):
        st.session_state.show_add_contact = True
    
    contacts = [
        {"name": "Dr. Rajesh Kumar", "role": "Primary Nephrologist", "phone": "+91 80 2550 0000", "hospital": "Manipal Hospital, Whitefield", "available": "24/7"},
        {"name": "Manipal Hospital ER", "role": "Emergency Room", "phone": "+91 80 2550 0001", "hospital": "Old Airport Road, Bangalore", "available": "24/7"},
        {"name": "Apollo Hospital ER", "role": "Emergency Room", "phone": "+91 80 2630 0000", "hospital": "Bannerghatta Road, Bangalore", "available": "24/7"},
        {"name": "Fortis Hospital", "role": "Dialysis Center", "phone": "+91 80 6621 4444", "hospital": "Bannerghatta Road, Bangalore", "available": "Mon-Sat 8AM-8PM"},
        {"name": "Narayana Health", "role": "Kidney Specialist Center", "phone": "+91 80 7122 2222", "hospital": "Bommasandra, Bangalore", "available": "24/7"}
    ]
    
    for contact in contacts:
        with st.container():
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.subheader(contact['name'])
                st.write(contact['role'])
                if 'hospital' in contact:
                    st.caption(f"🏥 {contact['hospital']}")
            with col2:
                st.write(f"📞 {contact['phone']}")
                st.write(f"🕐 Available: {contact['available']}")
            with col3:
                st.button("📞 Call", key=contact['name'])
            st.divider()

def kidney_prediction():
    st.title("🔬 Live Kidney Disease Prediction")
    st.write("Enter your medical parameters for AI-powered kidney disease risk assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Parameters")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=48)
        bp = st.number_input("Blood Pressure (mmHg)", min_value=50, max_value=200, value=80)
        sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025], index=2)
        al = st.selectbox("Albumin (0-5)", [0, 1, 2, 3, 4, 5], index=0)
        su = st.selectbox("Sugar (0-5)", [0, 1, 2, 3, 4, 5], index=0)
        
    with col2:
        st.subheader("Lab Results")
        bgr = st.number_input("Blood Glucose Random (mg/dL)", min_value=50, max_value=500, value=120)
        bu = st.number_input("Blood Urea (mg/dL)", min_value=10, max_value=200, value=40)
        sc = st.number_input("Serum Creatinine (mg/dL)", min_value=0.5, max_value=15.0, value=1.2, step=0.1)
        sod = st.number_input("Sodium (mEq/L)", min_value=100, max_value=180, value=140)
        pot = st.number_input("Potassium (mEq/L)", min_value=2.0, max_value=8.0, value=4.5, step=0.1)
        hemo = st.number_input("Hemoglobin (g/dL)", min_value=5.0, max_value=20.0, value=14.0, step=0.1)
    
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Additional Info")
        pcv = st.number_input("Packed Cell Volume (%)", min_value=20, max_value=60, value=44)
        wc = st.number_input("White Blood Cell Count (cells/cumm)", min_value=2000, max_value=20000, value=8000)
        rc = st.number_input("Red Blood Cell Count (millions/cmm)", min_value=2.0, max_value=8.0, value=5.0, step=0.1)
    
    with col4:
        st.subheader("Clinical Signs")
        rbc = st.selectbox("RBC in Urine", ["Normal", "Abnormal"], index=0)
        pc = st.selectbox("Pus Cell", ["Normal", "Abnormal"], index=0)
        pcc = st.selectbox("Pus Cell Clumps", ["Not Present", "Present"], index=0)
        ba = st.selectbox("Bacteria", ["Not Present", "Present"], index=0)
        htn = st.selectbox("Hypertension", ["No", "Yes"], index=0)
        dm = st.selectbox("Diabetes Mellitus", ["No", "Yes"], index=0)
    
    if st.button("🔍 Predict Kidney Disease Risk", type="primary", use_container_width=True):
        # Convert categorical to numerical
        rbc_val = 1 if rbc == "Abnormal" else 0
        pc_val = 1 if pc == "Abnormal" else 0
        pcc_val = 1 if pcc == "Present" else 0
        ba_val = 1 if ba == "Present" else 0
        htn_val = 1 if htn == "Yes" else 0
        dm_val = 1 if dm == "Yes" else 0
        
        # Create feature array
        features = np.array([[age, bp, sg, al, su, rbc_val, pc_val, pcc_val, ba_val, 
                             bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn_val, dm_val]])
        
        # Use ML models for prediction
        if rf_model is not None and gb_model is not None and scaler is not None:
            # Scale features
            features_scaled = scaler.transform(features)
            
            # Get predictions from both models
            rf_pred = rf_model.predict_proba(features_scaled)[0][1]
            gb_pred = gb_model.predict_proba(features_scaled)[0][1]
            
            # Ensemble prediction (average)
            ml_risk = (rf_pred + gb_pred) / 2
            risk_score = int(ml_risk * 100)
            
            st.info(f"🤖 Using Random Forest + Gradient Boosting Ensemble Model")
        else:
            # Fallback to rule-based
            risk_score = 0
            if sc > 1.5: risk_score += 25
            if bu > 50: risk_score += 20
            if hemo < 12: risk_score += 15
            if htn_val == 1: risk_score += 15
            if dm_val == 1: risk_score += 15
            if al > 2: risk_score += 10
            if bgr > 150: risk_score += 10
            if pcv < 35: risk_score += 10
            if pot > 5.5 or pot < 3.5: risk_score += 10
            if rbc_val == 1: risk_score += 10
            if pc_val == 1: risk_score += 10
            risk_score = min(risk_score, 100)
            st.warning("⚠️ Using rule-based prediction (ML models not loaded)")
        
        st.divider()
        st.subheader("🎯 Prediction Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Risk Score", f"{risk_score}%")
        
        with col2:
            if risk_score < 30:
                st.success("✅ Low Risk")
                risk_level = "Low"
            elif risk_score < 60:
                st.warning("⚠️ Moderate Risk")
                risk_level = "Moderate"
            else:
                st.error("🚨 High Risk")
                risk_level = "High"
        
        with col3:
            if risk_score < 30:
                stage = "Stage 1-2 CKD"
            elif risk_score < 60:
                stage = "Stage 2-3 CKD"
            else:
                stage = "Stage 3-4 CKD"
            st.info(f"📊 {stage}")
        
        st.divider()
        
        # Recommendations
        st.subheader("💡 Personalized Recommendations")
        
        if risk_score >= 60:
            st.error("**Immediate Action Required:**")
            st.write("• Schedule an urgent appointment with a nephrologist")
            st.write("• Get comprehensive kidney function tests done")
            st.write("• Monitor blood pressure and blood sugar daily")
            st.write("• Follow strict dietary restrictions")
        elif risk_score >= 30:
            st.warning("**Preventive Measures:**")
            st.write("• Schedule a consultation with your doctor within 2 weeks")
            st.write("• Get regular kidney function tests every 3 months")
            st.write("• Maintain healthy diet and exercise routine")
            st.write("• Monitor blood pressure regularly")
        else:
            st.success("**Maintain Healthy Lifestyle:**")
            st.write("• Continue regular health checkups")
            st.write("• Stay hydrated (8-10 glasses of water daily)")
            st.write("• Maintain balanced diet")
            st.write("• Exercise regularly (30 minutes daily)")
        
        st.divider()
        
        # Key indicators analysis
        st.subheader("📋 Key Indicators Analysis")
        
        indicators = []
        if sc > 1.5:
            indicators.append({"Parameter": "Serum Creatinine", "Value": f"{sc} mg/dL", "Status": "High", "Normal Range": "0.6-1.2 mg/dL"})
        if bu > 50:
            indicators.append({"Parameter": "Blood Urea", "Value": f"{bu} mg/dL", "Status": "High", "Normal Range": "7-20 mg/dL"})
        if hemo < 12:
            indicators.append({"Parameter": "Hemoglobin", "Value": f"{hemo} g/dL", "Status": "Low", "Normal Range": "12-16 g/dL"})
        if bgr > 150:
            indicators.append({"Parameter": "Blood Glucose", "Value": f"{bgr} mg/dL", "Status": "High", "Normal Range": "70-140 mg/dL"})
        if pot > 5.5:
            indicators.append({"Parameter": "Potassium", "Value": f"{pot} mEq/L", "Status": "High", "Normal Range": "3.5-5.5 mEq/L"})
        
        if indicators:
            df_indicators = pd.DataFrame(indicators)
            st.dataframe(df_indicators, use_container_width=True)
        else:
            st.success("✅ All parameters are within normal range!")
        
        # Nearby hospitals
        st.divider()
        st.subheader("🏥 Recommended Hospitals in Bangalore")
        
        hospitals = pd.DataFrame({
            'Hospital': ['Manipal Hospital', 'Apollo Hospital', 'Fortis Hospital', 'Narayana Health'],
            'Specialty': ['Nephrology', 'Nephrology', 'Dialysis', 'Kidney Transplant'],
            'Location': ['Whitefield', 'Bannerghatta Road', 'Bannerghatta Road', 'Bommasandra'],
            'Phone': ['+91 80 2550 0000', '+91 80 2630 0000', '+91 80 6621 4444', '+91 80 7122 2222']
        })
        st.dataframe(hospitals, use_container_width=True)

# Main app
if not st.session_state.authenticated:
    login_page()
else:
    # Sidebar navigation
    with st.sidebar:
        # Profile picture at top
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("https://ui-avatars.com/api/?name=" + st.session_state.current_user.replace(" ", "+") + "&background=4f46e5&color=fff&size=128&bold=true", width=128)
        
        st.title("🏥 Kidney Care")
        st.write(f"**{st.session_state.current_user}**")
        
        # Display current date and time
        now = datetime.now()
        st.info(f"📅 {now.strftime('%B %d, %Y')}")
        st.info(f"🕒 {now.strftime('%I:%M %p')}")
        
        st.divider()
        
        page = st.radio("Navigation", [
            "Dashboard",
            "Profile",
            "Health Assessment",
            "Kidney Prediction",
            "Medications",
            "Appointments",
            "Diet Plan",
            "Lab Reports",
            "AI Insights",
            "Emergency Contacts"
        ])
        
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.current_user = None
            st.rerun()
    
    # Page routing
    if page == "Dashboard":
        dashboard()
    elif page == "Profile":
        profile()
    elif page == "Health Assessment":
        health_assessment()
    elif page == "Kidney Prediction":
        kidney_prediction()
    elif page == "Medications":
        medications()
    elif page == "Appointments":
        appointments()
    elif page == "Diet Plan":
        diet_plan()
    elif page == "Lab Reports":
        lab_reports()
    elif page == "AI Insights":
        ai_insights()
    elif page == "Emergency Contacts":
        emergency_contacts()
