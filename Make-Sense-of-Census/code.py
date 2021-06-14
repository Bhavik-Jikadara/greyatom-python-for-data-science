# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
census= np.concatenate((data,new_record), axis=0)
print(census)

#Code starts here
age = np.array(census[:,0])
print(age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)

race_0 = np.array(census[:,2] == 0)
print(race_0)
race_1 = np.array(census[:,2] == 1)
print(race_1)
race_2 = np.array(census[:,2] == 2)
print(race_2)
race_3 = np.array(census[:,2] == 3)
print(race_3)
race_4 = np.array(census[:,2] == 4)
print(race_4)

len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)

if len(race_0) < len(race_1) and len(race_0) < len(race_2) and len(race_0) < len(race_3) and len(race_0) < len(race_4):
   minority_race = 0
   print(minority_race)
elif len(race_1) < len(race_0) and len(race_1) < len(race_2) and len(race_1) < len(race_3) and len(race_1) < len(race_4):
   minority_race = 1
   print(minority_race)
elif len(race_2) < len(race_0) and len(race_2) < len(race_1) and len(race_2) < len(race_3) and len(race_2) < len(race_4):
   minority_race = 2
   print(minority_race)
elif len(race_3) < len(race_0) and len(race_3) < len(race_1) and len(race_3) < len(race_2) and len(race_3) < len(race_4):
   minority_race = 3
   print(minority_race)
elif len(race_4) < len(race_0) and len(race_4) < len(race_1) and len(race_4) < len(race_2) and len(race_4) < len(race_3):
   minority_race = 4
   print(minority_race)

senior_citizens = census[census[:,0]>60]
print(senior_citizens)

working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)



# --------------
#Code starts here
#import statistics
high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


np.array_equal(avg_pay_high, avg_pay_low)









