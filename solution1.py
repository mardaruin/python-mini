
def number_of_bits(number):
    bit_length = 0
    temp_number = abs(number)
    while temp_number != 0:
        bit_length += 1
        temp_number >>= 1

    ones_count = 0
    if number < 0:
        number = ~abs(number) + 1
        ones_count += 1

    for _ in range(bit_length):
        ones_count += number & 1
        number >>= 1

    return ones_count

assert(number_of_bits(-1)) == 2
assert(number_of_bits(-12345678)) == 13
assert(number_of_bits(12345678)) == 12
assert(number_of_bits(-123)) == 3
assert(number_of_bits(1)) == 1

print(number_of_bits(-556))