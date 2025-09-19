# Big Zip
> Easy, General Skills, picoGym Exclusive
## Description
Unzip this archive and find the flag.
[Download zip](https://artifacts.picoctf.net/c/503/big-zip-files.zip)
## Solution
Unzip the zip file
```bash
unzip big-zip-files.zip
cd big-zip-files.zip 
```
Searched for flag in text files using grep and used recursive flag for chekcing in subdirectories
```bash
grep -r "pico"
```
```bash
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:
information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

## Flag

picoCTF{gr3p_15_m4g1c_ef8790dc}
