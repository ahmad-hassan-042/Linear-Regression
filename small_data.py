import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import linear_model 
import os

df = pd.read_excel('data.xlsx') 
plt.scatter(df['area'], df['price'], color = 'blue', marker = '+' )
plt.xlabel('Area'), plt.ylabel('Price') 
plt.show() 
model = linear_model.LinearRegression() 
new_df = df.drop('price', axis='columns') 
model.fit(new_df, df['price']) 

while True: 
    user_input = float(int(input("Enter your required Area to find out price: "))) 
    predicted_value = model.predict([[user_input]]) 
    print(predicted_value)
