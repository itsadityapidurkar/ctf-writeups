# 2Warm
> Easy, General Skills, picoCTF 2019
## Description
Can you convert the number 42 (base 10) to binary (base 2)?

# Solution
**Option 1**:

Solve by basic math by power of 2
Just remember this for decimal to binary conversion

| Bit Position | Power of 2 | Value   | Binary Digit Weight |
|--------------|------------|---------|----------------------|
| 0            | 2^0        | 1       | 0000 0001            |
| 1            | 2^1        | 2       | 0000 0010            |
| 2            | 2^2        | 4       | 0000 0100            |
| 3            | 2^3        | 8       | 0000 1000            |
| 4            | 2^4        | 16      | 0001 0000            |
| 5            | 2^5        | 32      | 0010 0000            |
| 6            | 2^6        | 64      | 0100 0000            |
| 7            | 2^7        | 128     | 1000 0000            |

Now as we want 42, 

42=32+8+2

101010

**Option 2:**

Use [Cyberchef](https://cyberchef.io/)

and then use from base and to base option set radix for from base to **42** and to base to **2**

## Flag

picoCTF{101010}
