import streamlit as st
import numpy as np
import joblib

# --- Set page config ---
st.set_page_config(page_title="🎓 Student Pass/Fail Predictor", page_icon="📘", layout="centered")

# --- Load model ---
model = joblib.load("../models/logistic_regression_model.pkl")
  # Make sure this is the correct path

# --- Title ---
st.markdown("<h1 style='text-align:center;'>🎓 Student Pass/Fail Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict if a student will pass or fail based on 13 input features using Machine Learning.</p>", unsafe_allow_html=True)
st.write("")

# --- Input Section ---
st.subheader("📥 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 Gender", ["female", "male"])
    race_ethnicity = st.selectbox("🧬 Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parent_edu = st.selectbox("🎓 Parental Level of Education", [
        "some high school", "high school", "some college", 
        "associate's degree", "bachelor's degree", "master's degree"
    ])
    lunch = st.selectbox("🍱 Lunch Type", ["standard", "free/reduced"])
    test_prep = st.selectbox("📝 Test Preparation", ["none", "completed"])
    study_time = st.slider("📖 Study Time (hrs/day)", 0.0, 10.0, 2.0, step=0.5)
    attendance = st.slider("📅 Attendance (%)", 0, 100, 85, step=1)

with col2:
    math_score = st.slider("➕ Math Score", 0, 100, 70)
    reading_score = st.slider("📖 Reading Score", 0, 100, 75)
    writing_score = st.slider("✍️ Writing Score", 0, 100, 72)
    past_failures = st.number_input("❌ Past Class Failures", 0, 5, 0)
    health = st.slider("❤️ Health (1 = Poor, 5 = Excellent)", 1, 5, 3)
    absences = st.number_input("🚫 Number of Absences", 0, 100, 5)

# --- Preprocessing ---
gender = 0 if gender == "female" else 1
race_map = {"group A": 0, "group B": 1, "group C": 2, "group D": 3, "group E": 4}
race = race_map[race_ethnicity]
edu_map = {
    "some high school": 0,
    "high school": 1,
    "some college": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}
edu_level = edu_map[parent_edu]
lunch = 1 if lunch == "standard" else 0
test_prep = 1 if test_prep == "completed" else 0

input_data = np.array([[gender, race, edu_level, lunch, test_prep,
                        math_score, reading_score, writing_score,
                        study_time, attendance, past_failures, health, absences]])

# --- Predict ---
if st.button("🚀 Predict Result"):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)

    st.markdown("---")
    if prediction[0] == 1:
        st.success("✅ The student is likely to **PASS**! 🎉")
        st.progress(int(proba[0][1] * 100))
        st.markdown(f"**Confidence:** {proba[0][1]*100:.2f}%")
    else:
        st.error("❌ The student is likely to **FAIL**. Encourage better habits.")
        st.progress(int(proba[0][0] * 100))
        st.markdown(f"**Confidence:** {proba[0][0]*100:.2f}%")

# --- Footer ---
st.markdown("---")
st.caption("🔍 Model: Logistic Regression | Built with ❤️ using Streamlit")
