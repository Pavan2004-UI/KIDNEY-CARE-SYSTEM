import React, { useState } from 'react';
import { Pill, Plus, Clock, CheckCircle } from 'lucide-react';
import './Medications.css';

const Medications = () => {
  const [medications, setMedications] = useState([
    { id: 1, name: 'Lisinopril', dosage: '10mg', frequency: 'Once daily', time: '08:00 AM', taken: true },
    { id: 2, name: 'Furosemide', dosage: '40mg', frequency: 'Twice daily', time: '08:00 AM, 08:00 PM', taken: true },
    { id: 3, name: 'Calcium Carbonate', dosage: '500mg', frequency: 'Three times daily', time: '08:00 AM, 02:00 PM, 08:00 PM', taken: false }
  ]);

  const [showAdd, setShowAdd] = useState(false);

  const toggleTaken = (id) => {
    setMedications(medications.map(med => med.id === id ? {...med, taken: !med.taken} : med));
  };

  return (
    <div className="medications">
      <div className="medications-header">
        <h2>My Medications</h2>
        <button className="btn-add" onClick={() => setShowAdd(!showAdd)}>
          <Plus size={20} /> Add Medication
        </button>
      </div>

      {showAdd && (
        <div className="add-medication-card">
          <h3>Add New Medication</h3>
          <form className="medication-form">
            <input type="text" placeholder="Medication Name" />
            <input type="text" placeholder="Dosage (e.g., 10mg)" />
            <input type="text" placeholder="Frequency" />
            <input type="time" placeholder="Time" />
            <div className="form-actions">
              <button type="submit" className="btn-save">Save</button>
              <button type="button" className="btn-cancel" onClick={() => setShowAdd(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}

      <div className="medications-list">
        {medications.map(med => (
          <div key={med.id} className={`medication-card ${med.taken ? 'taken' : ''}`}>
            <div className="medication-icon">
              <Pill size={24} />
            </div>
            <div className="medication-info">
              <h3>{med.name}</h3>
              <p className="dosage">{med.dosage} - {med.frequency}</p>
              <p className="time"><Clock size={16} /> {med.time}</p>
            </div>
            <button className={`btn-check ${med.taken ? 'checked' : ''}`} onClick={() => toggleTaken(med.id)}>
              <CheckCircle size={24} />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Medications;
