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
    ("흐림", "긴장"): ("토마토 리조또", "https://images.unsplash.com/photo-1603070649634-ef08b401))
                
                          

