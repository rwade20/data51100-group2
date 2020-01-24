# -*- coding: utf-8 -*-
"""
This program computes the mean and variance of user inputted values using online algorithms
Students:   Jenna Lopes, Geoffrey Stewart, Ryan Wade
Date:       Jan. 23, 2020
Course:     DATA-51100-002: 	Statistical Programming
Semester:   Spring 2020
Assignment: PROGRAMMING ASSIGNMENT #2

"""


def get_user_input():
    """
    A method to get handle retrieving the user's input for number of clusters.

    :return: the integer, representing the number of clusters as entered by the user
    """
    valid_integer = False
    # loop until a valid input was provided
    while not valid_integer:
        try:
            num_clusters = int(input("Enter the number of clusters: "))
            if num_clusters >= 0:
                valid_integer = True
                return num_clusters
            else:
                print('A negative number was provided, but a positive integer is required.')
                print('')
        except Exception as e:
            print(e)
            print('An invalid number was provided, a positive integer is required.')
            print('')
            
def average(l):
    # Accepts a numeric list and returns the average of the values in that list.
    return sum(l)/float(len(l))
     
def distance(p, q):
    # Accepts values and returns the distance between them.
       #Note: the distance is always a positive integer.
    return abs(p - q)
    
def initialize(values, k):
    # Accepts a numeric list and the number of groups to be created.
       Initializes the module based on the supplied values.
       
       if k < len(values):
        global groups
        groups = [ [x, [x], values.index(x)] for x in values[0:k] ]
        groups.sort()
        
        for value in values[k:len(values)]:
            group = find_best_group(value, groups)
            group[1].append(value)
            
def find_best_group(p, l):
    # this function does a binary search to locate and return the group with the nearest mean value.
    if len(l) == 1:
        return l[0];
        
    midpoint = int((len(l)-1) / 2)
    d1 = distance(p, l[midpoint][0])
    d2 = distance(p, l[midpoint + 1][0])
    
    if d1 < d2:
        return find_best_group(p, l[0:midpoint + 1])

    return find_best_group(p, l[midpoint + 1:len(l)])


def main():
    # log the required output header
    print('DATA-51100, Spring 2020')
    print('NAMES: Jenna Lopes, Geoffrey Stewart, Ryan Wade')
    print('PROGRAMMING ASSIGNMENT #2')
    print('')

    num_clusters = get_user_input()
    print('')

    with open('prog2-input-data.txt') as f:
        list_of_points = [float(x.rstrip()) for x in f]

    # TODO: remove these debug print statements
    print('num_clusters is: %d' % num_clusters)
    print('list of points is: %s' % list_of_points)


if __name__ == "__main__":
    main()
