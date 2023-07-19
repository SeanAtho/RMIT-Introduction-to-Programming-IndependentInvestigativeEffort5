import sys

#Imports all functions contained within the "updated_dealership_info" module.  
from updated_dealership_info import *

#Only displays brands available across all dealerships, this is done through a sys write
#with a standard interface like text and a call to the "common_stock" function defined in
#the imported .py file. 
sys.stdout.write("\nFollowing car brands available at all dealerships:\n")
common_stock()
sys.stdout.write("\n")

#Only displays brands exclusive to the Werribee dealership, this is done through a sys write
#with a standard interface like text and a call to the "werribee_exclusive_stock" function defined
#in the imported .py file. 
sys.stdout.write("\nFollowing car brands are exclusive to the Werribee dealership:\n")
werribee_exclusive_stock()
sys.stdout.write("\n")

#Only displays brands exclusive to the Sunbury dealership, this is done through a sys write with
#a standard interface like text and a call to the "sunbury_exclusive_stock" function defined in the
#imported .py file. 
sys.stdout.write("\nFollowing car brands are exclusive to the Sunbury dealership:\n")
sunbury_exclusive_stock()
sys.stdout.write("\n")

#Only displays brands exclusive to the Frankston dealership, this is done through a sys write with
#a standard interface like text and a call to the frankston_exclusive_stock function defined in the
#imported .py file. 
sys.stdout.write("\nFollowing car brands are exclusive to the Frankston dealership:\n")
frankston_exclusive_stock()
sys.stdout.write("\n")

