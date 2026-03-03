import React from 'react';
import { Utensils, CheckCircle, XCircle } from 'lucide-react';
import './DietPlan.css';

const DietPlan = () => {
  const recommended = [
    { name: 'Cauliflower', benefit: 'Low in potassium' },
    { name: 'Blueberries', benefit: 'Rich in antioxidants' },
    { name: 'Fish', benefit: 'High-quality protein' },
    { name: 'Egg Whites', benefit: 'Pure protein source' },
    { name: 'Olive Oil', benefit: 'Healthy fats' },
    { name: 'Cabbage', benefit: 'Low in potassium' }
  ];

  const avoid = [
    { name: 'Bananas', reason: 'High in potassium' },
    { name: 'Processed Meats', reason: 'High in sodium' },
    { name: 'Dairy Products', reason: 'High in phosphorus' },
    { name: 'Dark Sodas', reason: 'High in phosphorus' }
  ];

  const mealPlan = [
    { meal: 'Breakfast', items: ['Egg white omelet', 'Whole grain toast', 'Blueberries'] },
    { meal: 'Lunch', items: ['Grilled fish', 'Cauliflower rice', 'Green salad'] },
    { meal: 'Dinner', items: ['Chicken breast', 'Steamed vegetables', 'Quinoa'] },
    { meal: 'Snacks', items: ['Apple slices', 'Unsalted crackers', 'Cucumber'] }
  ];

  return (
    <div className="diet-plan">
      <div className="diet-header">
        <Utensils size={32} color="#4f46e5" />
        <h2>Kidney-Friendly Diet Plan</h2>
        <p>Personalized nutrition recommendations for optimal kidney health</p>
      </div>

      <div className="diet-grid">
        <div className="diet-card recommended">
          <h3><CheckCircle size={24} /> Recommended Foods</h3>
          <div className="food-list">
            {recommended.map((food, idx) => (
              <div key={idx} className="food-item">
                <h4>{food.name}</h4>
                <p>{food.benefit}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="diet-card avoid">
          <h3><XCircle size={24} /> Foods to Avoid</h3>
          <div className="food-list">
            {avoid.map((food, idx) => (
              <div key={idx} className="food-item">
                <h4>{food.name}</h4>
                <p>{food.reason}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="meal-plan-card">
        <h3>Daily Meal Plan</h3>
        <div className="meal-grid">
          {mealPlan.map((meal, idx) => (
            <div key={idx} className="meal-item">
              <h4>{meal.meal}</h4>
              <ul>
                {meal.items.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default DietPlan;
