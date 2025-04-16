from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefixo = strs[0]

    for palavra in strs[1:]:
        # Enquanto o prefixo não for o começo da palavra
        while not palavra.startswith(prefixo):
            # Vai cortando o prefixo
            prefixo = prefixo[:-1]
            if not prefixo:
                return ""
    
    return prefixo

# Teste
def main():
    print(longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(longestCommonPrefix(["dog", "racecar", "car"]))     # ""

if __name__ == "__main__":
    main()
