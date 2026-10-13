#!/usr/bin/env python3                                #Shebang

### Script description
#Create a random list between 0 and 100
#Calculate the mean, the maximum, minimum and the number of students who have passed the exam (>= 60)
#Return the numbers

import numpy

liste = numpy.random.randint(0, high=100, size=30)   #Generating randomly the exam scores list of 30 students

def main(liste) :                                    #Main function that allows to execute the code correctly
    print("La liste des scores d'examen :\n", liste)
    print("La moyenne est",mean(liste),".")
    print("Le maximum est",max(liste), ".")
    print("Le minimum est",min(liste), ".")
    print("Le nombre d'étudiants ayant un score >= 60 est de", passed(liste), ".")
    return

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

if __name__ == "__main__":                           # Guard the following block of code
    main(liste)