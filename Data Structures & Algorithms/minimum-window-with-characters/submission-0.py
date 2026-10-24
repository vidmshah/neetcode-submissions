class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return "" 
        need =  Counter(t)
        window = {}
        have = 0
        required = len(need)
        left = 0
        best_len = float("inf")
        best_start = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start:best_start + best_len]