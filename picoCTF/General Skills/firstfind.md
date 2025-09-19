# First Find
> Easy, General Skills, picoGym Exclusive

## Description
Unzip this archive and find the file named 'uber-secret.txt'
[Download zip](https://artifacts.picoctf.net/c/500/files.zip)

## Solution
Unzip the zip file
```bash
unzip big-zip-files.zip
cd files.zip 
```
Searched for flag in text files using grep and used recursive flag for chekcing in subdirectories
```bash
grep -r "pico"
```
```bash
adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:
picoCTF{f1nd_15_f457_ab443fd1}
14789.txt.utf-8:brassa un picotin d'orge_. Comme depuis une demi-heure environ c'était
```

## Flag

picoCTF{f1nd_15_f457_ab443fd1}
