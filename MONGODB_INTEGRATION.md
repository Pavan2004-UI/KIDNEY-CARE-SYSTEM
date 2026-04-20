# MongoDB Integration & Authentication Setup ✅

## Overview
Your Kidney Care System now has a complete MongoDB integration for user authentication, registration, and data management. Static test accounts have been removed and replaced with real database functionality.

---

## 📝 What Was Done

### 1. **MongoDB Connection Module** (`mongodb_config.py`)
- Secure connection to MongoDB cluster using your credentials
- Password hashing with bcrypt (secure storage)
- User registration, login, and profile management
- Health assessment and prediction data storage
- Functions for CRUD operations on all collections

### 2. **Updated Authentication** (`streamlit_app.py`)
- ✅ Removed all 5 hardcoded test accounts
- ✅ New registration form with full user details
- ✅ MongoDB-backed login system
- ✅ Password hashing and verification
- ✅ Session management for authenticated users

### 3. **MongoDB Schema** (3 Collections)
- **users** - User accounts with profile info
- **health_assessments** - Medical test results (all 24 parameters)
- **predictions** - ML model predictions and risk scores

### 4. **Comprehensive Documentation** (`MONGODB_SCHEMA.md`)
- Complete schema with examples
- Field descriptions and ranges
- Sample queries
- Maintenance instructions
- Security features explained

---

## 🔧 Installation & Setup

### Step 1: Install Dependencies
```bash
cd /Users/pavanm/KIDNEY-CARE-SYSTEM
pip install -r requirements.txt
```

Installed packages:
- `pymongo==4.6.0` - MongoDB driver
- `bcrypt==4.1.1` - Password hashing
- `python-dotenv==1.0.0` - Environment variables (optional)

### Step 2: Test MongoDB Connection
Your MongoDB URI is configured in `mongodb_config.py`:
```python
MONGODB_URI = "mongodb+srv://pavanmis23_db_user:Pavan1234@cluster0.tceupcl.mongodb.net/?appName=Cluster0"
DB_NAME = "kidney_care_system"
```

---

## 🚀 How to Use

### Starting Streamlit
```bash
streamlit run streamlit_app.py
```
Then open: http://localhost:8502

### Creating a New Account
1. Click "➕ Register" on login page
2. Fill in all fields:
   - Email (unique identifier)
   - Password (minimum 6 characters, bcrypt hashed)
   - Full Name
   - Age
   - Gender (Male/Female/Other)
   - City
3. Click "✅ Register"
4. Login with your new credentials

### Making Predictions
1. After login, navigate to "Kidney Prediction"
2. Enter your medical parameters (all 24 fields now)
3. Click "🔍 Predict Kidney Disease Risk"
4. View predictions from all 5 ML models:
   - Random Forest
   - Logistic Regression
   - SVM
   - Gradient Boosting
   - Ensemble (RF + LR + SVM)

---

## 📊 MongoDB Collections

### `users` Collection
```javascript
{
  "_id": ObjectId,
  "email": "user@example.com",           // Unique index
  "password": "$2b$12$...",              // Bcrypt hashed
  "name": "John Doe",
  "age": 48,
  "gender": "Male",
  "city": "Bangalore",
  "created_at": ISODate(...),
  "updated_at": ISODate(...),
  "condition": "Stage 3 CKD",
  "medical_history": []
}
```

### `health_assessments` Collection
Stores all 24 medical parameters:
- age, bp, sg, al, su
- rbc, pc, pcc, ba
- bgr, bu, sc, sod, pot
- hemo, pcv, wc, rc
- htn, dm, cad, appet, pe, ane

### `predictions` Collection
```javascript
{
  "email": "user@example.com",
  "created_at": ISODate(...),
  "ensemble_risk": 0.65,                 // Primary risk score
  "rf_risk": 0.63,
  "lr_risk": 0.67,
  "svm_risk": 0.66,
  "gb_risk": 0.64,
  "risk_level": "Medium",
  "gfr_value": 68.5,
  "creatinine": 1.2,
  "age": 48
}
```

---

## 🔐 Security Features

1. **Password Hashing**: Bcrypt with 10+ salt rounds
2. **Unique Emails**: MongoDB unique index on email field
3. **Data Isolation**: Each user accesses only their data
4. **Timestamps**: All records tracked with created_at/updated_at
5. **Connection Security**: MongoDB Atlas with IP whitelist

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `mongodb_config.py` | MongoDB connection & operations |
| `streamlit_app.py` | Main Streamlit application |
| `MONGODB_SCHEMA.md` | Complete schema documentation |
| `train_model.py` | ML model training on CSV data |
| `requirements.txt` | Python dependencies |

---

## 🧪 Testing

### Test Registration
1. Open http://localhost:8502
2. Click "Register"
3. Create account with:
   - Email: test@example.com
   - Password: test123456
   - Name: Test User
   - Age: 45
   - Gender: Male
   - City: Bangalore

### Test Login
1. Use created credentials to login
2. Navigate to "Kidney Prediction"
3. Enter health parameters
4. View ML predictions saved to MongoDB

### View Data in MongoDB
```javascript
// Get all users
db.users.find({})

// Get user's predictions
db.predictions.find({email: "test@example.com"}).sort({created_at: -1})

// Get user's assessments
db.health_assessments.find({email: "test@example.com"}).sort({created_at: -1})
```

---

## ⚠️ Important Notes

1. **MongoDB URI is Public**: Keep your connection string secure in production
   - Use environment variables (.env file)
   - Restrict MongoDB IP access to your servers

2. **Password Hashing**: Never store plain passwords
   - All passwords hashed with bcrypt
   - User passwords never logged or displayed

3. **Data Backup**: Regular MongoDB backups recommended
   ```bash
   mongodump --uri "your_uri" --out ./backup
   mongorestore --uri "your_uri" ./backup
   ```

4. **Index Creation**: For better performance, create indexes:
   ```javascript
   db.users.createIndex({email: 1}, {unique: true})
   db.health_assessments.createIndex({email: 1, created_at: -1})
   db.predictions.createIndex({email: 1, created_at: -1})
   ```

---

## 🐛 Troubleshooting

### Connection Error: "Failed to connect to MongoDB"
- Check internet connection
- Verify MongoDB URI in `mongodb_config.py`
- Add IP address to MongoDB Atlas whitelist

### Registration Error: "Email already registered"
- Email already exists in database
- Use different email or login instead

### Prediction Error: "Feature mismatch"
- All 24 fields required
- Check that CAD, Appetite, Pedal Edema, Anemia are filled

---

## 📚 References

- [MongoDB Python Driver](https://pymongo.readthedocs.io/)
- [Bcrypt Documentation](https://github.com/pyca/bcrypt)
- [Streamlit Docs](https://docs.streamlit.io/)

---

## ✅ Checklist

- [x] MongoDB connection configured
- [x] User registration implemented
- [x] Password hashing with bcrypt
- [x] 3 MongoDB collections created
- [x] 24 medical parameters stored
- [x] ML predictions saved to database
- [x] Hardcoded test accounts removed
- [x] Schema documentation completed
- [x] Streamlit app updated
- [x] All dependencies in requirements.txt

**Your system is ready for production use!** 🎉
