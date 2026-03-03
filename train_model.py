import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Generate synthetic kidney disease dataset based on medical research
np.random.seed(42)
n_samples = 1000

# Generate features
data = {
    'age': np.random.randint(20, 90, n_samples),
    'bp': np.random.randint(60, 180, n_samples),
    'sg': np.random.choice([1.005, 1.010, 1.015, 1.020, 1.025], n_samples),
    'al': np.random.choice([0, 1, 2, 3, 4, 5], n_samples),
    'su': np.random.choice([0, 1, 2, 3, 4, 5], n_samples),
    'rbc': np.random.choice([0, 1], n_samples),
    'pc': np.random.choice([0, 1], n_samples),
    'pcc': np.random.choice([0, 1], n_samples),
    'ba': np.random.choice([0, 1], n_samples),
    'bgr': np.random.randint(70, 400, n_samples),
    'bu': np.random.randint(15, 150, n_samples),
    'sc': np.random.uniform(0.4, 10.0, n_samples),
    'sod': np.random.randint(120, 160, n_samples),
    'pot': np.random.uniform(2.5, 7.5, n_samples),
    'hemo': np.random.uniform(6.0, 17.0, n_samples),
    'pcv': np.random.randint(25, 55, n_samples),
    'wc': np.random.randint(3000, 15000, n_samples),
    'rc': np.random.uniform(2.5, 7.0, n_samples),
    'htn': np.random.choice([0, 1], n_samples),
    'dm': np.random.choice([0, 1], n_samples)
}

df = pd.DataFrame(data)

# Create target based on medical indicators
def create_target(row):
    risk = 0
    if row['sc'] > 1.5: risk += 3
    if row['bu'] > 50: risk += 2
    if row['hemo'] < 12: risk += 2
    if row['htn'] == 1: risk += 2
    if row['dm'] == 1: risk += 2
    if row['al'] > 2: risk += 1
    if row['bgr'] > 150: risk += 1
    if row['pcv'] < 35: risk += 1
    if row['pot'] > 5.5 or row['pot'] < 3.5: risk += 1
    if row['rbc'] == 1: risk += 1
    if row['age'] > 60: risk += 1
    if row['bp'] > 140: risk += 1
    
    return 1 if risk >= 5 else 0

df['target'] = df.apply(create_target, axis=1)

# Split features and target
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Train Gradient Boosting
gb_model = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
gb_model.fit(X_train_scaled, y_train)

# Save models
with open('kidney_rf_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

with open('kidney_gb_model.pkl', 'wb') as f:
    pickle.dump(gb_model, f)

with open('kidney_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Models trained and saved successfully!")
print(f"Random Forest Accuracy: {rf_model.score(X_test_scaled, y_test):.2f}")
print(f"Gradient Boosting Accuracy: {gb_model.score(X_test_scaled, y_test):.2f}")
