import matplotlib.pyplot as plt
months = ["January", "February", "March", "April", "May", "June"]

product_A = [120, 150, 170, 160, 180, 200]
product_B = [100, 120, 140, 150, 170, 190]
product_C = [90, 110, 130, 120, 150, 160]

totals = [sum(product_A), sum(product_B), sum(product_C)]
products = ["Product A", "Product B", "Product C"]

plt.figure(figsize=(15,5))


plt.subplot(1,3,1)
plt.plot(months, product_A, marker='o', label="Product A")
plt.plot(months, product_B, marker='s', label="Product B")
plt.plot(months, product_C, marker='^', label="Product C")

plt.title("Monthly Sales Comparison")
plt.legend()
plt.grid(True)


plt.subplot(1,3,2)
plt.bar(products, totals, color=['blue','orange','green'])

plt.title("Total Sales per Product")
plt.xlabel("Products")
plt.ylabel("Total Sales")


plt.subplot(1,3,3)
plt.scatter(product_A, product_C, color='purple')

plt.title("Relationship between Product A and Product C Sales")
plt.xlabel("Product A Sales")
plt.ylabel("Product C Sales")

plt.tight_layout()
plt.show()


