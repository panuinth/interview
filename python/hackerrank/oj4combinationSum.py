class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates = [ i for i in candidates if i <= target] 
        self.dp_get(candidates, target)

    def dp_get(self, arr, target, partial=[]):
        s = sum(partial)

        if s == target:
            print partial
        if s > target:
            return

        for i in range(len(arr)):
            n = arr[i]
            remaining = arr[i+1:]
            if sum(partial + [n]) <= target:
                self.dp_get(remaining, target, partial + [n])


def test():
    for i in [([10,1,2,7,6,1,5], 8),
            #([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19], 25)
            ]:
        Solution().combinationSum2(i[0], i[1])

test()
