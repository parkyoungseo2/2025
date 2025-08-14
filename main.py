# weather_mood_food_app_full.py
import streamlit as st

# 다양한 날씨 + 기분 조합별 음식과 이미지 데이터
food_data = {
    ("맑음", "행복"): ("시원한 냉면", "https://images.unsplash.com/photo-1609335081028-984be1c3c18f"),
    ("맑음", "우울"): ("따뜻한 된장찌개", "https://images.unsplash.com/photo-1627308595190-f56d2d7d41d0"),
    ("맑음", "피곤"): ("아이스 아메리카노와 샌드위치", "https://images.unsplash.com/photo-1523983301871-64c2f27d8c5e"),
    ("맑음", "설렘"): ("딸기 케이크", "https://images.unsplash.com/photo-1551024709-8f23befc6f87"),
    ("맑음", "긴장"): ("초밥 세트", "https://images.unsplash.com/photo-1553621042-f6e147245754"),
    ("맑음", "허기"): ("치즈버거", "https://images.unsplash.com/photo-1550547660-d9450f859349"),

    ("흐림", "행복"): ("크림 파스타와 와인", "https://images.unsplash.com/photo-1521389508051-d7ffb5dc8a5d"),
    ("흐림", "우울"): ("부드러운 크림스프", "https://images.unsplash.com/photo-1603071659230-2d9b58d69db3"),
    ("흐림", "피곤"): ("카레라이스", "https://images.unsplash.com/photo-1598515213645-6aa4f30cc3f4"),
    ("흐림", "설렘"): ("티라미수", "https://images.unsplash.com/photo-1601979031896-8eaf5c4037b3"),
    ("흐림", "긴장"): ("토마토 리조또", "https://images.unsplash.com/photo-1603070649634-ef08b401d4e8"),
    ("흐림", "허기"): ("라자냐", "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f"),

    ("비", "행복"): ("김치전과 막걸리", "https://images.unsplash.com/photo-1617196039897-2f2bfae3f3b7"),
    ("비", "우울"): ("따뜻한 라면", "https://images.unsplash.com/photo-1617191519400-2fbb746f9fda"),
    ("비", "피곤"): ("닭곰탕", "https://images.unsplash.com/photo-1627308595210-8cc86d2a4e62"),
    ("비", "설렘"): ("수플레 팬케이크", "https://images.unsplash.com/photo-1601979031896-8eaf5c4037b3"),
    ("비", "긴장"): ("버섯 크림 리조또", "https://images.unsplash.com/photo-1603070649634-ef08b401d4e8"),
    ("비", "허기"): ("우동", "https://images.unsplash.com/photo-1627308595237-02a9d2c4a3f0"),

    ("눈", "행복"): ("핫초코와 쿠키", "https://images.unsplash.com/photo-1604152135912-04a22b3f5f87"),
    ("눈", "우울"): ("따끈한 국밥", "https://images.unsplash.com/photo-1625714586168-bb1d7403f0d3"),
    ("눈", "피곤"): ("찐빵과 호빵", "https://images.unsplash.com/photo-1587314168485-3234ff77d3fd"),
    ("눈", "설렘"): ("딸기 타르트", "https://images.unsplash.com/photo-1578985545062-69928b1d9587"),
    ("눈", "긴장"): ("샤브샤브", "https://images.unsplash.com/photo-1594041685349-e0c0f06b7a50"),
    ("눈", "허기"): ("군밤", "https://images.unsplash.com/photo-1601889096519-020b7c6d28d2"),

    ("바람", "행복"): ("바질 피자", "https://images.unsplash.com/photo-1601924638867-3ec3a39f7345"),
    ("바람", "우울"): ("미트볼 스파게티", "https://images.unsplash.com/photo-1605475128026-bd6a7a5e95cd"),
    ("바람", "피곤"): ("프렌치토스트", "https://images.unsplash.com/photo-1603077743909-fc05644d9022"),
    ("바람", "설렘"): ("크로아상과 커피", "https://images.unsplash.com/photo-1584367369853-8a5d4d4f8b04"),
    ("바람", "긴장"): ("치킨 커틀릿", "https://images.unsplash.com/photo-1627308595224-0e1a8e8572f7"),
    ("바람", "허기"): ("소고기 스테이크", "https://images.unsplash.com/photo-1551183053-bf91a1d81141"),

    ("안개", "행복"): ("홍차와 스콘", "https://images.unsplash.com/photo-1603071659230-2d9b58d69db3"),
    ("안개", "우울"): ("콘스프와 빵", "https://images.unsplash.com/photo-1598515213645-6aa4f30cc3f4"),
    ("안개", "피곤"): ("버섯 스프", "https://images.unsplash.com/photo-1603071659230-2d9b58d69db3"),
    ("안개", "설렘"): ("딸기 마카롱", "https://images.unsplash.com/photo-1587314168485-3234ff77d3fd"),
    ("안개", "긴장"): ("라자냐", "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f"),
    ("안개", "허기"): ("포크커틀릿", "https://images.unsplash.com/photo-1627308595237-02a9d2c4a3f0")
}

# 앱 제목
st.title("🍽 오늘의 날씨와 기분으로 음식 추천하기")

# 사용자 입력
st.subheader("1️⃣ 오늘의 날씨를 선택하세요")
weather = st.selectbox("날씨", ["맑음", "흐림", "비", "눈", "바람", "안개"])

st.subheader("2️⃣ 오늘의 기분을 선택하세요")
mood = st.selectbox("기분", ["행복", "우울", "피곤", "설렘", "긴장", "허기"])

# 추천 버튼
if st.button("추천 음식 보기 🍜"):
    result = food_data.get((weather, mood))
    if result:
        food_name, img_url = result
        st.success(f"오늘은 '{weather}' 날씨에 '{mood}' 기분이군요!")
        st.markdown(f"### 👉 추천 음식: **{food_name}**")
        st.image(img_url, caption=food_name, use_column_width=True)
    else:
        st.warning("추천 음식이 없습니다 😅")
