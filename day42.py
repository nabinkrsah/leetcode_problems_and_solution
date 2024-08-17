'''class Solution(object):
    def sortJumbled(self, mapping, nums):
        def mapped_value(num):
            return int("".join(str(mapping[int(digit)]) for digit in str(num)))
        return sorted(nums, key=mapped_value)
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        '''
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left_half = nums[:mid]
                right_half = nums[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0

                # Merge the sorted halves
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        nums[k] = left_half[i]
                        i += 1
                    else:
                        nums[k] = right_half[j]
                        j += 1
                    k += 1

                # Copy the remaining elements of left_half, if any
                while i < len(left_half):
                    nums[k] = left_half[i]
                    i += 1
                    k += 1

                # Copy the remaining elements of right_half, if any
                while j < len(right_half):
                    nums[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(nums)
        return nums


