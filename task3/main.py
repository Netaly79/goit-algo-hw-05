import timeit

def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def booyer_moore(text,pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return print("position: [", i, ']') 

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return print("No match found")

def knutt_compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0

        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

def knuth_morris_pratt(text, pattern):
    pi = knutt_compute_prefix_function(pattern)

    n = len(text)
    m = len(pattern)

    result = []
    q = 0

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]

        if pattern[q] == text[i]:
            q += 1

        if q == m:
            result.append(i - m + 1)
            q = pi[q - 1]

    return print("position: ", result)  if result else print("No match found")

def hash_function(s):
    return sum(ord(s[i]) * 256**(len(s) - 1 - i) for i in range(len(s)))

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    pattern_hash = hash_function(pattern)
    current_hash = hash_function(text[:m])

    result = []
    for i in range(n - m + 1):
        if current_hash == pattern_hash and text[i:i+m] == pattern:
            result.append(i)

        if i < n - m:
            current_hash = (current_hash - ord(text[i]) * 256**(m - 1)) * 256 + ord(text[i + m])

    return print("position: ", result) if result else print("No match found")


def main():
    with open('note1.txt', 'r') as file1:
        article1 = file1.read()

    with open('note2.txt', 'r') as file2:
        article2 = file2.read()
  
    pattern1 = "Висновки"
    print('----------------------------------------------------------------') 
    print("Trying to find existing pattern\n")

    print("----\nBooyer_Moore")
    booyer_moore_time = timeit.timeit(lambda: booyer_moore(article1, pattern1), number=1)
    print("1 article Time:", round(booyer_moore_time,5), " seconds")
    booyer_moore_time = timeit.timeit(lambda: booyer_moore(article2, pattern1), number=1)
    print("2 article Time:", round(booyer_moore_time,5) , " seconds")

    print("----\nKnuth_Morris_Pratt")
    knuth_morris_pratt_time = timeit.timeit(lambda: knuth_morris_pratt(article1, pattern1), number=1)
    print("1 article Time:", round(knuth_morris_pratt_time,5), " seconds")
    knuth_morris_pratt_time = timeit.timeit(lambda: knuth_morris_pratt(article2, pattern1), number=1)
    print("2 article Time:", round(knuth_morris_pratt_time,5), " seconds")

    print("----\nRabin_Karp")
    rabin_karp_time = timeit.timeit(lambda: rabin_karp(article1, pattern1), number=1)
    print("1 article Time:", round(rabin_karp_time,5), " seconds")
    rabin_karp_time = timeit.timeit(lambda: rabin_karp(article2, pattern1), number=1)
    print("2 article Time:", round(rabin_karp_time,5), " seconds")
    print('----------------------------------------------------------------')

    pattern2 = "Vysnovki "
    print("Trying to find not existing pattern\n")

    print("----\nBooyer_Moore")
    booyer_moore_time = timeit.timeit(lambda: booyer_moore(article1, pattern2), number=1)
    print("1 article Time:", round(booyer_moore_time,5), " seconds")
    booyer_moore_time = timeit.timeit(lambda: booyer_moore(article2, pattern2), number=1)
    print("2 article Time:", round(booyer_moore_time,5) , " seconds")

    print("----\nKnuth_Morris_Pratt")
    knuth_morris_pratt_time = timeit.timeit(lambda: knuth_morris_pratt(article1, pattern2), number=1)
    print("1 article Time:", round(knuth_morris_pratt_time,5), " seconds")
    knuth_morris_pratt_time = timeit.timeit(lambda: knuth_morris_pratt(article2, pattern2), number=1)
    print("2 article Time:", round(knuth_morris_pratt_time,5), " seconds")

    print("----\nRabin_Karp")
    rabin_karp_time = timeit.timeit(lambda: rabin_karp(article1, pattern2), number=1)
    print("1 article Time:", round(rabin_karp_time,5), " seconds")
    rabin_karp_time = timeit.timeit(lambda: rabin_karp(article2, pattern2), number=1)
    print("2 article Time:", round(rabin_karp_time,5), " seconds")

if __name__ == "__main__":
    main()
