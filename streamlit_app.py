import streamlit as st

st.set_page_config(page_title="펭귄 누적 앱", layout="centered")

st.title("🐧 펭귄을 모아보자!")

# -------------------------
# 상태 저장 (처음 실행 시 0으로 설정)
# -------------------------
if "penguin_count" not in st.session_state:
    st.session_state.penguin_count = 0

# -------------------------
# 버튼
# -------------------------
if st.button("🐧 펭귄 추가하기"):
    st.session_state.penguin_count += 1

st.subheader(f"현재 펭귄 수: {st.session_state.penguin_count}")

# -------------------------
# 움직이는 펭귄 GIF
# (온라인 GIF 사용 가능)
# -------------------------
penguin_gif = "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"

# -------------------------
# 펭귄 누적 출력
# -------------------------
for i in range(st.session_state.penguin_count):
    st.image(penguin_gif, width=120)
