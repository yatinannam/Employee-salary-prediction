# 🧠 Employee Salary Prediction App

This project is a **Streamlit web app** that predicts whether an employee earns more than \$50K per year based on demographic data, using a **Random Forest Classifier** trained on the UCI Adult Income dataset (`adult.csv`).

---

## 🚀 Live Demo

🔗 [Click here to try the app](https://employee-salary-prediction-cnwpsq48hihfu2ers6avs5.streamlit.app/)

---

## 📊 Features

- User-friendly **Streamlit interface**
- Model trained using **Random Forest**
- Label encoding and preprocessing of categorical variables
- Input via **interactive form**
- Live prediction: `<=50K` or `>50K` income
- Deployed on **Streamlit Cloud**

---

## 📌 Input Features

- Age
- Workclass
- FNLWGT
- Education
- Educational Number
- Marital Status
- Occupation
- Relationship
- Race
- Gender
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country

---

## 🛠️ Technologies Used

- Python
- pandas, numpy, scikit-learn
- Streamlit
- joblib
- Google Colab for training
- GitHub for version control
- Streamlit Cloud for deployment

---

## 📦 Installation (Optional for Local Use)

```bash
git clone https://github.com/yourusername/employee-salary-prediction.git
cd employee-salary-prediction
pip install -r requirements.txt
streamlit run app.py
