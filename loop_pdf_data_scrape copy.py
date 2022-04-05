import tabula
import pandas as pd
from tabula import read_pdf
HEADERS=['Car','Driver','AvgStart','AvgMidRace','AvgFinish','Avg Pos','LapsLed','PercentLapsLed','TotalLaps','DriverRating','Pts','PassDiff','GreenPass','GreenPassed','QualityPasses','PercentQualityPasses','NumFastestLaps','LapsinTop15','PercentLapsTop15']
data_location=input('Please provide the full path to the PDF data')
data_output=input('Please provide desired full path output location')
df=read_pdf(data_location,pages='1')

df2=df[0].iloc[5:]
df2['Box Score']=df2['Box Score'].str.split()
df2['Unnamed: 6']=df2['Unnamed: 6'].str.split()

df3=pd.DataFrame(df2['Box Score'].tolist(), columns=['PassDiff','GreenPass','GreenPassed','QualityPasses','PercentQualityPasses','NumFastestLaps'])
df4=pd.DataFrame(df2['Unnamed: 6'].tolist(), columns=['LapsinTop15','PercentLapsTop15'])

df2=df2[['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
       'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 8',
       'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11']]

df2=df2.reset_index(drop=True)
df_final=pd.concat([df2,df3,df4],axis=1)
df_final.columns=HEADERS

df_final=df_final[['Car','Driver','AvgStart','AvgMidRace','AvgFinish','Avg Pos','PassDiff','GreenPass','GreenPassed','QualityPasses','PercentQualityPasses','NumFastestLaps','LapsinTop15','PercentLapsTop15','LapsLed','PercentLapsLed','TotalLaps','DriverRating','Pts']]
df_final.to_csv(data_output,index=False)