class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5
        }
        number = 0
        for char in s:
            number += translations[char]
        return number


def main():
    solution = Solution()
    s = input("algoritmo romano: ")
    result = solution.romanToInt(s)
    print(result)


if __name__ == "__main__":
    main()