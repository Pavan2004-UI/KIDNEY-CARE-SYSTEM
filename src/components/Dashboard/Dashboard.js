import React from 'react';
import { Activity, Droplet, Heart, TrendingUp, AlertCircle, CheckCircle } from 'lucide-react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import './Dashboard.css';

const Dashboard = () => {
  const healthMetrics = [
    { label: 'GFR Level', value: '68', unit: 'mL/min', status: 'warning', icon: Activity },
    { label: 'Creatinine', value: '1.4', unit: 'mg/dL', status: 'normal', icon: Droplet },
    { label: 'Blood Pressure', value: '128/82', unit: 'mmHg', status: 'normal', icon: Heart },
    { label: 'Protein in Urine', value: '150', unit: 'mg/day', status: 'warning', icon: TrendingUp }
  ];

  const gfrData = [
    { month: 'Jan', value: 72 },
    { month: 'Feb', value: 70 },
    { month: 'Mar', value: 69 },
    { month: 'Apr', value: 68 },
    { month: 'May', value: 68 },
    { month: 'Jun', value: 68 }
  ];

  const medicationData = [
    { day: 'Mon', taken: 3 },
    { day: 'Tue', taken: 3 },
    { day: 'Wed', taken: 2 },
    { day: 'Thu', taken: 3 },
    { day: 'Fri', taken: 3 },
    { day: 'Sat', taken: 3 },
    { day: 'Sun', taken: 3 }
  ];

  const upcomingAppointments = [
    { date: '2024-01-15', doctor: 'Dr. Sarah Johnson', type: 'Nephrology Checkup' },
    { date: '2024-01-22', doctor: 'Dr. Michael Chen', type: 'Lab Tests' }
  ];

  const recentAlerts = [
    { type: 'warning', message: 'GFR level slightly decreased', time: '2 hours ago' },
    { type: 'success', message: 'All medications taken today', time: '5 hours ago' }
  ];

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h2>Welcome back, John!</h2>
        <p>Here's your kidney health overview</p>
      </div>

      <div className="metrics-grid">
        {healthMetrics.map((metric, idx) => (
          <div key={idx} className={`metric-card ${metric.status}`}>
            <div className="metric-icon">
              <metric.icon size={24} />
            </div>
            <div className="metric-info">
              <p className="metric-label">{metric.label}</p>
              <h3 className="metric-value">{metric.value} <span>{metric.unit}</span></h3>
            </div>
          </div>
        ))}
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <h3>GFR Trend (Last 6 Months)</h3>
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={gfrData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="value" stroke="#4f46e5" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h3>Medication Adherence (This Week)</h3>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={medicationData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="taken" fill="#10b981" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="info-grid">
        <div className="info-card">
          <h3>Upcoming Appointments</h3>
          <div className="appointments-list">
            {upcomingAppointments.map((apt, idx) => (
              <div key={idx} className="appointment-item">
                <div className="appointment-date">{apt.date}</div>
                <div className="appointment-details">
                  <p className="appointment-doctor">{apt.doctor}</p>
                  <p className="appointment-type">{apt.type}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="info-card">
          <h3>Recent Alerts</h3>
          <div className="alerts-list">
            {recentAlerts.map((alert, idx) => (
              <div key={idx} className={`alert-item ${alert.type}`}>
                {alert.type === 'warning' ? <AlertCircle size={20} /> : <CheckCircle size={20} />}
                <div className="alert-content">
                  <p className="alert-message">{alert.message}</p>
                  <p className="alert-time">{alert.time}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
