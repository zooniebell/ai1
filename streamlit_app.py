import streamlit as st
import pandas as pd

def main():
    # 사이드바 메뉴 버튼 생성 (HTML+CSS)
    st.sidebar.markdown(
        """
        <style>
        .menu-button {
            display: inline-block;
            margin: 10px 0;
            padding: 15px 20px;
            text-align: center;
            border-radius: 10px;
            color: white;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .otani-button {
            background-color: red;
        }
        .whitesox-button {
            background-color: black;
        }
        .samsung-button {
            background-color: blue;
        }
        .menu-button:hover {
            opacity: 0.9;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.sidebar.button("오타니", key="otani"):
        st.experimental_set_query_params(menu="오타니")
    if st.sidebar.button("화이트삭스", key="whitesox"):
        st.experimental_set_query_params(menu="화이트삭스")
    if st.sidebar.button("삼성 라이온즈", key="samsung"):
        st.experimental_set_query_params(menu="삼성 라이온즈")

    # URL 매개변수를 읽어 메뉴 선택
    query_params = st.experimental_get_query_params()
    menu = query_params.get("menu", ["오타니"])[0]

    # 메뉴 선택에 따라 페이지 표시
    if menu == "오타니":
        show_otani_page()
    elif menu == "화이트삭스":
        show_whitesox_page()
    elif menu == "삼성 라이온즈":
        show_samsung_page()

def show_otani_page():
    st.title("Streamlit 기본 예제 페이지")
    st.subheader("이 페이지는 다양한 Streamlit 기능을 보여줍니다.")

    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [24, 30, 29],
        "Country": ["Korea", "USA", "UK"]
    })
    st.write("데이터프레임 예제")
    st.dataframe(df)

    st.write("HTML 예제")
    st.markdown(
        """
        <div style="color: blue; font-size: 20px;">
            HTML을 활용한 예시 텍스트입니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("HTML과 CSS 예제")
    st.markdown(
        """
        <style>
        .styled-box {
            padding: 10px;
            margin: 5px;
            background-color: lightgreen;
            border-radius: 5px;
            color: darkgreen;
        }
        </style>
        <div class="styled-box">
            HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("이미지 표시 예제")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit 로고")

    st.write("유튜브 동영상 예제")
    st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")


#화이트삭스 페이지 함수 변경

def show_whitesox_page():
    st.title("화이트삭스 페이지")
    
    # 2열 레이아웃 설정
    left_column, right_column = st.columns(2)

    # 왼쪽 열 (2x2 이미지 및 동영상)
    with left_column:
        st.subheader("왼쪽 열: 2x2 이미지 및 동영상")
        
        # 첫 번째 행의 이미지
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/150", caption="이미지 1")
        with col2:
            st.image("https://via.placeholder.com/150", caption="이미지 2")
        
        # 두 번째 행의 동영상
        col3, col4 = st.columns(2)
        with col3:
            st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")  # 예제 URL
        with col4:
            st.video("https://www.youtube.com/watch?v=3JZ_D3ELwOQ")  # 예제 URL


    # 오른쪽 열 (3x3 이미지 및 표)
    with right_column:
        st.subheader("오른쪽 열: 3x3 이미지 및 표")
        
        # 3x3 이미지
        cols = st.columns(3)
        image_urls = [
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100",
            "https://via.placeholder.com/100"
        ]
        
        # 3x3 이미지 그리드
        for i in range(0, len(image_urls), 3):
            with cols[0]:
                st.image(image_urls[i], use_column_width=True)
            with cols[1]:
                st.image(image_urls[i+1], use_column_width=True)
            with cols[2]:
                st.image(image_urls[i+2], use_column_width=True)
        
        # 표 생성
        st.write("데이터프레임 예제")
        df = pd.DataFrame({
            "Column 1": ["A", "B", "C", "D", "E"],
            "Column 2": [10, 20, 30, 40, 50],
            "Column 3": ["X", "Y", "Z", "W", "V"]
        })
        st.table(df)


def show_samsung_page():
    st.title("삼성 라이온즈 페이지")
    st.subheader("동적인 페이지 요소 예제")

    # 1. 버튼 클릭 시 이미지 변경
    st.write("버튼 클릭 시 이미지를 변경해 보세요.")
    if st.button("이미지 1 보기"):
        st.image("https://via.placeholder.com/300/09f/fff.png", caption="이미지 1")
    if st.button("이미지 2 보기"):
        st.image("https://via.placeholder.com/300/f09/fff.png", caption="이미지 2")
    
    # 2. 슬라이더를 통해 값 변화에 따라 데이터 변화
    st.write("슬라이더를 움직여 데이터를 변경해 보세요.")
    slider_value = st.slider("값 선택", 1, 100, 50)
    st.write(f"선택된 값은: {slider_value}")

    # 3. 텍스트 입력에 따라 변경되는 동적 반응
    st.write("텍스트를 입력해 보세요.")
    text_input = st.text_input("텍스트 입력", "삼성 라이온즈")
    if text_input:
        st.write(f"입력된 텍스트: {text_input}")

    # 4. 스크롤 대신 대체로 Streamlit은 특정 스크롤 이벤트를 처리하지 않지만, 사용자가 선택한 요소에 따라 반응 가능
    st.write("멀티 선택 상자를 활용한 반응형 UI")
    options = st.multiselect("이미지 선택", ["이미지 1", "이미지 2", "이미지 3"])
    for option in options:
        if option == "이미지 1":
            st.image("https://via.placeholder.com/300/09f/fff.png", caption="이미지 1")
        elif option == "이미지 2":
            st.image("https://via.placeholder.com/300/f09/fff.png", caption="이미지 2")
        elif option == "이미지 3":
            st.image("https://via.placeholder.com/300/0f9/fff.png", caption="이미지 3")


if __name__ == "__main__":
    main()
