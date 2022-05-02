# 라이브러리
import pandas as pd

# 데이터 불러오기
path_20_year = 'C:/Users/admin/Desktop/미니 프로젝트 1/인구 관련/2020년_경기_전입사유.xlsx'
path_21_year = 'C:/Users/admin/Desktop/미니 프로젝트 1/인구 관련/2021년_경기_전입사유.xlsx'

df_20_year = pd.read_excel(path_20_year, header = 5)
df_21_year = pd.read_excel(path_21_year, header = 5)

# 데이터 확인
df_20_year
df_21_year

# 사용할 컬럼만 추출
df_20_year = df_20_year[['Unnamed: 1', '20세 미만', '20대', '30대']]
df_21_year = df_21_year[['Unnamed: 1', '20세 미만', '20대', '30대']]

# 데이터 확인
df_20_year
df_21_year

# 각 사유별 20세 미만, 20대, 30대 합치기
# 임시 데이터  프레임 만들고 미리 컬럼 생성해놓기
df_new = pd.DataFrame()
df_new['전입_사유'] = df_20_year['전입_사유']
df_new['2020년_청년층_전입_합계'] = 0
df_new['2021년_청년층_전입_합계'] = 0
df_new['청년층_전입_총_합계'] = 0
df_new['비율'] = 0

# 반복문으로 각 행 더해서 임시 데이터 프레임에 넣음
for i in range(8) :
    df_new['2020년_청년층_전입_합계'].iloc[i] = df_20_year.drop(['전입_사유'], axis = 1).iloc[i].sum()
    df_new['2021년_청년층_전입_합계'].iloc[i] = df_21_year.drop(['전입_사유'], axis = 1).iloc[i].sum()

# 20년, 21년 전입 인구를 더해서 새 컬럼에 넣음
for i in range(8) :
    df_new['청년층_전입_총_합계'].iloc[i] = df_new.drop(['전입_사유'], axis = 1).iloc[i].sum()
    
# 비율 컬럼 생성하기 : (각 사유 / 계) * 100
for i in range(8) :
    df_new['비율'].iloc[i] =( df_new['청년층_전입_총_합계'].iloc[i] / df_new['청년층_전입_총_합계'].iloc[0]) * 100
    
# 확인하기
df_new