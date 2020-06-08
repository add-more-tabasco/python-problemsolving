#!Python3


def reversevowels(s):
    """
    Write a function that takes a string as input and reverses only the vowels of a string.
    Example 1:
    Input: "hEllo"
    Output: "hollE"
    Example 2:
    Input: "leetcode"
    Output: "leotcede"
    Note: The vowels does not include the letter "y".

    :type s: str
    :return type: str
    """

    # deal with simplest cases:
    if len(s) < 2:
        return s

    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

    # O(n):

    chars = list(s)  # turn string to list to make it mutable
    left = 0
    right = len(chars)-1  # set pointers to first and last index of the string
    while left < right:
        if chars[left] in vowels:  # get to the first vowel, if any
            while right > left:
                if chars[right] in vowels:  # if there's another vowel, compare them
                    if chars[left] != chars[right]:  # switch them unless they're the same
                        chars[left], chars[right] = chars[right], chars[left]
                    right -= 1
                    break
                right -= 1  # decrement right and increment left pointers until sweep is done
        left += 1
    return ''.join(chars)


# uncomment to run tests
# if __name__ == '__main__':
#     samps = ['sample-test word', '', 'o', 'ao', 'il', 'pop', 'opo', 'oppo', 'koopa', 'abcd efghi', 'zebra',
#         'kkkokkk', 'aiueo', 'bcdfghi', 'bcdfghio', 'avv0vva']
#     for samp in samps:
#         print(reversevowels(samp))