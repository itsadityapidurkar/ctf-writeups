# First Grep
> Easy, General Skills, picoCTF 2019
## Description
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

[file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)
## Solution

Download the file and use grep command to find the flag

```bash
grep -i "pico" file
```
## Flag
picoCTF{grep_is_good_to_find_things_f77e0797}
