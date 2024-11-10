#스트림릿 페이지 메뉴 추가

import streamlit as st
import pandas as pd

# 함수 정의
def show_menu():
    # 사이드바 메뉴
    menu = st.sidebar.radio(
        "메뉴 선택",
        ("오타니", "화이트삭스", "삼성 라이온즈")
    )
    return menu

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

    # 6. 이미지 표시
    st.write("이미지 표시 예제")
    st.image("https://i.ibb.co/SN8hMQc/RMjy-Svv-Cwp-UCu-Zlv-NBDr-Ur-1-Di-Jn1-MUw-I713e7qfupo-M-4-G-99-0ag-N-H5se-Wrj-Ft-Z3w-C3u-Q0-BMc71l-P.webp", caption="오타니를 찬양하라!")

    # 7. 유튜브 링크 (썸네일 표시)
    st.write("유튜브 동영상 예제")
    st.video("https://www.youtube.com/watch?v=3hNXCbSDBvc")

def show_whitesox_page():
    st.title("화이트삭스 페이지")
    st.write("이 페이지는 현재 비어 있습니다.")

def show_samsung_page():
    st.title("삼성 라이온즈 페이지")
    st.write("이 페이지는 현재 비어 있습니다.")

# 메인 코드 실행
menu_selection = show_menu()

if menu_selection == "오타니":
    show_otani_page()
elif menu_selection == "화이트삭스":
    show_whitesox_page()
elif menu_selection == "삼성 라이온즈":
    show_samsung_page()
