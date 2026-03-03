import React, { useState } from 'react';
import { Phone, Plus, Edit2, Trash2 } from 'lucide-react';
import './EmergencyContacts.css';

const EmergencyContacts = () => {
  const [contacts] = useState([
    { id: 1, name: 'Dr. Sarah Johnson', role: 'Primary Nephrologist', phone: '+1 234 567 8900', available: '24/7' },
    { id: 2, name: 'City Hospital ER', role: 'Emergency Room', phone: '+1 234 567 8901', available: '24/7' },
    { id: 3, name: 'Jane Doe', role: 'Family Contact', phone: '+1 234 567 8902', available: 'Always' },
    { id: 4, name: 'Dialysis Center', role: 'Treatment Center', phone: '+1 234 567 8903', available: 'Mon-Sat 8AM-8PM' }
  ]);

  return (
    <div className="emergency-contacts">
      <div className="emergency-header">
        <Phone size={32} color="#dc2626" />
        <h2>Emergency Contacts</h2>
        <p>Quick access to important medical contacts</p>
      </div>

      <div className="alert-banner">
        <p>In case of severe emergency, call 911 immediately</p>
      </div>

      <button className="btn-add-contact">
        <Plus size={20} /> Add Contact
      </button>

      <div className="contacts-list">
        {contacts.map(contact => (
          <div key={contact.id} className="contact-card">
            <div className="contact-icon">
              <Phone size={24} />
            </div>
            <div className="contact-info">
              <h3>{contact.name}</h3>
              <p className="role">{contact.role}</p>
              <p className="phone">{contact.phone}</p>
              <p className="available">Available: {contact.available}</p>
            </div>
            <div className="contact-actions">
              <button className="btn-call">Call</button>
              <button className="btn-edit-contact"><Edit2 size={16} /></button>
              <button className="btn-delete"><Trash2 size={16} /></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EmergencyContacts;
