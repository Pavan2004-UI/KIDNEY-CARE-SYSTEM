# AI-Driven Kidney Care System - Frontend

A comprehensive React-based frontend application for managing kidney health with AI-powered insights.

## Features

- **User Authentication**: Login and Registration
- **Dashboard**: Health metrics overview with charts
- **Profile Management**: Personal and medical information
- **Health Assessment**: Interactive kidney health questionnaire
- **Medication Tracker**: Track and manage medications
- **Appointment Scheduler**: View and manage appointments
- **Diet Plan**: Kidney-friendly nutrition recommendations
- **Lab Reports**: View and download medical reports
- **AI Insights**: AI-powered health predictions and recommendations
- **Emergency Contacts**: Quick access to important contacts

## Tech Stack

- React 18
- React Router DOM
- Recharts (for data visualization)
- Lucide React (for icons)
- CSS3 (responsive design)

## Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm start
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## Project Structure

```
src/
├── components/
│   ├── Auth/
│   │   ├── Login.js
│   │   ├── Register.js
│   │   └── Auth.css
│   ├── Layout/
│   │   ├── Layout.js
│   │   └── Layout.css
│   ├── Dashboard/
│   ├── Profile/
│   ├── HealthAssessment/
│   ├── Medications/
│   ├── Appointments/
│   ├── DietPlan/
│   ├── LabReports/
│   ├── AIInsights/
│   └── EmergencyContacts/
├── App.js
├── App.css
├── index.js
└── index.css
```

## Usage

1. Start by registering a new account or logging in
2. Navigate through different sections using the sidebar
3. View health metrics on the dashboard
4. Complete health assessments
5. Track medications and appointments
6. Access AI-powered insights and recommendations

## Streamlit Version

A Streamlit version is also available for quick deployment:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The Streamlit app will open at `http://localhost:8501`

**Login credentials:**
- john@email.com / password123
- sarah@email.com / sarah123
- mike@email.com / mike123
- emma@email.com / emma123
- admin@kidney.com / admin123

## Note

Both versions currently use static data. Backend integration will be required for production use.
