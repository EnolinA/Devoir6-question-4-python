#!/usr/bin/env python3                                #Shebang

### Script description
#Create a random list between 0 and 100
#Calculate the mean, the maximum, minimum and the number of students who have passed the exam (>= 60)
#Return the numbers

import numpy

liste = numpy.random.randint(0, high=100, size=30)   #Generating randomly the exam scores list of 30 students

def mean (check):                                    #Calcultate de mean of the list given
    return numpy.mean(check)

def max (insert):                                    #Determine the maximum of the list given
    maximum = numpy.max(insert)
    return maximum

def min (insert2):                                   #Determine the minimum of the list given
    minimum = numpy.min(insert2)
    return minimum

def passed (students):                                #Determine how many students have above or equal 60/100
    count = 0
    for ajouter in range(len(students)):              #Check the whole list
        if students[ajouter] >= 60 :
            count = count+1
    return count