# weather_mood_food_app_with_images.py
import streamlit as st

# 음식 추천 데이터 + 이미지 URL 매핑
food_data = {
    ("맑음", "행복"): {
        "name": "시원한 냉면",
        "img": "https://images.unsplash.com/photo-1609335081028-984be1c3c18f"
    },
    ("맑음", "우울"): {
        "name": "따뜻한 된장찌개",
        "img": "https://images.unsplash.com/photo-1627308595190-f56d2d7d41d0"
    },
    ("맑음", "피곤"): {
        "name": "아이스 아메리카노와 샌드위치",
        "img": "https://images.unsplash.com/photo-1523983301871-64c2f27d8c5e"
    },
    ("흐림", "행복"): {
        "name": "파스타와 와인",
        "img": "https://images.unsplash.com/photo-1521389508051-d7ffb5dc8a5d"
    },
    ("흐림", "우울"): {
        "name": "부드러운 크림스프",
        "img": "https://images.unsplash.com/photo-1603071659230-2d9b58d69db3"
    },
    ("흐림", "피곤"): {
        "name": "카레라이스",
        "img": "https://images.unsplash.com/photo-1598515213645-6aa4f30cc3f4"
    },
    ("비", "행복"): {
        "name": "전과 막걸리",
        "img": "https://images.unsplash.com/photo-1617196039897-2f2bfae3f3b7"
    },
    ("비", "우울"): {
        "name": "따뜻한 라면",
        "img": "https://images.unsplash.com/photo-1617191519400-2fbb746f9fda"
    },
    ("비", "피곤"): {
        "name": "닭곰탕",
        "img": "https://images.unsplash.com/photo-1627308595210-8cc86d2a4e62"
    },
    ("눈", "행복"): {
        "name": "핫초코와 쿠키",
        "img": "https://images.unsplash.com/photo-1604152135912-04a22b3f5f87"
    },
    ("눈", "우울"): {
        "name": "따끈한 국밥",
        "img": "https://images.unsplash.com/photo-1625714586168-bb1d7403f0d3"
    },
    ("눈", "피곤"): {
        "name": "찐빵과 호빵",
        "img": "https://images.unsplash.com/photo-1587314168485-3234ff77d3fd"
    }
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
    result = food_data.get((weather, mood))
    if result:
        st.success(f"오늘은 '{weather}' 날씨에 '{mood}' 기분이군요! 👉 추천 음식: **{result['name']}**")
        st.image(result["img"], caption=result["name"], use_column_width=True)
    else:
        st.warning("추천 음식이 없습니다 😅")
