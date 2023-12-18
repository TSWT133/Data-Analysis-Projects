#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Create 2d list with insurance cost of each person
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150, 5320, 35210]
insurance_data = list(zip(names, insurance_costs))
print(insurance_data)

# Creating empty list and appending data
estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

print(estimated_insurance_data)

#Inspecting datasets
print("Here is the actual insurance cost data: ", insurance_data)
print("Here is the estimated insurance cost data: ", estimated_insurance_data)

# Calculating cost difference and creating a new list

maria_cost_difference =  maria_insurance_cost - 4150
rohan_cost_difference = rohan_insurance_cost - 5320 
valentina_cost_difference = valentina_insurance_cost - 35210 

insurance_cost_difference = [
  ["Maria", maria_cost_difference], ["Rohan", rohan_cost_difference], ["Valentina", valentina_cost_difference] 
]
print("Here is the difference in cost between actual and estimated: ", insurance_cost_difference)

print("From the analysis we can see that for each person, the estimated cost was more than the actual cost")



# In[ ]:




