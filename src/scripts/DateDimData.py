#import pandas library
import pandas as pd

#start date and end date between dates to be generated
start_date = '2014-01-01'
end_date = '2024-12-31'

#generate a series of dates between the dates
date_range=pd.date_range(start=start_date, end=end_date)
#print(date_range)

#convert these series of dates into a data frame
date_dimension = pd.DataFrame(date_range,columns=['Date'])
#print(date_dimension)

#add new columns to our dataframe
date_dimension['DayofWeek'] = date_dimension['Date'].dt.dayofweek
date_dimension['Month'] = date_dimension['Date'].dt.month
date_dimension['Quarter'] = date_dimension['Date'].dt.quarter
date_dimension['Year'] = date_dimension['Date'].dt.year
date_dimension['IsWeekend'] = date_dimension['DayofWeek'].isin([5,6])
date_dimension['DateId'] = date_dimension['Date'].dt.strftime('%Y%m%d').astype(int)
#print(date_dimension)

#reorder our data frame so that the dateid becomes the 1st column
cols = ['DateId'] + [col for col in date_dimension.columns if col != '']
date_dimension=date_dimension[cols]

#export it into a csv. Index column to be ignored
date_dimension.to_csv('DimDate.csv',index=False)