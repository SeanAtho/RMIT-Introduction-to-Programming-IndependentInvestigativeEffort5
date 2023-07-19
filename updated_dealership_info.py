import sys

#Lists containing dealerships stock.
werribee_stock = ["Audi", "Kia", "Lotus", "Nissan", "Ford", "Honda", "Jeep"]
sunbury_stock = ["Fiat", "Land Rover", "Ford", "Kia", "BMW", "Volvo", "Audi"]
frankston_stock = ["Ram", "Mazda", "Toyota", "Ford", "Porsche", "Audi", "Volkswagen"]

#The function named "common stock" as it contains and verifies common stock across dealerships.
#Alternate names that could be considered are "common items" and "all stock". 
def common_stock():
    werribee = 0
    while(werribee < len(werribee_stock)):
        sunbury = 0
        while (sunbury < len(sunbury_stock)):
            frankston = 0
            while (frankston < len(frankston_stock)):
                if (werribee_stock[werribee]== sunbury_stock[sunbury] == frankston_stock[frankston]):
                    sys.stdout.write(werribee_stock[werribee].center(50)+ "\n")
                frankston +=1
            sunbury +=1
        werribee +=1

#*Refer Here for Remaining Functions Justification
#The function named "werribee_exclusive_stock" determines and displays results for items that
#are exclusive to Werribee by analysing all dealership lists.
#Alternate names that could be considered are "werribee_exclusive" and "werribee_only_stock",
#however placing the dealership name followed by repeated naming scheme of "exclusive_stock"
#identifies what intended outcome of function should be e.g. determing and displaying brands
#and or stock exclusive to the werribee dealership/list.
#Justification and similar alternatives apply to repeated functions.
def werribee_exclusive_stock():
    i=0
    while(i <len(werribee_stock)):
        if (sunbury_stock.count(werribee_stock[i]) + (frankston_stock.count(werribee_stock[i]))) < 1:
            sys.stdout.write(werribee_stock[i].center(50)+"\n")
        i+=1

#*Refer to Main Justification Comment for "Exclusive Dealerships" functions*    
def sunbury_exclusive_stock():
    i=0
    while(i<len(sunbury_stock)):
        if (werribee_stock.count(sunbury_stock[i]) + (frankston_stock.count(sunbury_stock[i]))) < 1:
              sys.stdout.write(sunbury_stock[i].center(50)+"\n")
        i+=1

#*Refer to Main Justification Comment for "Exclusive Dealerships" functions*    
def frankston_exclusive_stock():
    i=0
    while (i<len(frankston_stock)):
        if (werribee_stock.count(frankston_stock[i]) + (sunbury_stock.count(frankston_stock[i]))) < 1:
            sys.stdout.write(frankston_stock[i].center(50)+"\n")
        i+=1

        

