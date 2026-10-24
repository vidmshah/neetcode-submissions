class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        longest = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(max_freq, freq[ch])

            while(right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest
