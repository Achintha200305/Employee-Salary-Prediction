# 💼 Employee Salary Prediction App

A Machine Learning web application built using **Multiple Linear Regression** and **Streamlit** to predict monthly employee salaries (in LKR) based on work experience, education level, skill score, and age.

## 🚀 Features
- **Feature Engineering:** Converts work experience into total months (`Years * 12 + Months`) for accurate predictions.
- **Interactive UI:** Built with Streamlit allowing users to adjust inputs easily.
- **Real-time Prediction:** Uses a pre-trained Scikit-Learn Linear Regression model (`R² Score: 1.0`).

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-Learn
- Streamlit
- Joblib

## 💻 How to Run Locally
1. Clone this repository:
   ```bash
  git clone https://github.com/Achintha200305/Employee-Salary-Prediction.git
  ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   python -m streamlit run app.py
   ```
