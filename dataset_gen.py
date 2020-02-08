#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:12:57 2019

@author: prawigya
"""

import random
import pandas as pd

#Define features
years_of_experience = [] #ranges from 1-12
hours_per_week=[] #Ranges from 25-60
job_type = [] #part time, full time, intern, other
jobtype=['full_time','intern']
hometown = [] #Do you work in your hometown? Yes/ No
yesno=['yes','no']
relationship_status = [] #single, married, in a relationship
relationship=['single','in_a_relationship','married']
recreational = [] #Values from 1 to 10
family_affected = [] #Values from 1 to 10
stressed = [] #Values from 1 to 10
exercise = [] #Values from 1-3
exercises=['regularly','sometimes','not_at_all']

happy=[]



#Happy People
"""
#Number of responses = 17

hours_per_week=[] #Ranges from 25-60 #Random
job_type = [] #part time, full time, intern, other #Random
hometown = [] #Do you work in your hometown? Yes/ No #Random
relationship_status = [] #single, married, in a relationship #Random
recreational = [] #Values from 1 to 10 #Ranges from 5-9
family_affected = [] #Values from 1 to 10 #Ranges from 
stressed = [] #Values from 1 to 10 #Ranges from 1-
exercise = [] #Values from 1-3 #Ranges from 2 to 3
happy = [] #All yes
"""
for i in range(17):
    years_of_experience.append(random.randint(1,12))
    hours_per_week.append(random.randint(25,60)) 
    job_type.append(jobtype[random.randint(0,1)])
    hometown.append(yesno[random.randint(0,1)])
    relationship_status.append(relationship[random.randint(0,2)])
    recreational.append(random.randint(5,10))
    family_affected.append(random.randint(1,4))
    stressed.append(random.randint(1,4)) 
    exercise.append(exercises[random.randint(0,2)])
    happy.append('yes')



#Medium People
"""
#Number of responses = 17

hours_per_week=[] #Ranges from 25-60 #Random
job_type = [] #part time, full time, intern, other #Random
hometown = [] #Do you work in your hometown? Yes/ No #Random
relationship_status = [] #single, married, in a relationship #Random
recreational = [] #Values from 1 to 10 #Ranges from 5-9
family_affected = [] #Values from 1 to 10 #Ranges from 
stressed = [] #Values from 1 to 10 #Ranges from 1-
exercise = [] #Values from 1-3 #Ranges from 2 to 3
happy = [] #All yes
"""
for i in range(17):
    years_of_experience.append(random.randint(1,12))
    hours_per_week.append(random.randint(35,60)) 
    
    job_type.append(jobtype[random.randint(0,1)])
    hometown.append(yesno[random.randint(0,1)])
    relationship_status.append(relationship[random.randint(0,2)])
    recreational.append(random.randint(4,8))
    family_affected.append(random.randint(3,8))
    stressed.append(random.randint(4,8)) 
    exercise.append(exercises[random.randint(0,2)])
    happy.append(yesno[random.randint(0,1)])



#Sad People
"""
#Number of responses = 17

hours_per_week=[] #Ranges from 25-60 #Random
job_type = [] #part time, full time, intern, other #Random
hometown = [] #Do you work in your hometown? Yes/ No #Random
relationship_status = [] #single, married, in a relationship #Random
recreational = [] #Values from 1 to 10 #Ranges from 5-9
family_affected = [] #Values from 1 to 10 #Ranges from 
stressed = [] #Values from 1 to 10 #Ranges from 1-
exercise = [] #Values from 1-3 #Ranges from 2 to 3
happy = [] #All yes
"""
for i in range(17):
    years_of_experience.append(random.randint(1,12))
    hours_per_week.append(random.randint(40,60)) 
    job_type.append(jobtype[random.randint(0,1)])
    hometown.append(yesno[random.randint(0,1)])
    relationship_status.append(relationship[random.randint(0,2)])
    recreational.append(random.randint(1,6))
    family_affected.append(random.randint(4,10))
    stressed.append(random.randint(5,10)) 
    exercise.append(exercises[random.randint(0,2)])
    happy.append('no')

data_frame = []
for i in range(len(happy)):
    if(job_type[i]=='intern'):
        relationship_status[i]=relationship[random.randint(0,1)]
        years_of_experience[i] = random.randint(1,3)
        hours_per_week[i] = random.randint(25,30)
    data_frame.append([years_of_experience[i], hours_per_week[i], job_type[i], hometown[i], relationship_status[i],
                       recreational[i], family_affected[i], stressed[i], exercise[i], happy[i]])

names = ['years_of_experience','hours_per_week','job_type','hometown','relationship_status','recreational','family_affected','stressed','exercise','happy']

df = pd.DataFrame(data_frame, columns = names)
df1 = df.sample(frac=1)
df1.to_csv('dataset.csv')


