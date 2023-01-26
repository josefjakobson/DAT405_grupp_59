from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import get_data

living_area, selling_price = get_data.main()

model = LinearRegression()
model.fit(living_area, selling_price)
price_prediction = model.predict(living_area)
slope = model.coef_[0][0]
intercept = model.intercept_[0]

plt.scatter(living_area, selling_price)
plt.plot(living_area, price_prediction)
plt.xlabel("Living Area in square meters")
plt.ylabel("Selling price in SEK")
plt.title("Living Area vs Selling price in Landvetter 2020")
plt.show()


print(f"slope: {slope}, intercept: {intercept}")
print(f"Estimated price at 100 sq.m.: {slope*100 + intercept} \n")
print(f"Estimated price at 150 sq.m.: {slope*150 + intercept} \n")
print(f"Estimated price at 200 sq.m.: {slope*200 + intercept} \n")


