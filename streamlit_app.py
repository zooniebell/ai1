import streamlit as st
import pandas as pd

def main():
    # 메뉴 HTML/CSS 구성
    st.sidebar.markdown(
        """
        <style>
        .menu-button {
            display: block;
            margin: 10px 0;
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            text-decoration: none;
            color: white;
            font-size: 20px;
            font-weight: bold;
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
            opacity: 0.8;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 메뉴 HTML 생성
    menu_html = """
    <a href="?menu=오타니" class="menu-button otani-button">오타니</a>
    <a href="?menu=화이트삭스" class="menu-button whitesox-button">화이트삭스</a>
    <a href="?menu=삼성 라이온즈" class="menu-button samsung-button">삼성 라이온즈</a>
    """
    st.sidebar.markdown(menu_html, unsafe_allow_html=True)

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

if __name__ == "__main__":
    main()
