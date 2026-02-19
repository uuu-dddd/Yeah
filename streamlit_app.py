import streamlit as st

st.set_page_config(page_title="서술형 평가 도우미", layout="wide")

st.title("📘 서술형 평가 작성 앱")

# -----------------------
# 문제 설정
# -----------------------
question = "식물이 광합성을 하는 이유를 설명하시오."
keywords = ["빛", "이산화탄소", "산소", "포도당"]

st.subheader("📝 문제")
st.write(question)

# -----------------------
# 학생 정보 입력
# -----------------------
student_name = st.text_input("학생 이름을 입력하세요")

answer = st.text_area("학생 서술 답안을 입력하세요", height=200)

# -----------------------
# 채점 버튼
# -----------------------
if st.button("채점하기"):

    if answer.strip() == "":
        st.warning("답안을 입력하세요!")
    else:
        score = 0
        matched_keywords = []

        for keyword in keywords:
            if keyword in answer:
                score += 1
                matched_keywords.append(keyword)

        total_score = len(keywords)

        st.subheader("📊 채점 결과")
        st.write(f"총점: {score} / {total_score}")
        st.write("✅ 포함된 핵심 개념:", matched_keywords)

        # 피드백 생성
        missing = list(set(keywords) - set(matched_keywords))

        if score == total_score:
            feedback = "핵심 개념을 모두 포함하여 매우 잘 작성했습니다 👏"
        else:
            feedback = f"다음 개념을 보완해 보세요 👉 {', '.join(missing)}"

        # -----------------------
        # 💬 말풍선 피드백
        # -----------------------
        with st.chat_message("assistant"):
            st.write(feedback)
