import numpy as np
grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("Grades: ",grades)
# What is the average (mean) grade in the class?
mean_result = np.mean(grades)
print("Average (mean) grade in the class: ",mean_result)
# How many students scored above 90?
above = np.count_nonzero(grades > 90)
print("Students scored above 90: ",above)
# Calculate the standard deviation of the grades.
std_deviation = np.std(grades)

