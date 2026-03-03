import React, { useState } from 'react';
import { User, Mail, Phone, Calendar, MapPin, Edit2, Save } from 'lucide-react';
import './Profile.css';

const Profile = () => {
  const [editing, setEditing] = useState(false);
  const [profile, setProfile] = useState({
    name: 'John Doe',
    email: 'john.doe@email.com',
    phone: '+1 234 567 8900',
    dob: '1975-05-15',
    address: '123 Main St, New York, NY 10001',
    bloodType: 'O+',
    height: '175',
    weight: '78',
    emergencyContact: 'Jane Doe - +1 234 567 8901'
  });

  return (
    <div className="profile">
      <div className="profile-header">
        <h2>My Profile</h2>
        <button className="btn-edit" onClick={() => setEditing(!editing)}>
          {editing ? <><Save size={20} /> Save</> : <><Edit2 size={20} /> Edit</>}
        </button>
      </div>

      <div className="profile-content">
        <div className="profile-card">
          <div className="profile-avatar">
            <User size={64} />
          </div>
          <h3>{profile.name}</h3>
          <p>{profile.email}</p>
        </div>

        <div className="profile-details">
          <h3>Personal Information</h3>
          <div className="details-grid">
            <div className="detail-item">
              <Mail size={20} />
              <div>
                <label>Email</label>
                {editing ? <input value={profile.email} onChange={(e) => setProfile({...profile, email: e.target.value})} /> : <p>{profile.email}</p>}
              </div>
            </div>
            <div className="detail-item">
              <Phone size={20} />
              <div>
                <label>Phone</label>
                {editing ? <input value={profile.phone} onChange={(e) => setProfile({...profile, phone: e.target.value})} /> : <p>{profile.phone}</p>}
              </div>
            </div>
            <div className="detail-item">
              <Calendar size={20} />
              <div>
                <label>Date of Birth</label>
                {editing ? <input type="date" value={profile.dob} onChange={(e) => setProfile({...profile, dob: e.target.value})} /> : <p>{profile.dob}</p>}
              </div>
            </div>
            <div className="detail-item">
              <MapPin size={20} />
              <div>
                <label>Address</label>
                {editing ? <input value={profile.address} onChange={(e) => setProfile({...profile, address: e.target.value})} /> : <p>{profile.address}</p>}
              </div>
            </div>
          </div>
        </div>

        <div className="profile-details">
          <h3>Medical Information</h3>
          <div className="details-grid">
            <div className="detail-item">
              <div>
                <label>Blood Type</label>
                {editing ? <input value={profile.bloodType} onChange={(e) => setProfile({...profile, bloodType: e.target.value})} /> : <p>{profile.bloodType}</p>}
              </div>
            </div>
            <div className="detail-item">
              <div>
                <label>Height (cm)</label>
                {editing ? <input value={profile.height} onChange={(e) => setProfile({...profile, height: e.target.value})} /> : <p>{profile.height}</p>}
              </div>
            </div>
            <div className="detail-item">
              <div>
                <label>Weight (kg)</label>
                {editing ? <input value={profile.weight} onChange={(e) => setProfile({...profile, weight: e.target.value})} /> : <p>{profile.weight}</p>}
              </div>
            </div>
            <div className="detail-item">
              <div>
                <label>Emergency Contact</label>
                {editing ? <input value={profile.emergencyContact} onChange={(e) => setProfile({...profile, emergencyContact: e.target.value})} /> : <p>{profile.emergencyContact}</p>}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
