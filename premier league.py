import streamlit as st
import pandas as pd

# 1. 웹 페이지 기본 레이아웃 설정
st.set_page_config(page_title="2025-2026 EPL 대시보드", layout="wide", page_icon="⚽")

# ==========================================
# 2. 스크린샷 데이터를 기반으로 한 데이터셋 정의
# ==========================================

# (1) EPL 20개 팀 최종 순위 전체 데이터 (1위~20위 완전 반영)
team_data = {
    "순위": list(range(1, 21)),
    "팀명": [
        "아스널", "맨 시티", "맨유", "애스턴 빌라", "리버풀", 
        "본머스", "선덜랜드", "브라이턴", "브렌트퍼드", "첼시", 
        "풀럼", "뉴캐슬", "에버턴", "리즈 유나이티드", "크리스탈 팰리스", 
        "노팅엄 포레스트", "토트넘", "웨스트 햄", "번리", "울브스"
    ],
    "경기수": [38] * 20,
    "승": [26, 23, 20, 19, 17, 13, 14, 14, 14, 14, 15, 14, 13, 11, 11, 11, 10, 10, 4, 3],
    "무": [7, 9, 11, 8, 9, 18, 12, 11, 11, 10, 7, 7, 10, 14, 12, 11, 11, 9, 10, 11],
    "패": [5, 6, 7, 11, 12, 7, 12, 13, 13, 14, 16, 17, 15, 13, 15, 16, 17, 19, 24, 24],
    "승점": [85, 78, 71, 65, 60, 57, 54, 53, 53, 52, 52, 49, 49, 47, 45, 44, 41, 39, 22, 20],
    "득점": [71, 77, 69, 56, 63, 58, 42, 52, 55, 58, 47, 53, 47, 49, 41, 48, 48, 46, 38, 27],
    "실점": [27, 35, 50, 49, 53, 54, 48, 46, 52, 52, 51, 55, 50, 56, 51, 51, 57, 65, 75, 68],
    "골득실": [44, 42, 19, 7, 10, 4, -6, 6, 3, 6, -4, -2, -3, -7, -10, -3, -9, -19, -37, -41]
}
df_teams = pd.DataFrame(team_data)

# (2) 개인 득점 순위 데이터
scorer_data = {
    "순위": [1, 2, 3, 4, 5, 5],
    "선수명": ["엘링 홀란드", "이고르 치아구", "앙투안 세메뇨", "올리 왓킨스", "주앙 페드로", "모건 깁스화이트"],
    "소속팀": ["맨 시티", "브렌트퍼드", "맨 시티", "애스턴 빌라", "첼시", "노팅엄 포레스트"],
    "득점": [27, 22, 17, 16, 15, 15]
}
df_scorers = pd.DataFrame(scorer_data)

# (3) 개인 도움 순위 데이터
assist_data = {
    "순위": [1, 2, 3, 4, 5, 5, 5, 5, 5],
    "선수명": [
        "브루노 페르난데스", "라얀 셰르키", "재러드 보언", "엘링 홀란드", 
        "도미닉 소보슬라이", "엔조 르 페", "해리 윌슨", "제임스 가너", "모하메드 살라"
    ],
    "소속팀": ["맨유", "맨 시티", "웨스트 햄", "맨 시티", "리버풀", "선덜랜드", "풀럼", "에버턴", "리버풀"],
    "도움": [21, 12, 11, 8, 7, 7, 7, 7, 7]
}
df_assists = pd.DataFrame(assist_data)


# ==========================================
# 3. 대시보드 화면 UI 구성
# ==========================================

# 타이틀 영역
st.title("⚽ 2025-2026 프리미어리그(EPL) 데이터 대시보드")
st.markdown("#### 🎓 AI소프트웨어융합학부 데이터 시각화 실습 과제")
st.write("---")

# 가점 포인트 ①: 핵심 지표 요약 (Metric 사용)
st.subheader("📌 시즌 주요 하이라이트")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="🏆 리그 우승 팀", value="아스널", delta="85 승점")
with col2:
    st.metric(label="🔥 최다 득점 팀", value="맨체스터 시티", delta="77 득점")
with col3:
    st.metric(label="🥇 득점왕 (Golden Boot)", value="엘링 홀란드", delta="27 골")
with col4:
    st.metric(label="🪄 도움왕 (Playmaker)", value="브루노 페르난데스", delta="21 어시스트")

st.write("---")

# 가점 포인트 ②: 사이드바 대화형 필터 기능 추가
st.sidebar.header("🔍 데이터 검색 필터")
selected_team = st.sidebar.selectbox("특정 팀의 기록만 확인하기", ["전체 보기"] + list(df_teams["팀명"]))


# 4. 기능별 탭 분할 구성
tab1, tab2, tab3 = st.tabs(["🏆 팀별 종합 순위표", "⚽ 개인 득점 순위", "🪄 개인 도움 순위"])

# --- 첫 번째 탭: 팀 순위 ---
with tab1:
    st.subheader("📋 2025-2026 EPL 최종 순위표")
    
    # 사이드바 필터와 연동
    if selected_team == "전체 보기":
        st.dataframe(df_teams.set_index("순위"), use_container_width=True)
        
        # 전체 보기일 때만 하단에 시각화 그래프 출력
        st.write("")
        st.subheader("📊 팀별 최종 승점 비교 그래프")
        st.bar_chart(data=df_teams, x="팀명", y="승점", color="#1f77b4")
        
        st.subheader("📈 팀별 득점력 비교 그래프")
        st.bar_chart(data=df_teams, x="팀명", y="득점", color="#ff7f0e")
    else:
        # 특정 팀 선택 시 해당 팀 데이터만 깔끔하게 서머리 표출
        filtered_df = df_teams[df_teams["팀명"] == selected_team]
        st.dataframe(filtered_df.set_index("순위"), use_container_width=True)
        st.success(f"💡 {selected_team}은(는) 이번 시즌 최종 {filtered_df['순위'].values[0]}위를 기록했습니다.")

# --- 두 번째 탭: 득점 순위 ---
with tab2:
    st.subheader("🔥 시즌 개인 득점 순위 Top 5 (공동 순위 포함)")
    st.dataframe(df_scorers.set_index("순위"), use_container_width=True)
    
    st.write("")
    st.subheader("📊 주요 선수별 득점 수 시각화")
    st.bar_chart(data=df_scorers, x="선수명", y="득점", color="#d62728")

# --- 세 번째 탭: 도움 순위 ---
with tab3:
    st.subheader("🪄 시즌 개인 도움 순위 Top 5 (공동 순위 포함)")
    st.dataframe(df_assists.set_index("순위"), use_container_width=True)
    
    st.write("")
    st.subheader("📊 주요 선수별 어시스트 수 시각화")
    st.bar_chart(data=df_assists, x="선수명", y="도움", color="#2ca02c")
