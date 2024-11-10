# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("Streamlit 기본 예제 페이지")

# 2. 부제목
st.subheader("이 페이지는 다양한 Streamlit 기능을 보여줍니다.")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 29],
    "Country": ["Korea", "USA", "UK"]
})
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 5. HTML과 CSS 활용 예제
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

