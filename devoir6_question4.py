#!/usr/bin/env python3                                #Shebang

### Script description
#Create a random list between 0 and 100
#Calculate the mean, the maximum, minimum and the number of students who have passed the exam (>= 60)
#Return the numbers

import numpy

liste = numpy.random.randint(0, high=101, size=30)   #Generating randomly the exam scores list of 30 students

def main(liste) :                                    
    """
    Main function that runs the whole script: it prints the exam scores
    and the main statistics (mean, maximum, minimum, number of passing students).

    Parameters : liste (numpy.ndarray) - Array of exam scores (integers between 0 and 100).
    Returns : None - Nothing is returned, the results are printed to the console.
    """
    
    print("La liste des scores d'examen :\n", liste)
    print("La moyenne est",mean(liste),".")
    print("Le maximum est",maximum_score(liste), ".")
    print("Le minimum est",minimum_score(liste), ".")
    print("Le nombre d'étudiants ayant un score >= 60 est de", passed(liste), ".")
    
    return

def mean (check):                                    
    """
    Calculate the mean (average) of a list of scores.

    Parameters : check (numpy.ndarray) - Array of exam scores.
    Returns : numpy.float64 - Mean of all scores in the array.
    """
    
    return numpy.mean(check)

def maximum_score (insert):                                   
    """
    Find the highest score in a list of scores.

    Parameters : insert (numpy.ndarray) - Array of exam scores.
    Returns : numpy.int64 - Maximum score found in the array.
    """
    
    return numpy.max(insert)

def minimum_score (insert2):                                   
    """
    Find the lowest score in a list of scores.

    Parameters : insert2 (numpy.ndarray) - Array of exam scores.
    Returns : numpy.int64 - Minimum score found in the array.
    """
 
    return numpy.min(insert2)

def passed (students):                                
    """
    Count how many students passed the exam (score >= 60).

    Parameters : students (numpy.ndarray) - Array of exam scores, one per student.
    Returns : int - Number of students whose score is greater than or equal to 60.
    """
    
    count = 0
    for ajouter in range(len(students)):              #Check the whole list
        if students[ajouter] >= 60 :
            count = count+1
    return count

if __name__ == "__main__":                           # Guard the following block of code
    main(liste)