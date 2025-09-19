# Bases
> Easy, General Skills, picoCTF 2019
## Description
What does this **bDNhcm5fdGgzX3IwcDM1** mean? I think it has something to do with bases.
## Solution
Whenever a challenge of bases first of all try for if it is base64 as mostly used

then use 
**Option 1:**

```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
```
**Option 2:**

Use [Cyberchef](https://gchq.github.io/CyberChef/)

Add from base64 and put the string the flag content will be in output, just wrap it in the flag format.
## Flag
picoCTF{l3arn_th3_r0p35}
