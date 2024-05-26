# Definition for singly-linked list.

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(hours)):
            if (hours[i] > target):
                return i
        else:
            return 0


test = Solution()

print(test.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2))
