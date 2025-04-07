# 🎓 Student Performance Prediction

📌 **Project Overview**

This project aims to predict whether a student will pass or fail based on various study habits and lifestyle factors. The model is trained using a dataset containing features such as study hours, attendance, internet usage, and more. A Streamlit app is built to allow users to interactively input data and get predictions.

🎯 **Objective**

The goal is to analyze key factors affecting student performance and build a predictive model that classifies outcomes as either "Pass" or "Fail."

📂 **Dataset Used**

**Features:**
- Gender  
- Age  
- Study Hours  
- Attendance  
- Sleep Hours  
- Internet Usage  
- Past Failures  
- Family Support  
- Extra Classes  
- Health Status  
- Travel Time  
- Daily Free Time  
- Workday Alcohol Consumption

**Target Variable:**  
- **Performance Outcome** (`Pass` / `Fail`)

🏆 **Model Chosen**

- **Logistic Regression**: Chosen for its simplicity and effectiveness in binary classification problems.
- **Random Forest Classifier (RFC)**: Added for comparison and performance tuning.

🔬 **Data Preprocessing**

- Handling Missing Values  
- Encoding Categorical Variables using `LabelEncoder`  
- Feature Scaling using `StandardScaler`  
- Train-Test Split (80% training, 20% testing)

📊 **Performance Metrics**

- Accuracy Score  
- Confusion Matrix  
- Classification Report (Precision, Recall, F1-Score)

🚀 **Deployment**

The model is deployed using **Streamlit**, offering an intuitive interface where users can input student-related information to receive a performance prediction.

🌍 **Live Demo**  
🚀 Check out the live Streamlit app: [Student Performance Predictor](https://your-streamlit-app-link)

---

## 💻 How to Run

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
pip install -r requirements.txt
streamlit run app.py

---

Project Structure
├── app.py                  # Streamlit app
├── model/                  # Saved models
├── src/                    # Preprocessing and ML code
├── requirements.txt        # Dependencies
├── LICENSE                 # Open-source license
├── README.md               # Project overview
└── docs/                   # Additional documentation

---


---

Let me know if you want this as a downloadable file or want me to auto-fill your GitHub username and Streamlit app link into it.

