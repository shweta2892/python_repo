class Solution:
    def reverse(self, x: int) -> int:
        def helper(x, rev):
            if x == 0:
                return rev

        # Check for overflow before multiplication
            if abs(rev) > 2**31 // 10:
                return 0

            rem = x % 10
            rev = rev * 10 + rem
            return helper(x // 10, rev)

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = helper(x, 0) * sign

    # Check for overflow one more time

        return result if -2**31 <= result <= 2**31 - 1 else 0
        