class Solution:
    def fib(self, n: int) -> int:
        # dp approach: just build an arr of values
        arr = [0, 1]

        for i in range(n-1): # if n = 1, don't need to do steps
            num = arr[-1] + arr[-2]
            arr.append(num)
        
        return arr[n]

