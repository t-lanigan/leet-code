class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0


        count = 0
        for i in range(2,n):
            if self.isPrime(i):
                count += 1

        return count


    def isPrime(self, n: int) -> bool:

        
        for i in range(2,n):
            if n % i == 0:
                return False

        return True


solution = Solution()
assert solution.countPrimes(1) == 0
assert solution.countPrimes(10) == 4
assert solution.countPrimes(0) == 0
print(solution.countPrimes(499979))



print("All tests passed!")


# public int countPrimes(int n) {
#    boolean[] isPrime = new boolean[n];
#    for (int i = 2; i < n; i++) {
#       isPrime[i] = true;
#    }
#    // Loop's ending condition is i * i < n instead of i < sqrt(n)
#    // to avoid repeatedly calling an expensive function sqrt().
#    for (int i = 2; i * i < n; i++) {
#       if (!isPrime[i]) continue;
#       for (int j = i * i; j < n; j += i) {
#          isPrime[j] = false;
#       }
#    }
#    int count = 0;
#    for (int i = 2; i < n; i++) {
#       if (isPrime[i]) count++;
#    }
#    return count;
# }