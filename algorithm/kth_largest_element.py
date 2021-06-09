'''
Kth Largest Element In An Array

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

역으로 sorting 한 다음
index에 맞게 리턴

'''
from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        heappush(self.heap, k)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val

        while( i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = (self.heap[self.parent(i)], self.heap[i])

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float('-inf'))
        self.extractMin()

    def getMin(self):
        return self.heap[0]


def find_kth_largest(nums, k):
    if(len(nums) == 0 or k > len(nums)):
        return -1
    sorted_arr = sorted(nums)

    return sorted_arr[len(nums) - k]


def find_kth_largest_two(nums, size, k):
    min_heap = []

    for i in range(k):
        min_heap.append(nums[i])

    for i in range(k, size):
        min_heap.sort()

        if (min_heap[0] > nums[i]):
            continue
        else:
            min_heap.pop(0)
            min_heap.append(nums[i])

    for i in min_heap:
        print(i, end = ' ')

(find_kth_largest_two([3, 2, 1, 4, 5, 6], 5, 2))  # return 5