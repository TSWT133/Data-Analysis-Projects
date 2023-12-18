#!/usr/bin/env python
# coding: utf-8

# In[1]:


paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

paintings = list(zip(paintings, dates))

paintings.append(["The Broken Column", 1944])
paintings.append(["The Wounded Deer", 1946])
paintings.append(["Me and My Doll", 1937])

length_of_paintings = len(paintings)
audio_tour_number = []
id_num = 1

for id_num in range(length_of_paintings):
  audio_tour_number.append(id_num+1)

master_list = list(zip(paintings, audio_tour_number))
print("This is the master list in order for the audio tour: ", master_list)


# In[ ]:




