import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')

df = pd.read_csv('pages/r_costii.csv')

# 차트 제목
st.title("총 연구개발비의 시도별 추이")
selected_regions = st.multiselect('지역 선택', options=df['region'])

data = {}
for region in selected_regions:
    data[region] = []
    for year in range(2018, 2022):
        data[region].append(df[df['region'] == region][str(year)].values[0])
 
plt.figure(figsize=(10, 6))  
for region, values in data.items():
    plt.plot(range(2018, 2022), values, label=region)

plt.xlabel('연도')  
plt.ylabel('과학기술혁신 역량평가 지수')  
plt.title('지역 과학기술혁신 역량평가 지수')  
plt.legend()  
st.pyplot(plt)  
