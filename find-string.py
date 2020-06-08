
import io
import sys


def count_substring(string, sub_string):
    """
    The user enters a string and a substring. You have to print the number of times that the substring occurs in the
     given string. NOTE: String letters are case-sensitive.
    Input Format: The first line of input contains the original string. The next line contains the substring.
    Constraints:
    Each character in the string is an ascii character.
    Output Format:
    Output the integer number indicating the total number of occurrences of the substring in the original string.
     """
    match = 0  # initialize return value
    sublength = len(sub_string)
    limit = len(string) - sublength + 1  # stop iterating when too few chars left for a substring
    for index in range(limit):
        matching = 0
        for ind, char in enumerate(string[index:]):
            if ind == sublength:
                break
            if char != sub_string[ind]:
                break
            matching += 1
            if matching == sublength:
                match += 1
    print(match)  # for command line use
    return match  # for other uses


if __name__ == '__main__':

    # You may enter string and sub string in the command line or via a text file.
    # If a text file: the string and sub string are written on separate lines.

    try:
        string, sub_string = open('input01.txt')
    except:
        string, sub_string = input("Enter a string followed by a sub string, separated by a space \n").split()
    count_substring(string, sub_string)
