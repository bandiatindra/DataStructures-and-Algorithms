def PolyHash (pattern, prime):
    #pattern = 'geeksforgeeks'

    prime = 31
    pow = prime
    mod = 1000000007
    ans = ord(pattern[0]) - ord('a') + 1


    for i in range(1, len(pattern)):
        ans = (ans + (ord(pattern[i]) - ord('a') + 1)*pow)%mod 
        pow = (pow * prime)%mod
    return ans

