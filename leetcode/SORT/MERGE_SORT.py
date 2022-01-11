import random


def get_random_arr(count):
    return random.sample(range(100), count)


class Solution:
    def merge(self, arr, left, mid, right, temp):
        left_pos, right_pos, cur = left, mid + 1, 0
        while left_pos <= mid and right_pos <= right:
            if arr[left_pos] <= arr[right_pos]:
                temp[cur] = arr[left_pos]
                left_pos += 1
            else:
                temp[cur] = arr[right_pos]
                right_pos += 1
            cur += 1

        while left_pos <= mid:
            temp[cur] = arr[left_pos]
            cur += 1
            left_pos += 1
        while right_pos <= right:
            temp[cur] = arr[right_pos]
            cur += 1
            right_pos += 1

        for i in range(cur):
            arr[i + left] = temp[i]

    def msort(self, arr, left, right, temp):
        if left < right:
            mid = (left + right) // 2
            self.msort(arr, left, mid, temp)
            self.msort(arr, mid + 1, right, temp)
            self.merge(arr, left, mid, right, temp)

    def merge_sort(self, arr):
        print(arr)
        temp = [None] * len(arr)
        self.msort(arr, 0, len(arr) - 1, temp)
        print(arr)


if __name__ == '__main__':
    s = Solution()
    arr = get_random_arr(10)
    s.merge_sort(arr)
