import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_csv('study.csv')
X = data['Study Hours'].values.reshape(-1,1)
Y = data['Exam Score'].values

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)
slope = model.coef_[0]
intercept = model.intercept_
print("Slope (Coefficient):", slope)
print("Y-Intercept:", intercept)

plt.scatter(X, Y, label='Actual Data')
plt.plot(X, Y_pred, color='red', label=f'Regression Line (y = {slope:.2f}x + {intercept:.2f})')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()
plt.title('Linear Regression: Study Hours vs. Exam Score')
plt.show()
new_SH = float(input("Enter the number of hours: "))
pred_Sc = model.predict(np.array([[new_SH]]))
print(f'Predicted Exam Score for {new_SH} study hours: {pred_Sc[0]:.2f}')
