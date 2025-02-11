# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution(object):
    def sortArray(self, nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_half = sorted(nums[:mid])
            right_half = sorted(nums[mid:])

            sorted_arr = []
            left_index = 0
            right_index = 0
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    sorted_arr.append(left_half[left_index])
                    left_index += 1
                else:
                    sorted_arr.append(right_half[right_index])
                    right_index += 1

            sorted_arr.extend(left_half[left_index:])
            sorted_arr.extend(right_half[right_index:])

            return sorted_arr
        



                
        