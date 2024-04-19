# Author: Sheida Samadi , Baran Farokhian

# Library

# Variables: Global

# Functions
def Average(numbers_lists):
   numbers_sum = sum(numbers_lists)
   numbers_n = len(user_inputs)
   average = numbers_sum/numbers_n
   return average





# Conditions: C_*
# Print Conditions:
# Input validation
# Check condition: 5 inputs by user
# Print Results:
## Print user inputs

# Main 
## User inputs
x=float(input('number_1 :'))
y=float(input('number_2 :'))
w=float(input('number_3 :'))
z=float(input('number_4 :'))
p=float(input('number_5 :'))

# Make a list from user's inputs
user_inputs = [x,y,w,z,p]

# Calculate average
user_inputs_average = Average(user_inputs)

# Print average
print('Average: '+str(user_inputs_average))
