import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Dashboard from './components/Dashboard/Dashboard';
import Profile from './components/Profile/Profile';
import HealthAssessment from './components/HealthAssessment/HealthAssessment';
import Medications from './components/Medications/Medications';
import Appointments from './components/Appointments/Appointments';
import DietPlan from './components/DietPlan/DietPlan';
import LabReports from './components/LabReports/LabReports';
import AIInsights from './components/AIInsights/AIInsights';
import EmergencyContacts from './components/EmergencyContacts/EmergencyContacts';
import Layout from './components/Layout/Layout';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={!isAuthenticated ? <Login setAuth={setIsAuthenticated} /> : <Navigate to="/dashboard" />} />
          <Route path="/register" element={!isAuthenticated ? <Register setAuth={setIsAuthenticated} /> : <Navigate to="/dashboard" />} />
          <Route path="/" element={<Navigate to={isAuthenticated ? "/dashboard" : "/login"} />} />
          <Route path="/*" element={isAuthenticated ? <Layout setAuth={setIsAuthenticated}><Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/assessment" element={<HealthAssessment />} />
            <Route path="/medications" element={<Medications />} />
            <Route path="/appointments" element={<Appointments />} />
            <Route path="/diet" element={<DietPlan />} />
            <Route path="/lab-reports" element={<LabReports />} />
            <Route path="/ai-insights" element={<AIInsights />} />
            <Route path="/emergency" element={<EmergencyContacts />} />
          </Routes></Layout> : <Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
