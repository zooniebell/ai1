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


def show_whitesox_page():
    st.title("화이트삭스 페이지")
    
    # 2열 레이아웃 설정
    left_column, right_column = st.columns(2)

    # 왼쪽 열 (2x2 이미지 및 동영상)
    with left_column:
        st.subheader("왼쪽 열: 2x2 이미지 및 동영상")
        
        # 이미지 1
        st.image("https://via.placeholder.com/150", caption="이미지 1")
        # 이미지 2
        st.image("https://via.placeholder.com/150", caption="이미지 2")
        # 동영상 1
        st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")  # 예제 URL
        # 동영상 2
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
    st.write("이 페이지는 현재 비어 있습니다.")

if __name__ == "__main__":
    main()
