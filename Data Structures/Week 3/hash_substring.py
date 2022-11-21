# python3

def PolyHash (pattern, prime, n):
    
    mod = 1000000007  
    ans = (ord(pattern[0]) - ord('a') + 1)%mod

    for i in range(1, n):
        ans = (ans*prime + (ord(pattern[i]) - ord('a') + 1))%mod 
        
    return ans

def precomputeHashes(text, n, prime):
    m = len(text)
    curr_hash = PolyHash(text, prime, n)
    H=[]
    H.append(curr_hash)
    mod = 1000000007 

    y = 1
    for i in range (1,n):
        y = (y*prime)%mod

    for i in range(1, len(text) - n + 1):
        curr_hash = ((curr_hash - (ord(text[i-1]) - ord('a') + 1)*y)*prime + (ord(text[i + n - 1]) - ord('a') + 1))%mod
        if curr_hash <0:
            curr_hash = curr_hash + mod
        
        H. append(curr_hash)

    return H

def AreEqual(S_1, S_2):
    if len(S_1) != len(S_2):
        return False
    for i in range(len(S_1)):
        if S_1[i] != S_2[i]:
            return False
    return True



def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    #print(output)

def get_occurrences(pattern, text):
    prime = 101
    positions = []
    n = len(pattern)
    pHash = PolyHash(pattern, prime, n)
    H = precomputeHashes(text,n,prime)

    for i in range(len(text) - n + 1):
        if pHash != H[i]:
            continue
        if text[i:i+n] == pattern :
            positions.append(i)
    return positions
    
    # return [
    #     i 
    #     for i in range(len(text) - len(pattern) + 1) 
    #     if text[i:i + len(pattern)] == pattern
    # ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

