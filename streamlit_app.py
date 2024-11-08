import streamlit as st
import pandas as pd

# 타이틀 설정
st.title("나의 첫번째 서비스")

# 서브타이틀
st.subheader("GPT 만세!!!!!")

# 표 데이터 생성
data = {
    '이름': ['홍길동', '이중엽', '조용수'],
    '나이': [50, 10, 59],
    '직업': ['학생', '마라토너', '동네건달']
}
df = pd.DataFrame(data)

# 표 출력
st.write("강원사대부고:")
st.dataframe(df)

# HTML 메시지 출력
st.markdown("""
    <div style="background-color: lightblue; padding: 10px;">
        <h3>HTML 스타일링 메시지</h3>
        <p>내가 아직도 장원재로 보이니 흐흐흐흐흐흐.</p>
    </div>
""", unsafe_allow_html=True)

# 추가적인 텍스트
st.write("하하호호호호호호호호호호ㅗㅎ호ㅗ호호호호호홓")
