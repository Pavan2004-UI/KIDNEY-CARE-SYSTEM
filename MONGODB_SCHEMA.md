# MongoDB Schema Documentation - Kidney Care System

## 📁 Database Name: `kidney_care_system`

---

## 📊 Collections Overview

### 1. **users** - User Accounts & Profiles
Stores user registration data and account information

### 2. **health_assessments** - Medical Parameters
Stores all medical test results and health metrics for each assessment

### 3. **predictions** - ML Model Results
Stores prediction results from all 5 ML models

### 4. **lab_reports** - Medical Test Reports
Stores user's lab test results and medical reports

### 5. **appointments** - Medical Appointments
Stores user's scheduled medical appointments

---

## 📋 Detailed Schema

### Collection: `users`

**Purpose:** Store user account information

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "email": "john@example.com",              // Unique, indexed
  "password": "$2b$12$...",                 // Bcrypt hashed password
  "name": "John Doe",
  "age": 48,
  "gender": "Male",                         // Male, Female, Other
  "city": "Bangalore",
  "created_at": ISODate("2024-04-20T10:00:00Z"),
  "updated_at": ISODate("2024-04-20T10:00:00Z"),
  "condition": "Stage 3 CKD",              // CKD stage
  "medical_history": []                     // Array for future use
}
```

**Indexes:**
```
- email (unique)
- created_at
```

**Sample Data:**
```javascript
db.users.insertOne({
  email: "john@example.com",
  password: "$2b$12$KIXxPfxzAW...",
  name: "John Doe",
  age: 48,
  gender: "Male",
  city: "Bangalore",
  created_at: new Date(),
  updated_at: new Date(),
  condition: "Stage 3 CKD",
  medical_history: []
})
```

---

### Collection: `health_assessments`

**Purpose:** Store detailed medical parameters for each patient assessment

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439012"),
  "email": "john@example.com",              // Foreign key to users
  "created_at": ISODate("2024-04-20T10:15:00Z"),
  
  // Basic Parameters
  "age": 48,                                // Integer
  "bp": 128,                                // Blood Pressure (mmHg)
  "sg": 1.015,                              // Specific Gravity
  "al": 1,                                  // Albumin (0-5)
  "su": 0,                                  // Sugar (0-5)
  
  // Urine Analysis
  "rbc": 0,                                 // RBC in Urine (0=Normal, 1=Abnormal)
  "pc": 0,                                  // Pus Cell (0=Normal, 1=Abnormal)
  "pcc": 0,                                 // Pus Cell Clumps (0=Not Present, 1=Present)
  "ba": 0,                                  // Bacteria (0=Not Present, 1=Present)
  
  // Lab Results
  "bgr": 121,                               // Blood Glucose Random (mg/dL)
  "bu": 36,                                 // Blood Urea (mg/dL)
  "sc": 1.2,                                // Serum Creatinine (mg/dL) - KEY KIDNEY INDICATOR
  "sod": 140,                               // Sodium (mEq/L)
  "pot": 4.5,                               // Potassium (mEq/L)
  "hemo": 15.4,                             // Hemoglobin (g/dL)
  "pcv": 44,                                // Packed Cell Volume (%)
  "wc": 7800,                               // White Blood Cell Count
  "rc": 5.2,                                // Red Blood Cell Count
  
  // Clinical Conditions
  "htn": 1,                                 // Hypertension (0=No, 1=Yes)
  "dm": 1,                                  // Diabetes Mellitus (0=No, 1=Yes)
  "cad": 0,                                 // Coronary Artery Disease (0=No, 1=Yes)
  "appet": 0,                               // Appetite (0=Good, 1=Poor)
  "pe": 0,                                  // Pedal Edema (0=No, 1=Yes)
  "ane": 0                                  // Anemia (0=No, 1=Yes)
}
```

**Indexes:**
```
- email
- created_at
- email + created_at (compound)
```

