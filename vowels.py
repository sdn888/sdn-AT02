def count_vowels(s: str) -> int:
    vowels = "aeiouаеёиоуыэюя"  # латиница + кириллица
    return sum(1 for char in s.lower() if char in vowels)
