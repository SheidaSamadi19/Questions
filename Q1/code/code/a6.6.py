# Authors: Sheida Samadi , Baran Farrokhian
 
# Function
def count_animals(total_legs, total_heads):

# Loop
    for chickens in range(total_heads):

# Equation
        rabbits = total_heads - chickens
        if (chickens * 2) + (rabbits * 4) == total_legs:
            return chickens, rabbits

# Question
print("""question:  In a farm that has a number of chickens and rabbits, a count was made in which 94 chickens and 35 heads were counted.
 How many rabbits and chickens are there in this farm?
 """)

total_legs = 94
total_heads = 35
result = count_animals(total_legs, total_heads)

# Answers
print("Number of chickens:", result[0])
print("Number of rabbits:", result[1])