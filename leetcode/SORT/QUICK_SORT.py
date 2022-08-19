class Solution:
    def quick_sort_stack(self, arr, l, r):
        if l >= r:
            return arr
        left, right = l, r
        base = arr[left]

        while left < right:
            while left < right and arr[right] >= base:
                right -= 1
            arr[left] = arr[right]

            while left < right and arr[left] < base:
                left += 1
            arr[right] = arr[left]

        arr[left] = base
        # 先排左边
        self.quick_sort_stack(arr, l, right - 1)
        # 再排右边
        self.quick_sort_stack(arr, right + 1, r)

        return arr

    def quick_sort_ite(self, arr, l, r):
        if l >= r:
            return arr

        stack = []
        stack.append(l)
        stack.append(r)
        while stack:
            l, r = stack.pop(0), stack.pop(0)
            if l >= r:
                continue
            base = arr[l]
            left, right = l, r
            while left < right:
                while left < right and arr[right] < base:
                    right -= 1
                arr[left] = arr[right]
                while left < right and arr[left] > base:
                    left += 1
                arr[right] = arr[left]
            arr[left] = base
            stack.extend([l, left - 1, left + 1, r])

        return arr


if __name__ == '__main__':
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    s = Solution()
    # s.quick_sort_ite(lists, 0, len(lists) - 1)
    s.quick_sort_stack(lists, 0, len(lists) - 1)
    print(lists)
