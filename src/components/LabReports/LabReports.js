import React from 'react';
import { FileText, Download, Eye } from 'lucide-react';
import './LabReports.css';

const LabReports = () => {
  const reports = [
    { id: 1, name: 'Kidney Function Test', date: '2024-01-10', doctor: 'Dr. Sarah Johnson', status: 'completed' },
    { id: 2, name: 'Blood Test - Complete Panel', date: '2024-01-10', doctor: 'Dr. Sarah Johnson', status: 'completed' },
    { id: 3, name: 'Urine Analysis', date: '2023-12-15', doctor: 'Dr. Michael Chen', status: 'completed' },
    { id: 4, name: 'GFR Test', date: '2023-11-20', doctor: 'Dr. Sarah Johnson', status: 'completed' }
  ];

  return (
    <div className="lab-reports">
      <div className="reports-header">
        <h2>Lab Reports</h2>
        <p>View and download your medical test results</p>
      </div>

      <div className="reports-list">
        {reports.map(report => (
          <div key={report.id} className="report-card">
            <div className="report-icon">
              <FileText size={32} />
            </div>
            <div className="report-info">
              <h3>{report.name}</h3>
              <p className="report-date">Date: {report.date}</p>
              <p className="report-doctor">Ordered by: {report.doctor}</p>
            </div>
            <div className="report-actions">
              <button className="btn-view"><Eye size={18} /> View</button>
              <button className="btn-download"><Download size={18} /> Download</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default LabReports;
