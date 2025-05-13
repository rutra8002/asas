# 10 -> 8
import math

def dec_to_other(n, other):
    result = ''
    while n > 0:
        result = str(n % other) + result
        n //= other
    return result

print(dec_to_other(120, 8))

def dec_to_hex(n):
    result = ''
    hex_chars = '0123456789ABCDEF'
    while n > 0:
        result = hex_chars[n % 16] + result
        n //= 16
    return result

print(dec_to_hex(368))

def other_to_dec(n, other):
    result = 0
    n = str(n)[::-1]
    for i in range(len(n)):
        result += int(n[i]) * (other ** i)
    return result

print(other_to_dec(170, 8))

def hex_to_dec(n):
    result = 0
    hex_chars = '0123456789ABCDEF'
    n = str(n)[::-1]
    n = n.upper()
    for i in range(len(n)):
        result += hex_chars.index(n[i]) * (16 ** i)
    return result


print(hex_to_dec("17d"))
