# 📚 공부 습관 대시보드 (Study Habit Dashboard)

Streamlit과 Pandas, Matplotlib을 활용하여 학생들의 공부 시간, 스마트폰 사용 시간, 성적 데이터를 시각화하는 웹 대시보드입니다.

## 📁 프로젝트 구조

```
PythonProject/
│
├── 6주차실습_제공파일/
│   └── study.csv          # 학생 데이터 파일
│
├── dashboard.py           # 대시보드 메인 파이썬 코드
├── requirements.txt       # 필요 라이브러리 목록 (streamlit, pandas, matplotlib)
└── README.md              # 프로젝트 안내 문서
```

## 🛠️ 주요 기능

1. **주요 지표 요약 (`st.metric`)**:
   * 전체 학생 수, 평균 점수, 평균 공부시간을 한눈에 확인할 수 있습니다.

2. **조건별 데이터 필터링 (`st.slider`)**:
   * 슬라이더를 통해 '최소 공부시간'을 설정하여 특정 기준 이상의 학생 데이터만 필터링합니다.

3. **데이터 시각화**:
   * **공부시간 vs 점수 산점도**: 공부시간과 점수 간의 관계를 시각적으로 확인합니다.
   * **학생별 점수 막대 그래프**: 학생 개인별 성적을 한눈에 비교합니다.

## 🚀 실행 방법

### 1. 필수 패키지 설치

터미널에서 아래 명령어를 실행하여 필요한 패키지(`streamlit`, `pandas`, `matplotlib`)를 설치합니다.

```bash
pip install -r requirements.txt
```

### 2. 대시보드 앱 실행

아래 명령어를 입력하여 Streamlit 대시보드를 실행합니다.

```bash
streamlit run dashboard.py
```

명령어를 실행하면 브라우저에 대시보드가 자동으로 열립니다.