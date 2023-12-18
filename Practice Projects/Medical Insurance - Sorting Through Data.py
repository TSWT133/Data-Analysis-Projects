#!/usr/bin/env python
# coding: utf-8

# In[1]:


names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Exploring List Data

names.append("Priscilla")
insurance_costs.append(8320)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are ", num_medical_records, " medical records")

# Selecting List Elements

first_medical_record = medical_records[0]
print("Here is the first medical record: ", first_medical_record)

# Sorting Lists

sorted_medical_records = sorted(medical_records)
print("Here are the medical records sorted by insurance cost", sorted_medical_records)

# Slicing Lists

cheapest_three = sorted_medical_records[0:3]
print("Here are the three cheapest insurance costs in our medical records: ", cheapest_three)

priciest_three = sorted_medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: ", priciest_three)

# Counting Elements

occurences_paul = names.count("Paul")
print("There are ", occurences_paul, " individuals with the name Paul in our medical records")

# Extra Practice

medical_records_by_name = list(zip(names, insurance_costs))
medical_records_by_name.sort()
middle_five_records = medical_records_by_name[3:8]
print("Here are the middle 5 insurance records sorted by name: ", middle_five_records)


# In[ ]:




