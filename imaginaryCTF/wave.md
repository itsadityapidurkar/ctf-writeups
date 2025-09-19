# Wave  
**Category:** Forensics  

---

## Challenge Description  
*“not a steg challenge i promise”*  
Attachment provided: **wave.wav**  

---

## Initial Thoughts  
- The description suggested it was *not* a steganography challenge.  
- Initially suspected it might be a trick hint and tested common steg tools anyway.  

---

## Steps Taken  

1. **Steg check**  
   ```bash
   zsteg wave.wav
   ```  
   - No useful results. Confirmed it wasn’t steganography-related.  

2. **Metadata inspection**  
   ```bash
   exiftool wave.wav
   ```  
   - Found the flag directly in the **Comment** section of the metadata.  

---

## Exploitation / Final Approach  
- The solution was straightforward: running `exiftool` revealed the flag without further processing.  

---

## Flag / Solution  
```
<flag found in Comment section>
```

---

## Key Takeaways  
- Always start with basic analysis tools (like `exiftool`) before jumping into heavier techniques.  
- Challenge hints can be misleading, but verifying the basics first often saves time.  
- Metadata can often hide critical information in forensic challenges.  
