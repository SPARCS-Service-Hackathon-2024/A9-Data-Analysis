import streamlit as st
import pandas as pd

# CSV 파일을 읽어와서 데이터프레임으로 변환
df = pd.read_csv('pages/retirement_ready.csv')

st.title("과학기술인 퇴직 준비")

# 각 연도를 열로 변환하여 데이터 프레임 생성
df_transposed = df.T
# df_transposed.columns = df_transposed.iloc[0]
# df_transposed = df_transposed[0:]

# 바 차트 그리기
st.bar_chart(df_transposed)