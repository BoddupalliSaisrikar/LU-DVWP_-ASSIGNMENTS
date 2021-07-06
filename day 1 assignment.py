# Assignment-1
# Sqaure of numbers

x = np.arange(0,10) # ouput : array([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9])
y = x*x # output : array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
plt.plot(x,y) #To plot a graph (line graph) between x and y.
plt.title("line plot of numbers and their squares.")
plt.xlabel("numbers")
plt.ylabel("square of numbers")
plt.show() # This is not mandatory as we have included %matplotlib inline at starting.

# Assignment -2 
# sales for days of week

x = [1,2,3,4,5,6,7] # days of week
y = [160,150,140,145,175,165,180] # sales
plt.plot(x,y) # Plot the graph 
plt.title("Sales for each day of a week")
plt.xlabel("Days of week")
plt.ylabel("sales")
plt.show()

# Assignment - 3
# Sales in a week between two companies

days = [1,2,3,4,5,6,7]  # days of week
sales_1 = [160,150,140,145,175,165,180]
sales_2 = [70,90,160,150,140,145,175]
plt.plot(days,sales_1)
plt.plot(days,sales_2)
plt.title("sales for each day in a week")
plt.xlabel("Days of week")
plt.ylabel("sales")
plt.show()
