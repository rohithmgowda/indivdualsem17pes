#1a.
import pandas as pd
import matplotlib.pyplot as plt  

a = pd.read_csv("C:/Users/User/Documents/python/individual17/company_sales_data.csv")
profitList = a ['total_profit'].tolist()
monthList  = a ['month_number'].tolist()
plt.plot(monthList, profitList, label = "Month wise Profit data of last year")
plt.xlabel("Month number")
plt.ylabel("Profit in dollar")
plt.xticks(monthList)
plt.title("Company profit per month")
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()





#1b
 

onthList  = a ['month_number'].tolist()
faceCremSalesData   = a ['facecream'].tolist()
faceWashSalesData   = a ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper right')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Face wash and face cream sales data')
plt.show()


#1c  


monthList  = a ['month_number'].tolist()

labels = ['Face Cream', 'Face Wash', 'Tooth Paste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [a ['facecream'].sum(), 
a['facewash'].sum(), 
a ['toothpaste'].sum(), 
a ['bathingsoap'].sum(), 
a ['shampoo'].sum(), 
a ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()



#1d
  


monthList  = a ['month_number'].tolist()

faceCremSalesData   = a ['facecream'].tolist()
faceWashSalesData   = a ['facewash'].tolist()
toothPasteSalesData = a ['toothpaste'].tolist()
bathingsoapSalesData   = a ['bathingsoap'].tolist()
shampooSalesData   = a ['shampoo'].tolist()
moisturizerSalesData = a ['moisturizer'].tolist()

plt.plot([],[],color='c', label='face Cream', linewidth=5)
plt.plot([],[],color='m', label='Face wash', linewidth=5)
plt.plot([],[],color='k', label='Tooth paste', linewidth=5)
plt.plot([],[],color='g', label='Bathing soap', linewidth=5)
plt.plot([],[],color='r', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)
plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,bathingsoapSalesData, shampooSalesData, moisturizerSalesData, colors=['c','m','k','g','r','y'])
plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('All product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()



#1e
  


monthList  = a ['month_number'].tolist()

profitList = a ['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()