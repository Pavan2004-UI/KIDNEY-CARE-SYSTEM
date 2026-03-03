import React, { useState } from 'react';
import { Calendar, Plus, Clock, MapPin } from 'lucide-react';
import './Appointments.css';

const Appointments = () => {
  const [appointments] = useState([
    { id: 1, date: '2024-01-15', time: '10:00 AM', doctor: 'Dr. Sarah Johnson', specialty: 'Nephrologist', location: 'City Hospital, Room 302', status: 'upcoming' },
    { id: 2, date: '2024-01-22', time: '02:30 PM', doctor: 'Dr. Michael Chen', specialty: 'Lab Specialist', location: 'Medical Center, Lab 2', status: 'upcoming' },
    { id: 3, date: '2023-12-20', time: '11:00 AM', doctor: 'Dr. Sarah Johnson', specialty: 'Nephrologist', location: 'City Hospital, Room 302', status: 'completed' }
  ]);

  return (
    <div className="appointments">
      <div className="appointments-header">
        <h2>My Appointments</h2>
        <button className="btn-add"><Plus size={20} /> Book Appointment</button>
      </div>

      <div className="appointments-list">
        {appointments.filter(a => a.status === 'upcoming').map(apt => (
          <div key={apt.id} className="appointment-card upcoming">
            <div className="appointment-date-badge">
              <Calendar size={24} />
              <div>
                <p className="date">{apt.date}</p>
                <p className="time"><Clock size={14} /> {apt.time}</p>
              </div>
            </div>
            <div className="appointment-details">
              <h3>{apt.doctor}</h3>
              <p className="specialty">{apt.specialty}</p>
              <p className="location"><MapPin size={16} /> {apt.location}</p>
            </div>
            <div className="appointment-actions">
              <button className="btn-reschedule">Reschedule</button>
              <button className="btn-cancel">Cancel</button>
            </div>
          </div>
        ))}
      </div>

      <h3 className="section-title">Past Appointments</h3>
      <div className="appointments-list">
        {appointments.filter(a => a.status === 'completed').map(apt => (
          <div key={apt.id} className="appointment-card completed">
            <div className="appointment-date-badge">
              <Calendar size={24} />
              <div>
                <p className="date">{apt.date}</p>
                <p className="time"><Clock size={14} /> {apt.time}</p>
              </div>
            </div>
            <div className="appointment-details">
              <h3>{apt.doctor}</h3>
              <p className="specialty">{apt.specialty}</p>
              <p className="location"><MapPin size={16} /> {apt.location}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Appointments;
