import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Activity, LayoutDashboard, User, ClipboardList, Pill, Calendar, Utensils, FileText, Brain, Phone, LogOut, Menu, X } from 'lucide-react';
import './Layout.css';

const Layout = ({ children, setAuth }) => {
  const location = useLocation();
  const navigate = useNavigate();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const menuItems = [
    { path: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
    { path: '/profile', icon: User, label: 'Profile' },
    { path: '/assessment', icon: ClipboardList, label: 'Health Assessment' },
    { path: '/medications', icon: Pill, label: 'Medications' },
    { path: '/appointments', icon: Calendar, label: 'Appointments' },
    { path: '/diet', icon: Utensils, label: 'Diet Plan' },
    { path: '/lab-reports', icon: FileText, label: 'Lab Reports' },
    { path: '/ai-insights', icon: Brain, label: 'AI Insights' },
    { path: '/emergency', icon: Phone, label: 'Emergency' }
  ];

  const handleLogout = () => {
    setAuth(false);
    navigate('/login');
  };

  return (
    <div className="layout">
      <aside className={`sidebar ${sidebarOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <Activity size={32} color="#4f46e5" />
          <h2>Kidney Care</h2>
          <button className="close-btn" onClick={() => setSidebarOpen(false)}><X size={24} /></button>
        </div>
        <nav className="sidebar-nav">
          {menuItems.map(item => (
            <Link key={item.path} to={item.path} className={`nav-item ${location.pathname === item.path ? 'active' : ''}`} onClick={() => setSidebarOpen(false)}>
              <item.icon size={20} />
              <span>{item.label}</span>
            </Link>
          ))}
        </nav>
        <button className="logout-btn" onClick={handleLogout}>
          <LogOut size={20} />
          <span>Logout</span>
        </button>
      </aside>
      <div className="main-content">
        <header className="top-header">
          <button className="menu-btn" onClick={() => setSidebarOpen(true)}><Menu size={24} /></button>
          <h1>AI-Driven Kidney Care System</h1>
        </header>
        <main className="content">{children}</main>
      </div>
      {sidebarOpen && <div className="overlay" onClick={() => setSidebarOpen(false)}></div>}
    </div>
  );
};

export default Layout;
