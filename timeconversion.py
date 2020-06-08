

def timeconversion(s):
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    :param s: a string representing time in 12 hour format (hh:mm:ssAM | hh:mm:ssPM)
    :return: the given time in 24-hour format
    Sample Input
    07:05:45PM
    Sample Output
    19:05:45
    """
    tarray = s.split(':')  # create a array to hold separate hour, minute, and secondAMPM values
    if tarray[2][-2:] == 'PM' and tarray[0] != '12':  # convert all PM values starting at 1:00
        hour = int(tarray[0])
        hour += 12
        tarray[0] = str(hour)
    if tarray[2][-2:] == 'AM' and tarray[0] == '12':  # convert AM values before 1:00
        tarray[0] = '00'
    tarray[2] = tarray[2][:2] #drop AMPMs
    return ':'.join(tarray)
