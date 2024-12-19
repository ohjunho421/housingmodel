import streamlit as st
import joblib
import os

# Check if the model file exists
if not os.path.exists("gradient_boosting_model.pkl"):
    st.error("Model file not found. Please upload 'gradient_boosting_model.pkl' to the correct directory.")
else:
    model = joblib.load("gradient_boosting_model.pkl")

    # Streamlit app
    st.title("주택가격예측모델")
    st.write("가격예측을위한 지표값을 넣어주세요.")

    # Input fields
    LSTAT = st.number_input("LSTAT (% 인구밀도)")
    RM = st.number_input("RM (주거지당 평균 방 수)")
    PTRATIO = st.number_input("도시별 학생-교사 비율")

    # Predict button
    if st.button("Predict"):
        X_new = [[LSTAT, RM, PTRATIO]]
        prediction = model.predict(X_new)[0]
        st.write(f"Predicted value: ${prediction * 1000:.2f}")
