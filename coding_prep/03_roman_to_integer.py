"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
"""

roman_to_int_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_num(roman_numerals: str) -> int:
    total_num = 0
    prev_num = "M"
    for r in roman_numerals:
        total_num += roman_to_int_dict[r]
        if roman_to_int_dict[prev_num] < roman_to_int_dict[r]:
            total_num -= 2 * roman_to_int_dict[prev_num]
        prev_num = r
    return total_num

def main():

    # Test 1
    t1 = roman_to_num("III")
    assert t1 == 3, "Wrong value."
    # Test 2
    t2 = roman_to_num("LVIII")
    assert t2 == 58, "Wrong value."
    # Test 3
    t3 = roman_to_num("MCMXCIV")
    assert t3 == 1994, "Wrong value."
    
if __name__ == "__main__":
    main()