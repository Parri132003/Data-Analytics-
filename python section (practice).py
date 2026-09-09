'''

  practice session:

# price of product-->5000
Discount--> 10%
GST--> 18%
Find price of the product?
input--> price ,discount, gst
output--> final price
Logic--> operators

#price = 5000#check the type(price)
#accessing input from the user
price = 5000 # check yhe type(price)
discount = 0.1 #type (discount)
discount =float(input("Enter the discount in between 0.1- 0.2:"))
gst = 0.18

final_price  = (price -(price *discount))
final_price = final_price + (final_price*gst)
print ("Final_price  is:",final_price)

'''

# operators--> arthimetic,assignment,comparision,membership,logical,
#Identity,Bitwise...

# assignment --> = (assigning), += (update the value)

price = 2500
#New prce is adding 500 rupees extra
# price = price +500 # price += 500
price+=500
print(price)

#comparision--> compare the value  < ,> ,<=,>=,==,!=
#membership--> in ,not in --> check for the values in a collection

# we will have diff prices -> diff discount--> gst same
prices = [15000,2000,13000,25000,35000]
#price <= 15000 10%
#price > 5000--> to apply a discount
#price> 20000--> 15%

#get the final prices in a list
final_prices = []
for  price in prices:
    #print(price)
    if price <= 15000 and price>5000:
        price = price -( price*0.1)
        final_prices. append(int(price))
    elif price > 20000:
        price = price -(price *0.15)
        final_prices .append(int(price))
    elif price <5000:
        final_prices. append(price)
print(final_prices)
    























# we will have diff 






