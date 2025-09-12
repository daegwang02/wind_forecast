import streamlit as st
import time
import numpy as np

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'recommendation_result' not in st.session_state:
    st.session_state.recommendation_result = None

# 페이지 이동 함수
def go_to_page(page_name):
    st.session_state.page = page_name

# 메인 화면
def main_page():
    st.title("AI 여행 플래너")
    st.markdown("### 메인 화면")
    st.image("https://via.placeholder.com/600x200.png?text=Main+Screen+Image", caption="여행의 시작, AI와 함께")

    st.write("환영합니다! 원하시는 서비스를 선택하세요.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("AI 추천 받기", use_container_width=True):
            go_to_page('ai')
        if st.button("지도 보기", use_container_width=True):
            go_to_page('map')
    with col2:
        if st.button("스탬프 투어", use_container_width=True):
            go_to_page('stamp_tour')
        if st.button("예약 / 결제", use_container_width=True):
            go_to_page('reservation')

# AI 추천 화면
def ai_page():
    st.title("AI 기반 추천 시스템")
    st.markdown("### 당신의 맞춤형 여행지를 찾아보세요!")

    # 사용자 정보 입력
    st.subheader("1. 사용자 정보 입력")
    nationality = st.selectbox("국적", ["한국", "미국", "일본", "기타"])
    gender = st.selectbox("성별", ["남성", "여성"])
    age = st.number_input("나이", min_value=1, max_value=100, value=25)
    location = st.text_input("현재 관광 중인 지역 (예: 부산 해운대)")

    # 취향/음식 자연어 입력
    st.subheader("2. 취향 입력 (자연어)")
    taste_query = st.text_area("취향/음식 키워드를 자유롭게 입력하세요. (예: 조용하고 예쁜 카페, 매콤한 해산물 요리)")

    if st.button("AI 추천 실행"):
        # AI 추천 로직 시뮬레이션
        with st.spinner("AI가 당신을 위한 최고의 장소를 찾고 있습니다..."):
            time.sleep(2)  # BERT 및 코사인 유사도 계산 시뮬레이션

            # 임의의 데이터와 코사인 유사도 시뮬레이션
            st.session_state.recommendation_result = {
                "user_info": f"국적: {nationality}, 성별: {gender}, 나이: {age}, 위치: {location}",
                "query": taste_query,
                "recommendations": [
                    {"name": "더베이101", "description": "야경과 식사를 동시에 즐기는 명소"},
                    {"name": "감천문화마을", "description": "다채로운 색깔의 마을, 인생샷 명소"},
                    {"name": "해운대시장 곰장어", "description": "부산의 명물, 매콤한 곰장어 요리"}
                ]
            }
        st.success("✅ 추천이 완료되었습니다!")

    if st.session_state.recommendation_result:
        st.markdown("---")
        st.subheader("AI 추천 결과 (상위 3개)")
        st.write(f"**입력 정보:** {st.session_state.recommendation_result['user_info']}")
        st.write(f"**취향 키워드:** _{st.session_state.recommendation_result['query']}_")
        
        for i, rec in enumerate(st.session_state.recommendation_result['recommendations']):
            st.markdown(f"**{i+1}. {rec['name']}**")
            st.write(f"_{rec['description']}_")

    st.markdown("---")
    if st.button("메인 화면으로 돌아가기"):
        go_to_page('main')

# 스탬프 투어 화면
def stamp_tour_page():
    st.title("스탬프 투어")
    st.markdown("### 🏃‍♂️ 여행하며 스탬프를 모아보세요!")
    st.info("이 기능은 목업입니다. 스탬프 투어 시스템은 현재 개발 중입니다.")
    st.image("https://via.placeholder.com/600x400.png?text=Stamp+Tour+Map+Mockup", caption="스탬프 투어 지도 (목업)")
    
    st.markdown("---")
    if st.button("메인 화면으로 돌아가기"):
        go_to_page('main')

# 지도 화면
def map_page():
    st.title("지도 기능")
    st.markdown("### 🗺️ 네이버 지도 API 연동 (목업)")
    st.info("사용자가 직접 입력한 위치를 중심으로 지도를 표시합니다.")
    user_location = st.text_input("위치 입력", "서울시 강남구")
    st.image("https://via.placeholder.com/600x400.png?text=Naver+Map+API+Mockup", caption=f"'{user_location}' 위치 지도")

    st.markdown("---")
    if st.button("메인 화면으로 돌아가기"):
        go_to_page('main')

# 예약 화면
def reservation_page():
    st.title("음식점 예약")
    st.markdown("### 🍽️ '캐치테이블' 예약 시스템 연동 (목업)")
    
    st.write("원하시는 음식점을 선택하고 예약하세요.")
    restaurant_list = ["더베이101", "아지노야", "곰장어집"]
    selected_restaurant = st.selectbox("음식점 선택", restaurant_list)
    
    if st.button("예약 및 선결제 진행하기", use_container_width=True):
        go_to_page('payment')

    st.markdown("---")
    if st.button("메인 화면으로 돌아가기"):
        go_to_page('main')

# 결제 화면
def payment_page():
    st.title("결제 화면")
    st.markdown("### 💳 Visa 선결제 (목업)")
    st.write("Visa 카드로만 선결제가 가능합니다.")
    
    st.image("https://via.placeholder.com/200x100.png?text=Visa+Card+Logo", caption="Visa 카드만 가능")
    
    card_number = st.text_input("카드 번호", "4___ ____ ____ ____")
    expiry_date = st.text_input("유효기간", "MM/YY")
    cvc = st.text_input("CVC", "___")

    if st.button("결제하기"):
        st.success("✅ **결제가 성공적으로 처리되었습니다.** (목업)")
        st.balloons()
    
    st.markdown("---")
    if st.button("예약 화면으로 돌아가기"):
        go_to_page('reservation')

# 페이지 라우팅
page_functions = {
    'main': main_page,
    'ai': ai_page,
    'stamp_tour': stamp_tour_page,
    'map': map_page,
    'reservation': reservation_page,
    'payment': payment_page
}

page_functions[st.session_state.page]()
