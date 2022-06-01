class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        b = [0] * (n + 1)
        for i in bookings:
            b[i[0] - 1] += i[-1]
            b[i[1]] -= i[-1]
        ans = [0] * (n + 1)
        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] + b[i - 1]
        return ans[1:]