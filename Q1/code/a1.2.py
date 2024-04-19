# Author: Sheida Samadi , Baran Farokhian


# Library
import numpy

# Functions
def Average(numbers_lists):
   numbers_sum = sum(numbers_lists)
   numbers_n = len(user_inputs)
   average = numbers_sum/numbers_n
   return average

def All_user_inputs():
     user_inputs = []
     len.user_inputs = 5

def user_input(x):
     
     try:
        x = str(x)

        user_input=float(input(x)) = True
        if (0 <= user_inputs <= 1)  # Condition that shows the number should be between 0 and 1
        user_inputs.append(user_input)

        except: Flase
        print ("The number isn't between 0 and 1. try again.")

# Function for Variance formula
def Variance(numbers_lists):
    numbers_sum = sum(numbers_lists)
    numbers_n = len(user_inputs)
    average = numbers_sum/numbers_n
    variance = ((((x-average)^2) * ((y-average)^2) * ((w-average)^2) * ((z-average)^2) * ((p-average)^2))/(numbers_n - 1) )
    return variance

# User inputs
x=float(input('number_1 :'))
y=float(input('number_2 :'))
w=float(input('number_3 :'))
z=float(input('number_4 :'))
p=float(input('number_5 :'))


# Make a list from user's inputs
user_inputs = [x,y,w,z,p]

# Calculate variance
user_inputs_variance = Variance(user_inputs)

# Print variance
print('Variance: '+str(user_inputs_variance))

# Calculate average
user_inputs_average = Average(user_inputs)

# Print average
print('Average: '+str(user_inputs_average))