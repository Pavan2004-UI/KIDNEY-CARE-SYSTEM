import React from 'react';
import { Brain, TrendingUp, AlertTriangle, CheckCircle, Lightbulb } from 'lucide-react';
import './AIInsights.css';

const AIInsights = () => {
  const insights = [
    { type: 'warning', icon: AlertTriangle, title: 'GFR Declining Trend', message: 'Your GFR has decreased by 5% over the last 3 months. Consider discussing treatment adjustments with your doctor.' },
    { type: 'success', icon: CheckCircle, title: 'Excellent Medication Adherence', message: 'You have maintained 95% medication adherence this month. Keep up the great work!' },
    { type: 'info', icon: Lightbulb, title: 'Hydration Recommendation', message: 'Based on your recent lab results, increasing water intake to 2L per day may help improve kidney function.' }
  ];

  const predictions = [
    { metric: 'GFR Level', current: 68, predicted: 66, trend: 'down', timeframe: '3 months' },
    { metric: 'Blood Pressure', current: '128/82', predicted: '125/80', trend: 'up', timeframe: '1 month' },
    { metric: 'Creatinine', current: 1.4, predicted: 1.5, trend: 'down', timeframe: '2 months' }
  ];

  return (
    <div className="ai-insights">
      <div className="insights-header">
        <Brain size={32} color="#4f46e5" />
        <h2>AI Health Insights</h2>
        <p>Personalized recommendations powered by artificial intelligence</p>
      </div>

      <div className="insights-grid">
        {insights.map((insight, idx) => (
          <div key={idx} className={`insight-card ${insight.type}`}>
            <div className="insight-icon">
              <insight.icon size={24} />
            </div>
            <div className="insight-content">
              <h3>{insight.title}</h3>
              <p>{insight.message}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="predictions-card">
        <h3><TrendingUp size={24} /> Health Predictions</h3>
        <p className="predictions-subtitle">AI-powered forecasts based on your health trends</p>
        <div className="predictions-list">
          {predictions.map((pred, idx) => (
            <div key={idx} className="prediction-item">
              <div className="prediction-header">
                <h4>{pred.metric}</h4>
                <span className={`trend-badge ${pred.trend}`}>{pred.trend === 'up' ? '↑' : '↓'}</span>
              </div>
              <div className="prediction-values">
                <div className="value-item">
                  <span className="label">Current</span>
                  <span className="value">{pred.current}</span>
                </div>
                <div className="arrow">→</div>
                <div className="value-item">
                  <span className="label">Predicted ({pred.timeframe})</span>
                  <span className="value">{pred.predicted}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AIInsights;
