# 🚀 Quick Start Guide - MongoDB & User Authentication

## Installation (First Time Only)

```bash
# Navigate to project
cd /Users/pavanm/KIDNEY-CARE-SYSTEM

# Install dependencies
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run streamlit_app.py
```

Open: **http://localhost:8502**

---

## Your First Login

### Create a New Account
1. Click **"➕ Register"** button
2. Fill in the form:
   ```
   Email: your.email@domain.com
   Password: YourSecurePassword123
   Full Name: Your Full Name
   Age: 45
   Gender: Male
   City: Bangalore
   ```
3. Click **"✅ Register"**
4. Login with your new credentials

### Alternative: Use Existing Account
If you already registered, just enter your email and password.

---

## Using the Kidney Prediction Feature

1. **Login** with your credentials
2. Navigate to **"🔬 Kidney Prediction"** from sidebar
3. **Fill all medical parameters** (all 24 fields):
   - Basic: Age, Blood Pressure, Specific Gravity, Albumin, Sugar
   - Lab: Glucose, Urea, Creatinine, Sodium, Potassium, Hemoglobin
   - Additional: PCV, WBC, RBC, RBC Urine, Pus Cell, Pus Cell Clumps, Bacteria
   - Conditions: Hypertension, Diabetes, CAD, Appetite, Pedal Edema, Anemia
4. Click **"🔍 Predict Kidney Disease Risk"**
5. **View results** from 5 ML models:
   - Random Forest
   - Logistic Regression
   - SVM
   - Gradient Boosting
   - Ensemble (Best - 98.75% accuracy)

---

## Your Data Stored in MongoDB

### What Gets Saved?

1. **User Profile** (`users` collection)
   - Email, password (hashed), name, age, gender, city
   - Account created/updated dates

2. **Health Assessments** (`health_assessments` collection)
   - All 24 medical parameters you entered
   - Timestamp of assessment

3. **Predictions** (`predictions` collection)
   - Risk scores from all 5 ML models
   - GFR and creatinine values
   - Risk level classification

### Example View in MongoDB

```javascript
// Your user document
{
  "email": "your.email@domain.com",
  "name": "Your Full Name",
  "age": 45,
  "gender": "Male",
  "city": "Bangalore",
  "created_at": "2024-04-20T10:45:00Z"
}

// Your latest prediction
{
  "email": "your.email@domain.com",
  "ensemble_risk": 0.65,        // 65% CKD probability
  "rf_risk": 0.63,
  "lr_risk": 0.67,
  "svm_risk": 0.66,
  "gb_risk": 0.64,
  "risk_level": "Medium",
  "created_at": "2024-04-20T10:50:00Z"
}
```

---

## 🔐 Security

✅ **Passwords are hashed** with bcrypt (never stored plain text)
✅ **Emails are unique** (one account per email)
✅ **Secure connection** to MongoDB Atlas
✅ **Your data is private** (only you can access it)

---

## ⚙️ Important Files

| File | What It Does |
|------|-------------|
| `streamlit_app.py` | Main application (register, login, predictions) |
| `mongodb_config.py` | Database connection & operations |
| `MONGODB_SCHEMA.md` | Complete database schema documentation |
| `MONGODB_INTEGRATION.md` | Setup & configuration guide |

---

## 🆘 Troubleshooting

### Can't Login?
- Check if email is registered (try Register if not)
- Verify password (case-sensitive)
- Check internet connection to MongoDB

### Prediction Error?
- Make sure ALL 24 fields are filled
- Check for "X has N features" error → fill all missing fields
- All fields have default values, verify they match your data

### Need to Check Your Data?
Use MongoDB Compass or shell:
```javascript
// View your user profile
db.users.findOne({email: "your@email.com"})

// View your predictions (latest first)
db.predictions.find({email: "your@email.com"}).sort({created_at: -1}).limit(5)
```

---

## 📊 Medical Parameters Guide

### What each field means:

**Basic Tests:**
- **Age**: Your age in years
- **BP**: Blood pressure (mmHg) - Normal: 120/80
- **SG**: Urine specific gravity - Normal: 1.005-1.030
- **Albumin (AL)**: Protein in urine - 0=none, 5=high
- **Sugar (SU)**: Glucose in urine - 0=none, 5=high

**Lab Results:**
- **Blood Glucose Random (BGR)**: Blood sugar mg/dL - Normal: 70-100
- **Blood Urea (BU)**: mg/dL - Normal: 7-20
- **Serum Creatinine (SC)**: mg/dL - **KEY KIDNEY INDICATOR** - Normal: 0.6-1.2
- **Sodium (SOD)**: mEq/L - Normal: 135-145
- **Potassium (POT)**: mEq/L - Normal: 3.5-5.0
- **Hemoglobin (HEMO)**: g/dL - Normal: 12-16

**Urine Analysis:**
- **RBC**: Red Blood Cells in urine
- **Pus Cell (PC)**: White blood cells in urine
- **Pus Cell Clumps (PCC)**: Presence of clumps
- **Bacteria (BA)**: Bacterial infection indicator

**Conditions:**
- **Hypertension (HTN)**: High blood pressure condition
- **Diabetes Mellitus (DM)**: Diabetes status
- **CAD**: Coronary artery disease
- **Appetite**: Food intake quality
- **Pedal Edema (PE)**: Leg/ankle swelling
- **Anemia (ANE)**: Low red blood cells

---

## 🎯 Next Steps

1. ✅ Install & run application
2. ✅ Create your account
3. ✅ Enter your health data
4. ✅ Get AI predictions
5. ✅ Track your kidney health over time

---

## 📞 Support

For issues or questions:
1. Check `MONGODB_INTEGRATION.md` for detailed setup
2. Review `MONGODB_SCHEMA.md` for database structure
3. Look at error messages in terminal

---

**You're all set! Start monitoring your kidney health with AI today! 🏥**
