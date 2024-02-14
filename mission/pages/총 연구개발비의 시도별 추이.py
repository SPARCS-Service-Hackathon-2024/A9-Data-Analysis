import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')

df = pd.read_csv('pages/rnd_money.csv')

st.title("총 연구개발비의 시도별 추이")

selected_regions = st.multiselect('지역 선택', options=df['region'])

data = {}
for region in selected_regions:
    data[region] = []
    for year in range(2017, 2021):
        data[region].append(df[df['region'] == region][str(year)].values[0])

plt.figure(figsize=(10, 6))  
for region, values in data.items():
    plt.fill_between(range(2017, 2021), values, label=region, alpha=0.3)

plt.xlabel('연도')  
plt.ylabel('연구 개발비 (단위 : 억원)')  
plt.title('총 연구개발비의 시도별 추이')  
plt.legend()  
st.pyplot(plt)  
