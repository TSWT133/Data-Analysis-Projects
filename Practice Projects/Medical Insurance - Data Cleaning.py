#!/usr/bin/env python
# coding: utf-8

# In[1]:


medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# 
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

num_records = 0
for records in updated_medical_data:
  if records == "$":
    num_records += 1
print("There are {} medical records in the data".format(num_records))

medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

medical_records = []

for records in medical_data_split:
  medical_records.append(records.split(","))
print(medical_records)

medical_records_clean = []

for records in medical_records:
  records_clean = []
  for item in records:
    records_clean.append(item.strip())
  medical_records_clean.append(records_clean)

print(medical_records_clean)

for records in medical_records_clean:
  records[0] = records[0].upper()
  print(records[0])

names = []
ages = []
bmis = []
insurance_costs = []

for records in medical_records_clean:
  names.append(records[0])
  ages.append(records[1])
  bmis.append(records[2])
  insurance_costs.append(records[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = round(total_bmi / len(bmis), 4)
print((("Average BMI: {}").format(average_bmi)))

fixed_insurance_costs = []

for costs in insurance_costs:
  fixed_insurance_costs.append(float(costs.replace("$", "")))
print(fixed_insurance_costs)

total_cost = 0
for costs in fixed_insurance_costs:
  total_cost += costs
average_insurance_costs = total_cost / len(fixed_insurance_costs)


print("The total cost is: $", total_cost)
print("The average cost is: $", average_insurance_costs)

for record in medical_records_clean:
  names = record[0]
  ages = record[1]
  bmis = record[2]
  insurance_costs = record[3]
  print("{} is {} years old with a BMI of {} and an insurance cost of {}".format(names, ages, bmis, insurance_costs))
 



# In[ ]:




