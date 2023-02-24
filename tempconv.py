celsius=  float(input("Please enter the temparature in celsius: "))

fahrenheit= (celsius * 1.8) + 32
print('%0.1f degree Celcius is equal to %0.1f degree fahrenheit'%(celsius,fahrenheit))

temp= fahrenheit
if (temp >= 104):
    print("It's hot")

elif (temp <= 50):
    print("its cold")

else:
    print("the temprature is nice")