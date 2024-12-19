import os
import streamlit as st
import joblib

# Load model
model_path = "gradient_boosting_model.pkl"

try:
    # 모델 로드 시도
    model = joblib.load("gradient_boosting_model.pkl", mmap_mode=None)
    print("Model loaded successfully!")
except FileNotFoundError:
    # 파일이 없는 경우 처리
    print("Model file 'gradient_boosting_model.pkl' not found! Ensure it is uploaded correctly.")
except Exception as e:
    # 다른 예외 처리
    print(f"An error occurred while loading the model: {e}")

# Streamlit app
st.title("주택 가격 예측 모델")
st.write("예측을 위한 입력값을 넣어주세요.")

# Input fields
LSTAT = st.number_input("LSTAT (% 인구밀도)")
RM = st.number_input("RM (주거지당 평균 방 수)")
PTRATIO = st.number_input("PTRATIO (도시별 학생-교사 비율)")

# Predict button
if st.button("Predict"):
    try:
        X_new = [[LSTAT, RM, PTRATIO]]
        prediction = model.predict(X_new)[0]
        st.write(f"예측된 주택 가격: ${prediction * 1000:.2f}")
    except Exception as e:
        st.error("예측 중 오류가 발생했습니다. 입력값을 확인하세요.")
