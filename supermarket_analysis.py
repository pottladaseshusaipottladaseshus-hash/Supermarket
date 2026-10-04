import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_sales.csv")

print("Total sales:", df["TotalSales"].sum())
print("\nSales by category:")
print(df.groupby("Category")["TotalSales"].sum())

print("\nSales by product:")
print(df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False))

df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()
