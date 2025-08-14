
# weather_mood_food_app.py
import streamlit as st

# 음식 추천 데이터 (날씨 + 기분 조합)
food_recommendations = {
    ("맑음", "행복"): "시원한 냉면",
    ("맑음", "우울"): "따뜻한 된장찌개",
    ("맑음", "피곤"): "아이스 아메리카노와 샌드위치",
    ("흐림", "행복"): "파스타와 와인",
    ("흐림", "우울"): "부드러운 크림스프",
    ("흐림", "피곤"): "카레라이스",
    ("비", "행복"): "전과 막걸리",
    ("비", "우울"): "따뜻한 라면",
    ("비", "피곤"): "닭곰탕",
    ("눈", "행복"): "핫초코와 쿠키",
    ("눈", "우울"): "따끈한 국밥",
    ("눈", "피곤"): "찐빵과 호빵"
}

# 앱 제목
st.title("🍽 오늘의 날씨와 기분으로 음식 추천하기")

# 사용자 입력
st.subheader("1️⃣ 오늘의 날씨를 선택하세요")
weather = st.selectbox("날씨", ["맑음", "흐림", "비", "눈"])

st.subheader("2️⃣ 오늘의 기분을 선택하세요")
mood = st.selectbox("기분", ["행복", "우울", "피곤"])

# 추천 버튼
if st.button("추천 음식 보기 🍜"):
    recommendation = food_recommendations.get((weather, mood), "추천 음식이 없습니다 😅")
    st.success(f"오늘은 '{weather}' 날씨에 '{mood}' 기분이군요!\n👉 추천 음식: **{recommendation}**")
