#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def search(candidates, target, temp, result):
            if target < 0:
                return
            if target == 0:
                result.append(temp)
            for i in range(len(candidates)):
                temp.append(candidates[i])
                search(candidates[i:], target - candidates[i], temp, result)
                temp.pop(-1)
        result = []
        temp = []
        search(candidates, target, temp, result)
        return result

        result = []
        curr = []
        self.backTrack(candidates, target, curr, result)
        return result


    def backTrack(self, candidates, target, curr, result):
        # base case
        if target < 0:
            return
        if target == 0:
            result.append(curr[:])
            return
            
        for i in range(len(candidates)):
            # make decision
            curr.append(candidates[i])
            # forward
            self.backTrack(candidates[i:], target-candidates[i], curr, result)
            # cancle decision
            curr.pop(-1)

        

        
# @lc code=end

