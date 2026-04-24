# AI-Driven Kidney Care System - Copilot Instructions

## Project Overview

This is a dual-stack kidney health management application with a **React 18 frontend** and a **Streamlit Python backend** for ML model predictions. The system helps patients monitor kidney function through health metrics, AI insights, and medical record management.

### Tech Stack
- **Frontend**: React 18, React Router, Recharts (visualizations), Lucide React (icons), CSS3
- **Backend/Dashboard**: Streamlit with scikit-learn ML models (Random Forest, Gradient Boosting, SVM, Ensemble)
- **Key Dependencies**: `recharts`, `lucide-react`, `react-router-dom`

---

## Architecture & Key Patterns

### Authentication & Routing
- **Single-state auth** in `App.js`: `isAuthenticated` boolean drives all routing logic
- Public routes: `/login`, `/register`
- Protected routes: All dashboard routes wrapped in `<Layout>` component that receives `setAuth` callback
- Login currently validates hardcoded credentials; production needs backend integration

### Component Structure
All UI components live in `src/components/` with paired `.js` and `.css` files:
- **Auth/** - Login/Register forms with email/password validation
- **Layout/** - Sidebar navigation wrapper (passes `setAuth` to children, manages mobile hamburger menu)
- **Dashboard/** - Health metrics cards with color-coded status badges (normal/warning), Recharts line/bar charts
- **AIInsights/** - ML prediction display with trend indicators (↑/↓)
- Other components follow same pattern: local state, hardcoded data, chart/grid layouts

### Data & State Management
- **No global state library** - components use local `useState` only
- All mock data is **hardcoded** in React components
- **CSV Data Integration**: `kidney_disease.csv` (400 records) is used to train ML models via `train_model.py`
- Models trained: Random Forest, Logistic Regression, SVM, Gradient Boosting, and Ensemble (RF+LR)
- Streamlit app loads all 5 trained models (`.pkl` files) and uses them for predictions
- Status badges use CSS classes: `.normal` (green), `.warning` (amber), `.success` (green)
- Health metrics structure: `{ label, value, unit, status, icon }`

### Styling Convention
- **CSS modules pattern**: Each component has colocated `.css` file
- **Color scheme**: Primary indigo (`#4f46e5`), warnings/amber (`#f59e0b`), success green (`#10b981`), grays (`#1f2937`, `#6b7280`)
- **Responsive grids**: `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))` for metric cards; minmax adjusts per component
- CSS is **minified/compressed** - expand files carefully when reading

---

## Critical Workflows

### Starting Development
```bash
npm install          # Install React dependencies
npm start            # Runs on http://localhost:3000 (auto-reload)
npm build            # Production build to public/
```

### Running ML Dashboard (Optional)
```bash
cd KIDNEY-CARE-SYSTEM
python3 train_model.py    # Trains all 5 models on kidney_disease.csv, saves as .pkl files
pip install -r requirements.txt
streamlit run streamlit_app.py  # Opens http://localhost:8501
```

The training script loads `kidney_disease.csv`, preprocesses missing values, encodes categorical features, and trains all models with ~98-99% test accuracy. The Streamlit app loads all trained models and displays predictions from each model plus ensemble predictions.

**Predefined test users** (both React & Streamlit):
- john@email.com / password123
- sarah@email.com / sarah123
- mike@email.com / mike123
- admin@kidney.com / admin123

---

## Project-Specific Patterns

### Metric Card Pattern
Health metrics throughout the app use this structure:
```javascript
const healthMetrics = [
  { label: 'GFR Level', value: '68', unit: 'mL/min', status: 'warning', icon: Activity }
];
// Rendered with CSS classes: metric-card, metric-card.warning
```
Status determines border-left color and icon background. Always include `icon` as Lucide component reference.

### Chart Data Format
Recharts uses simple array-of-objects format:
```javascript
const gfrData = [
  { month: 'Jan', value: 72 },  // For LineChart
  { day: 'Mon', taken: 3 }      // For BarChart
];
```
Charts wrapped in `ResponsiveContainer` for mobile responsiveness.

### Layout Sidebar Navigation
`menuItems` array in Layout.js defines all routes. Adding a new page requires:
1. Create component in `src/components/NewPage/`
2. Import in `App.js`
3. Add route in nested Routes
4. Add menu item object to Layout's `menuItems` array with path/icon/label

---

## File Location Reference

- **Main routing**: `src/App.js` - App-level authentication state and route setup
- **Layout wrapper**: `src/components/Layout/Layout.js` - Sidebar navigation, menuItems array
- **Dashboard example**: `src/components/Dashboard/Dashboard.js` - Shows metric cards + Recharts pattern
- **AI predictions**: `src/components/AIInsights/AIInsights.js` - Shows insight cards and prediction rendering
- **Styling reference**: `src/components/Dashboard/Dashboard.css` - Color/grid patterns
- **ML models** (Python): `streamlit_app.py` - Loads pickled sklearn models, gfr calculation, user DB

---

## Common Tasks

### Adding a New Health Metric
Modify Dashboard's `healthMetrics` array - add status-colored icon, follow metric card CSS conventions.


---

## Important Notes

- **No backend API yet** - all data is static; production requires server integration
- **Authentication is not real** - no password validation; just toggles `isAuthenticated` state
- **Mobile-first responsive**: Test media queries at `max-width: 768px`
- **Lucide icons**: Browse https://lucide.dev for available icons; pass size prop for scaling
