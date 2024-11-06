import pandas as pd
import numpy as np

num_rows = int(input("Enter the number of rows for orders: "))

#generate the series of dates between 2014 and 2024
random_dates=np.random.choice(np.arange(np.datetime64('2014-01-01'),np.datetime64('2024-07-20')),size=num_rows)
print(random_dates)

#change to int format
formatted_rows = pd.to_datetime(random_dates).strftime('%Y%m%d')
print(formatted_rows)

data = {
    'DateID':formatted_rows,
    'ProductID':np.random.randint(1,1001,size=num_rows),
    'StoreID':np.random.randint(1,101,size=num_rows),
    'CustomerID':np.random.randint(1,1001,size=num_rows),
    'QuantityOrdered':np.random.randint(1,21,size=num_rows),
    'OrderAmount':np.random.randint(100,1001,size=num_rows)
}

#tabular format
df = pd.DataFrame(data)
print(df)

#get discount amount
discount_perc = np.random.uniform(0.02,0.15,size=num_rows)
shipping_cost = np.random.uniform(0.05,0.15,size=num_rows)


#calculate columns
df['DiscountAmount'] = df['OrderAmount'] * discount_perc
df['ShippingCost'] = df['OrderAmount'] * shipping_cost
df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] +df['ShippingCost'])

print(df)

df.to_csv('factorders.csv',index=False)
