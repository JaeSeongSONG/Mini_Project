# 라이브러리
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 시각화시 한글 폰트
plt.rc('font', family = 'Malgun Gothic')

# 데이터 불러오기
path = 'C:/Users/admin/Desktop/미니 프로젝트 1/시각화용(전처리 완료)/10년간_지역별_청년인구_순이동.csv'
df = pd.read_csv(path)

# 확인하기
df

# 히트맵 생성을 위해 피벗테이블 만들기
pt = df.pivot_table(values = df.columns, index = '지역')

# 피벗테이블 확인하기
pt

# 히트맵 만들기
# 크기 설정하기
plt.figure(figsize = (16, 10))

# 적용하기
sns.heatmap(pt, annot = True, fmt = '.0f', cmap = 'rocket_r')

# 제목
plt.title('지역별 청년층 순이동 인구 수')

# 보여줘
plt.show()