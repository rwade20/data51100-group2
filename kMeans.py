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
