import streamlit as st
import json

# Page configuration
st.set_page_config(page_title="Health Insurance Plan Selector", layout="centered")

# Title
st.title("🏥 Health Insurance Plan Selector")

# Gender
gender = st.selectbox("Gender", ["Male", "Female"])

# Age
age = st.slider("Age", min_value=0, max_value=100, value=30)

# Pre-existing diseases
disease_options = [
    "None", "Diabetes", "Hypertension", "Asthma", "High Cholesterol",
    "COPD", "Obesity", "Coronary Artery Disease", "Other Diseases"
]
diseases = st.multiselect("Select Pre-existing Conditions (if any)", options=disease_options, default=["None"])

# Ensure 'None' is exclusive
if "None" in diseases and len(diseases) > 1:
    diseases = [d for d in diseases if d != "None"]

# Coverage bracket
coverage_brackets = [
    "₹5L", "₹10L", "₹15L", "₹20L", "₹25L", "₹30L",
    "₹40L", "₹50L", "₹60L", "₹70L", "₹80L", "₹90L", "₹1Cr"
]
coverage = st.selectbox("Coverage Required", coverage_brackets)

# Submit
if st.button("🔍 Find Best Plans"):
    user_profile = {
        "gender": gender,
        "age": age,
        "diseases": diseases,
        "coverage": coverage
    }

    st.success("✅ Profile captured successfully!")

    # You can remove this display if you just want backend flow
    st.subheader("📦 Collected User Input (for API/backend):")
    st.json(user_profile)

    # Save input as JSON file (optional for now)
    with open("user_input.json", "w") as f:
        json.dump(user_profile, f, indent=4)
