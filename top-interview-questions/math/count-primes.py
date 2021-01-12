class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        primes = [False for i in range(n+1)]
        for i in range(2,n):
            if primes[i] == False:
                count+=1
                j = 2
            while j*i<n:
                 primes[j*i] = True
                 j+=1
        return count


solution = Solution()
assert solution.countPrimes(1) == 0
assert solution.countPrimes(10) == 4
assert solution.countPrimes(0) == 0
assert solution.countPrimes(499979) == 41537 # This one will take a long time



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