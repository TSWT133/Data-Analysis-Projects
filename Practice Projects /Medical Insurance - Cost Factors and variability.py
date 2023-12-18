#!/usr/bin/env python
# coding: utf-8

# In[7]:


# create the initial variables below
age = 28
sex = 0 
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is",  insurance_cost, "dollars")
# Age Factor
age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who are 4 years older have an estimated cost increase of", change_in_insurance_cost, "dollars")
# older people tend to have a higher insurance

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who have a BMI of 3.1 higher have an estimated cost increase of", change_in_insurance_cost, "dollars")

# individuals with a higher bmi have a higher insurance cost

# Male vs. Female Factor
bmi = 26.2
sex += 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who are Male instead of female have an estimated cost decrease of", change_in_insurance_cost, "dollars")

# Males have lower medical costs on average compared to Females

# Extra Practice
# Children Factor
sex = 0
num_of_children += 2
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who have 2 extra children have an estimated cost increase of", change_in_insurance_cost, "dollars")
# Having more children increases medical costs

#Smoking Factor
num_of_children = 3
smoker += 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("People who smoke have an estimated cost increase of", change_in_insurance_cost, "dollars")
# Smoking is the biggest factor in medical insurance costs

