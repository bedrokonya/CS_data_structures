import typing as tp


def polynomial_hash(s: str, x_powers: tp.List[int], p: int) -> int:
    hash_value: int = 0
    for i in range(len(s)):
        hash_value += x_powers[i] * ord(s[i]) % p
    return hash_value % p


def rabin_karp(pattern: str, text: str):
    x: int = 263
    p: int = 1000000007
    p_length: int = len(pattern)
    t_length: int = len(text)
    x_powers = [pow(x, i, p) for i in range(p_length)]
    p_hash = polynomial_hash(pattern, x_powers, p)

    last_window_num = t_length - p_length
    window_hashes: tp.List[int] = [None for _ in range(last_window_num + 1)]
    window_hashes[last_window_num] = polynomial_hash(text[last_window_num:], x_powers, p)

    result = []

    if window_hashes[last_window_num] == p_hash:
        if pattern == text[last_window_num:]:
            result.append(last_window_num)

    for i in range(last_window_num - 1, -1, -1):
        window_hashes[i] = ((window_hashes[i + 1] - (ord(text[i + p_length]) * x_powers[p_length - 1]) % p) * x % p + ord(text[i])) % p
        if window_hashes[i] == p_hash:
            result.append(i)
    result.sort()
    for i, value in enumerate(result):
        result[i] = str(value)

    print(" ".join(result))

def main():
    pattern: str = input().strip()
    text: str = input().strip()
    rabin_karp(pattern, text)

if __name__ == "__main__":
    main()