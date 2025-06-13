# 🏠 House Price Prediction using Linear Regression

This is a Flask-based web application that predicts house prices based on user inputs. The model is trained using Linear Regression on the Boston Housing dataset.

---

## 🚀 Features

- Linear Regression model (scikit-learn)
- Flask backend with clean routing
- 13-input feature form (no derived inputs from user)
- Predicts median house value based on user inputs
- Scaler used for consistent preprocessing
- Responsive HTML + CSS frontend inside the templates folder

---

## 📁 Project Structure

```
.
├── house-price-prediction.ipynb     # Jupyter notebook for training and saving model
├── house-price-prediction.pkl       # Trained Linear Regression model
├── scaler.pkl                       # StandardScaler for input transformation
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to ignore in Git
├── app.py                           # Flask web server
└── templates/
    ├── index.html                   # HTML input form
    └── style.css                    # CSS for styling the form
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bhoomi1301/boston-price-predictor.git
cd your-repo-name
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Web App Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🧾 Input Features (13 required inputs)

User must provide values for the following features:

1. **CRIM** – Per capita crime rate
2. **ZN** – Proportion of residential land zoned
3. **INDUS** – Proportion of non-retail business acres
4. **CHAS** – Charles River dummy variable (0 or 1)
5. **NOX** – Nitric oxide concentration
6. **RM** – Average number of rooms
7. **AGE** – Proportion of older homes
8. **DIS** – Weighted distance to employment centers
9. **RAD** – Accessibility to radial highways
10. **TAX** – Property tax rate
11. **PTRATIO** – Pupil-teacher ratio
12. **B** – 1000(Bk - 0.63)^2 (where Bk is proportion of Black residents)
13. **LSTAT** – % lower status population

These values are scaled using a saved `StandardScaler` and passed to the trained Linear Regression model for prediction.

---

## 📊 Model Performance

- **Model**: Linear Regression
- **R² Score**: `0.8059`
- **MAE**: `~3.19`
- **RMSE**: `~4.93`

---

## 🔧 Deployment Ready

You can deploy this app using:

- GitHub + Render / Railway / Heroku
- Add a `Procfile`, update `requirements.txt`, and push to your preferred platform

---

## 📝 Author

**Bhoomika N S**  
Built with ❤️ using Python, Flask, and scikit-learn.

---

## 📜 License

Licensed under the MIT License.
