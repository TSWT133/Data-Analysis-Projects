#!/usr/bin/env python
# coding: utf-8

# In[1]:


names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Creating For loop
total_cost = 0

for cost in actual_insurance_costs:
  total_cost += cost

print(total_cost)

average_cost = total_cost / len(actual_insurance_costs)

print("Average Insurance Cost:", average_cost)

# Using Range in Loops

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for", name, "is", insurance_cost)
  if insurance_cost > average_cost:
    print("The insurance cost for", name, "is above average")
  elif insurance_cost < average_cost:
    print("The insurance cost for", name, "is below average")
  else:
    print("The insurance cost for", name, "is equal to the average")

# The difference between actual cost and estimated is 10%

updated_estimated_costs = [round(cost*1.1) for cost in estimated_insurance_costs]

print("The updated estimate costs are: ", updated_estimated_costs)




# In[ ]:




