"""
Solution 1:

3 Pointers

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        res = []
        x1, x2, x3 = 0, 0, 0
        while x1 < len(arr1) and x2 < len(arr2) and x3 < len(arr3):
            if arr1[x1] == arr2[x2] and arr2[x2] == arr3[x3]:
                res.append(arr1[x1])
                x1 += 1
                x2 += 1
                x3 += 1
            elif arr1[x1] < arr2[x2] and arr1[x1] < arr3[x3]:
                x1 += 1
            elif arr2[x2] < arr1[x1] and arr2[x2] < arr3[x3]:
                x2 += 1
            elif arr3[x3] < arr1[x1] and arr3[x3] < arr2[x2]:
                x3 += 1
            elif arr3[x3] == arr1[x1] and arr3[x3] < arr2[x2]:
                x1 += 1
                x3 += 1
            elif arr2[x2] == arr1[x1] and arr2[x2] < arr3[x3]:
                x1 += 1
                x2 += 1
            else:
                x2 += 1
                x3 += 1

        return res


"""
Solution 2:

Confined Version

We don't have to move the pointer pointing to the smallest number  
**We only need to move the pointer pointing to a smaller number**

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        res = []
        x1, x2, x3 = 0, 0, 0
        while x1 < len(arr1) and x2 < len(arr2) and x3 < len(arr3):
            if arr1[x1] == arr2[x2] and arr2[x2] == arr3[x3]:
                res.append(arr1[x1])
                x1 += 1
                x2 += 1
                x3 += 1
            else:
                if arr1[x1] > arr2[x2]:
                    x2 += 1
                elif arr2[x2] > arr3[x3]:
                    x3 += 1
                else:
                    x1 += 1

        return res
