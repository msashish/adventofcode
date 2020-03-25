from builtins import list


class StairCase:

    def simple_recursive(self, N, rule: list):
        # Given N and rules say [1,2], number of ways to climb the stair is num_of_ways(N-1) + num_of_ways(N-2)
        if N == 0 or N == 1:
            if 1 in rule:
                return 1
            return 0
        result = 0
        for r in rule:
            if N - r > 0:
                result = result + self.simple_recursive(N-r, rule)
            if N - r == 0:
                # case where when N == r and hence there is always exactly 1 more way
                result = result + 1
        return result

    def find_using_dp(self, N, rule):
        # using Dynamic programming bottom up approach
        if N == 0 or N == 1:
            if 1 in rule:
                return 1
            return 0
        nums = [0] * (N+1)
        nums[0] = 1
        for i in range(1, N+1):
            result = 0
            for r in rule:
                if i - r > 0:
                    result = result + self.find_using_dp(i - r, rule)
                if i - r == 0:
                    # case where when i == r and hence there is always exactly 1 more way
                    result = result + 1
            nums[i] = result
        #print(nums)
        return nums[N]
