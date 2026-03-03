import React, { useState } from 'react';
import { ClipboardList, AlertCircle } from 'lucide-react';
import './HealthAssessment.css';

const HealthAssessment = () => {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const questions = [
    { id: 1, text: 'Do you experience frequent urination?', type: 'radio', options: ['Yes', 'No', 'Sometimes'] },
    { id: 2, text: 'Have you noticed swelling in your legs or ankles?', type: 'radio', options: ['Yes', 'No', 'Sometimes'] },
    { id: 3, text: 'Do you feel fatigued or weak regularly?', type: 'radio', options: ['Yes', 'No', 'Sometimes'] },
    { id: 4, text: 'Have you experienced changes in urine color?', type: 'radio', options: ['Yes', 'No', 'Not Sure'] },
    { id: 5, text: 'Do you have difficulty sleeping?', type: 'radio', options: ['Yes', 'No', 'Sometimes'] },
    { id: 6, text: 'Rate your overall pain level (0-10)', type: 'range', min: 0, max: 10 }
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="health-assessment">
      <div className="assessment-header">
        <ClipboardList size={32} color="#4f46e5" />
        <h2>Kidney Health Assessment</h2>
        <p>Answer these questions to help us understand your current health status</p>
      </div>

      {!submitted ? (
        <form onSubmit={handleSubmit} className="assessment-form">
          {questions.map(q => (
            <div key={q.id} className="question-card">
              <h3>{q.text}</h3>
              {q.type === 'radio' ? (
                <div className="radio-group">
                  {q.options.map(opt => (
                    <label key={opt}>
                      <input type="radio" name={`q${q.id}`} value={opt} onChange={(e) => setAnswers({...answers, [q.id]: e.target.value})} />
                      <span>{opt}</span>
                    </label>
                  ))}
                </div>
              ) : (
                <div className="range-group">
                  <input type="range" min={q.min} max={q.max} value={answers[q.id] || 0} onChange={(e) => setAnswers({...answers, [q.id]: e.target.value})} />
                  <span className="range-value">{answers[q.id] || 0}</span>
                </div>
              )}
            </div>
          ))}
          <button type="submit" className="btn-submit">Submit Assessment</button>
        </form>
      ) : (
        <div className="assessment-result">
          <div className="result-card">
            <AlertCircle size={48} color="#f59e0b" />
            <h3>Assessment Complete</h3>
            <p>Based on your responses, we recommend scheduling a consultation with your nephrologist. Your responses indicate some symptoms that should be monitored.</p>
            <div className="result-actions">
              <button className="btn-primary" onClick={() => setSubmitted(false)}>Retake Assessment</button>
              <button className="btn-secondary">Schedule Appointment</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HealthAssessment;
