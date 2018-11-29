
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
"""


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        if len(time) < 5:
            return ""
        digits = []
        for digit in time:
            if digit != ':':
                digits.append(int(digit))

        start_time = (digits[0] * 10 + digits[1]) * \
            60 + digits[2]*10 + digits[3]
        min_elapsed_time = 24 * 60
        min_time = start_time
        for h1 in digits:
            for h2 in digits:
                hours = (h1*10 + h2)
                if hours < 0 or hours > 23:
                    continue
                for m1 in digits:
                    for m2 in digits:
                        mins = (m1*10 + m2)
                        if mins < 0 or mins > 59:
                            continue
                        curr_time = (hours * 60) + mins
                        elapsed_time = (curr_time - start_time) % (24*60)
                        #print elapsed_time, min_elapsed_time
                        if elapsed_time > 0 and elapsed_time < min_elapsed_time:
                            min_elapsed_time = elapsed_time
                            min_time = curr_time
        return "{:02d}:{:02d}".format(*divmod(min_time, 60))
