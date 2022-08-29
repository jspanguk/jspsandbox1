import pandas as pd
import os
import numpy

print(os.getcwd()) #실행폴더 확인

file_path = 'C:\\Users\zkshq\Documents\VSCodeProjects\jspsandbox\df_summary_fullest.csv' #폴더아래에 csv파일 넣어둬야 실행가능하지만 경로를 지정해주면 작업환경이 달라도 불러오기 가능

df = pd.read_csv(file_path, encoding='utf-8')        #불러올 파일의 경로, 폰트깨짐을 막기위해 파일별로 적정한 인코딩방식
df3 = df.head(3)         #크기가 너무 크므로 앞부분 3개의 레코드만 불러온다
df3.to_json('df_summary_fullset3.json',force_ascii=False)   #json파일로 내보내기, 아스키코드 사용 X
pdf3 = pd.read_json('df_summary_fullset3.json')    #변환된 json 파일을 불러오기
print(pdf3)    #pdf3의 json 파일 출력