**Sample Data:**
```javascript
db.health_assessments.insertOne({
  email: "john@example.com",
  created_at: new Date(),
  age: 48,
  bp: 128,
  sg: 1.015,
  al: 1,
  su: 0,
  rbc: 0,
  pc: 0,
  pcc: 0,
  ba: 0,
  bgr: 121,
  bu: 36,
  sc: 1.2,
  sod: 140,
  pot: 4.5,
  hemo: 15.4,
  pcv: 44,
  wc: 7800,
  rc: 5.2,
  htn: 1,
  dm: 1,
  cad: 0,
  appet: 0,
  pe: 0,
  ane: 0
})
```

---

### Collection: `predictions`

**Purpose:** Store ML model prediction results and risk scores

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439013"),
  "email": "john@example.com",              // Foreign key to users
  "created_at": ISODate("2024-04-20T10:20:00Z"),
  
  // Model Predictions (probability 0-1)
  "ensemble_risk": 0.65,                    // Ensemble (RF + LR + SVM) - PRIMARY SCORE
  "rf_risk": 0.63,                          // Random Forest
  "lr_risk": 0.67,                          // Logistic Regression
  "svm_risk": 0.66,                         // Support Vector Machine
  "gb_risk": 0.64,                          // Gradient Boosting
  
  // Risk Assessment
  "risk_level": "Medium",                   // Low/Medium/High
  
  // Associated Health Metrics
  "gfr_value": 68.5,                        // Glomerular Filtration Rate (mL/min)
  "creatinine": 1.2,                        // Serum Creatinine (mg/dL)
  "age": 48                                 // Patient age at time of prediction
}
```

**Indexes:**
```
- email
- created_at
- email + created_at (compound)
```

**Sample Data:**
```javascript
db.predictions.insertOne({
  email: "john@example.com",
  created_at: new Date(),
  ensemble_risk: 0.65,
  rf_risk: 0.63,
  lr_risk: 0.67,
  svm_risk: 0.66,
  gb_risk: 0.64,
  risk_level: "Medium",
  gfr_value: 68.5,
  creatinine: 1.2,
  age: 48
})
```

---

### Collection: `lab_reports`

**Purpose:** Store user's medical lab test reports

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439013"),
  "email": "john@example.com",              // Foreign key to users
  "reports": [
    {
      "name": "Kidney Function Test",       // Test name
      "date": "2024-04-20",                 // Test date
      "doctor": "Dr. Sarah Johnson",        // Ordering doctor
      "status": "completed",                // completed, pending
      "file_url": "https://...",            // Optional file URL
      "created_at": ISODate("2024-04-20T10:00:00Z")
    }
  ]
}
```

**Indexes:**
```
- email (unique)
```

**Sample Data:**
```javascript
db.lab_reports.insertOne({
  email: "john@example.com",
  reports: [
    {
      name: "Kidney Function Test",
      date: "2024-04-20",
      doctor: "Dr. Sarah Johnson",
      status: "completed",
      created_at: new Date()
    }
  ]
})
```

---

### Collection: `appointments`

**Purpose:** Store user's medical appointments

```javascript
{
  "_id": ObjectId("507f1f77bcf86cd799439014"),
  "email": "john@example.com",              // Foreign key to users
  "appointments": [
    {
      "date": "2024-04-25",                 // Appointment date
      "time": "10:00",                      // Appointment time
      "doctor": "Dr. Sarah Johnson",        // Doctor name
      "specialty": "Nephrologist",          // Medical specialty
      "location": "City Hospital, Room 302", // Location
      "status": "upcoming",                 // upcoming, completed, cancelled
      "created_at": ISODate("2024-04-20T10:00:00Z")
    }
  ]
}
```

**Indexes:**
```
- email (unique)
```

**Sample Data:**
```javascript
db.appointments.insertOne({
  email: "john@example.com",
  appointments: [
    {
      date: "2024-04-25",
      time: "10:00",
      doctor: "Dr. Sarah Johnson",
      specialty: "Nephrologist",
      location: "City Hospital, Room 302",
      status: "upcoming",
      created_at: new Date()
    }
  ]
})
```

---

## 🔑 Field Descriptions

