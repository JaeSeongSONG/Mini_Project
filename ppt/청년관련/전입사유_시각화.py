# 라이브러리
import pandas as pd
import matplotlib.pyplot as plt

# 시각화시 한글 폰트
plt.rc('font', family = 'Malgun Gothic')

# 데이터 불러오기
path = 'C:/Users/admin/Desktop/미니 프로젝트 1/시각화용(전처리 완료)/20년_21년_청년층_경기도_전입_사유_및_전입_합계(비율).csv'
df = pd.read_csv(path).drop(['Unnamed: 0'], axis = 1)

# 사용하지 않는 행 제외하기
df = df[(df['전입_사유'] != '계')]

# 확인하기
df

# 시각화
# 20년 전입사유 시각화
# 그래프 크기
plt.figure(figsize=(10,10))

# 중심에서 벗어나는 정도 설정하기
explode = list()

# for문으로 리스트에 데이터 세트의 행의 수 만큼 값을 넣음
for i in range(len(df)) :
    explode.append(0.1)

# 적용하기
plt.pie(df['2020년_청년층_전입_합계'], labels = df['전입_사유'], autopct='%.1f%%', explode = explode)

# 제목 설정하기
plt.title('20년 청년층 전입 사유')

# 보여줘
plt.show()

# 21년 전입사유 시각화
plt.figure(figsize=(10,10))
explode = list()
for i in range(len(df)) :
    explode.append(0.1)
plt.pie(df['2021년_청년층_전입_합계'], labels = df['전입_사유'], autopct='%.1f%%', explode = explode)
plt.title('21년 청년층 전입 사유')
plt.show()