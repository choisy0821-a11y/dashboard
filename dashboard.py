import pandas as pd
import streamlit as st

# 1. 앱 제목 설정
st.title("📚 공부 습관 대시보드")
st.write("학생들의 공부 시간과 성적 데이터를 시각화한 대시보드입니다.")

# 2. study.csv 파일 읽기
# (같은 폴더에 study.csv 파일이 있어야 합니다)
df=pd.read_csv("6주차실습_제공파일/study.csv")

# 3. 주요 지표(학생 수, 평균 점수, 평균 공부시간) 계산
total_students = len(df)
avg_score = df["점수"].mean()
avg_study_time = df["공부시간"].mean()

# st.metric을 사용해 한 줄(3개의 열)에 주요 지표 표시
col1, col2, col3 = st.columns(3)
col1.metric("전체 학생 수", f"{total_students}명")
col2.metric("평균 점수", f"{avg_score:.1f}점")
col3.metric("평균 공부시간", f"{avg_study_time:.1f}시간")

st.divider()  # 시각적 구분선

# 4. 슬라이더로 최소 공부시간 필터링 구현
min_study = st.slider(
    "최소 공부시간 선택 (시간)",
    min_value=float(df["공부시간"].min()),
    max_value=float(df["공부시간"].max()),
    value=0.0,
    step=0.5,
)

# 조건에 맞는 데이터 필터링
filtered_df = df[df["공부시간"] >= min_study]
st.write(f"현재 조건에 맞는 학생 수: **{len(filtered_df)}명**")

# 5. 스트림릿 기본 차트 그리기
# (1) 공부시간과 점수의 관계를 보여주는 산점도
st.subheader("📊 공부시간 vs 점수 산점도")
st.scatter_chart(filtered_df, x="공부시간", y="점수")

# (2) 학생별 점수를 보여주는 막대 그래프 (학생ID를 인덱스로 지정)
st.subheader("📈 학생별 점수 막대 그래프")
chart_data = filtered_df.set_index("학생ID")["점수"]
st.bar_chart(chart_data)