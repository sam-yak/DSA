def character_replacement(s, k):
    freq = {}
    left = 0
    max_freq = 0
    best = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])
        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    print("All tests passed!")
