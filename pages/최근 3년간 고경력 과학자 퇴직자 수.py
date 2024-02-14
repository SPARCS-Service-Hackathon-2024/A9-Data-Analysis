import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fontproperties import fontprop

# CSV 파일을 읽어와서 데이터프레임으로 변환
df = pd.read_csv('pages/retirement.csv')

st.title("최근 3년간 고경력 과학자 퇴직자 수")
st.markdown("출처 : 대덕넷")

# 각 연도를 열로 변환하여 데이터 프레임 생성
df_transposed = df.T
df_transposed.columns = df_transposed.iloc[0]
df_transposed = df_transposed[0:]

# 바 차트 그리기
st.bar_chart(df_transposed)
st.markdown("퇴직자 수 표본 : 대덕 연구 단지")