### Health Assessment Fields

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| age | Integer | 1-150 | Patient age in years |
| bp | Integer | 50-200 | Blood pressure in mmHg |
| sg | Float | 1.005-1.030 | Urine specific gravity |
| al | Integer | 0-5 | Albumin level (0=no, 1-5=increasing) |
| su | Integer | 0-5 | Sugar level (0=no, 1-5=increasing) |
| rbc | Integer | 0-1 | RBC in urine (0=Normal, 1=Abnormal) |
| pc | Integer | 0-1 | Pus cell presence |
| pcc | Integer | 0-1 | Pus cell clumps |
| ba | Integer | 0-1 | Bacteria in urine |
| bgr | Integer | 50-500 | Blood glucose random (mg/dL) |
| bu | Integer | 10-200 | Blood urea (mg/dL) |
| sc | Float | 0.4-15.0 | Serum creatinine - **KEY INDICATOR** |
| sod | Integer | 100-180 | Sodium level (mEq/L) |
| pot | Float | 2.0-8.0 | Potassium level (mEq/L) |
| hemo | Float | 5.0-20.0 | Hemoglobin (g/dL) |
| pcv | Integer | 20-60 | Packed cell volume (%) |
| wc | Integer | 2000-20000 | White blood cell count |
| rc | Float | 2.0-8.0 | Red blood cell count |
| htn | Integer | 0-1 | Hypertension (0=No, 1=Yes) |
| dm | Integer | 0-1 | Diabetes (0=No, 1=Yes) |
| cad | Integer | 0-1 | Coronary artery disease |
| appet | Integer | 0-1 | Appetite (0=Good, 1=Poor) |
| pe | Integer | 0-1 | Pedal edema |
| ane | Integer | 0-1 | Anemia |

---

## 📈 Useful Queries

### Get user's latest prediction
```javascript
db.predictions.findOne({ email: "john@example.com" }, { sort: { created_at: -1 } })
```

### Get user's prediction history (last 5)
```javascript
db.predictions.find({ email: "john@example.com" })
  .sort({ created_at: -1 })
  .limit(5)
```

### Get user's health assessments
```javascript
db.health_assessments.find({ email: "john@example.com" })
  .sort({ created_at: -1 })
  .limit(10)
```

### Get high-risk patients (ensemble_risk > 0.7)
```javascript
db.predictions.find({ ensemble_risk: { $gt: 0.7 } })
  .sort({ created_at: -1 })
```

### Get all users
```javascript
db.users.find({})
```

### Update user condition
```javascript
db.users.updateOne(
  { email: "john@example.com" },
  { $set: { condition: "Stage 4 CKD" } }
)
```

---

## 🔐 Security Features

1. **Password Hashing**: All passwords hashed with bcrypt (10+ rounds)
2. **Unique Emails**: Email field is unique indexed
3. **Data Isolation**: Each user can only access their own data
4. **Timestamps**: All records have created_at and updated_at

---

## 📊 Data Size Estimate

- **users collection**: ~1-2 KB per document
- **health_assessments collection**: ~2-3 KB per document
- **predictions collection**: ~1-2 KB per document
- **lab_reports collection**: ~5-10 KB per document (with file URLs)
- **appointments collection**: ~2-5 KB per document

For 10,000 users with 50 assessments, 50 predictions, 20 lab reports, and 30 appointments each:
- Total size: ~1-2 GB

---

## 🛠️ Maintenance

### Create Indexes
```javascript
// Users collection
db.users.createIndex({ email: 1 }, { unique: true })
db.users.createIndex({ created_at: -1 })

// Health assessments
db.health_assessments.createIndex({ email: 1 })
db.health_assessments.createIndex({ created_at: -1 })
db.health_assessments.createIndex({ email: 1, created_at: -1 })

// Predictions
db.predictions.createIndex({ email: 1 })
db.predictions.createIndex({ created_at: -1 })
db.predictions.createIndex({ email: 1, created_at: -1 })

// Lab reports
db.lab_reports.createIndex({ email: 1 }, { unique: true })

// Appointments
db.appointments.createIndex({ email: 1 }, { unique: true })
```

### Backup
```bash
mongodump --uri "mongodb+srv://user:password@host/kidney_care_system" --out ./backup
```

### Restore
```bash
mongorestore --uri "mongodb+srv://user:password@host/kidney_care_system" ./backup
```
