import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fontproperties import fontprop

plt.rc('font', family='AppleGothic')
df = pd.read_csv('pages/rnd_money.csv')

st.title("총 연구개발비의 시도별 추이")
st.markdown("출처 : 부산 과학기술정보 서비스")

selected_regions = st.multiselect('지역 선택', options=df['region'], default=["대전", "대구", "광주"])

data = {}
for region in selected_regions:
    data[region] = []
    for year in range(2017, 2021):
        data[region].append(df[df['region'] == region][str(year)].values[0])

fig, ax = plt.subplots()
plt.figure(figsize=(10, 6))  
for region, values in data.items():
    plt.fill_between(range(2017, 2021), values, label=region, alpha=0.3)
for label in ax.get_xticklabels():
    label.set_fontproperties(fontprop)

plt.xlabel('연도', fontproperties=fontprop)
plt.ylabel('연구 개발비 (단위 : 억원)', fontproperties=fontprop)
plt.title('총 연구개발비의 시도별 추이', fontproperties=fontprop)
plt.legend()  
st.pyplot(plt)  
