import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')

# CSV 파일을 읽어와서 데이터프레임으로 변환
df = pd.read_csv('pages/rnd_population.csv')

# CSV 파일의 region 열을 선택지로 사용하여 multiselect 생성
selected_regions = st.multiselect('지역 선택', options=df['region'])

# 선택된 각 지역에 대해 각 연도의 값을 리스트에 저장
data = {}
for region in selected_regions:
    data[region] = []
    for year in range(2015, 2021):
        # 인구수를 문자열에서 숫자로 변환하여 저장
        data[region].append(int(df[df['region'] == region][str(year)].str.replace(',', '').values[0]))

# 하나의 그래프 안에 선택된 모든 지역의 값을 비교하여 표시
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
for region, values in data.items():
    plt.plot(range(2015, 2021), values, label=region)

plt.xlabel('연도')  # x축 라벨 설정
plt.ylabel('인구 수')  # y축 라벨 설정
plt.title('지역 별 연구개발인력 현황')  # 그래프 제목 설정
plt.legend()  # 범례 표시
st.pyplot(plt)  # 그래프를 Streamlit 앱에 표시
