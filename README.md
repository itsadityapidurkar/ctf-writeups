# CTF Writeups Archive

A premium, fast, and responsive Capture The Flag (CTF) writeups site built using the **Astro** Static Site Generator, styled with a high-contrast monospace cyber-green hacker theme, and integrated with **Decap CMS** for content management.

## 🚀 Key Features
* **Modern Developer Flow**: Write writeups in native Markdown (`.md`) inside the repository, and they are compiled directly into static HTML at build time.
* **No Iframes**: Writeups are rendered directly inside the website structure for optimal performance, mobile responsiveness, and SEO indexing.
* **Instant Client-Side Search**: Dynamic search built using Lunr.js with indexing generated automatically on build.
* **Built-in Admin Panel**: Access a visual editor at `/admin` powered by Decap CMS to manage writeups directly in the browser.
* **Vercel Serverless OAuth**: Secure, self-contained GitHub login handler running on Vercel Serverless Functions.

---

## 🛠️ Local Development & Running

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Start Development Server**:
   ```bash
   npm run dev
   ```
   * **Main Site**: [http://localhost:4321](http://localhost:4321)
   * **CMS Admin Dashboard**: [http://localhost:4321/admin](http://localhost:4321/admin)

3. **Verify Build**:
   ```bash
   npm run build
   ```

---

## ⚡ Deployment on Vercel (Step-by-Step)

Follow this guide to deploy your site live with active CMS support:

### Step 1: Create a GitHub OAuth App
To allow logging in securely on your live website's admin panel:
1. Go to your GitHub account settings.
2. Under the left sidebar, click **Developer settings** -> **OAuth Apps** -> **New OAuth App**.
3. Fill in the details:
   * **Application Name**: `CTF Writeups Admin`
   * **Homepage URL**: `https://<your-project-name>.vercel.app`
   * **Authorization callback URL**: `https://<your-project-name>.vercel.app/api/callback`
4. Click **Register application**.
5. Save the displayed **Client ID**.
6. Generate and save a **Client Secret**.

### Step 2: Configure Environment Variables in Vercel
1. Import your `ctf-writeups` repository into **Vercel**.
2. Under **Project Settings** -> **Environment Variables**, add the following keys:
   * `OAUTH_CLIENT_ID` = `(your GitHub Client ID)`
   * `OAUTH_CLIENT_SECRET` = `(your GitHub Client Secret)`
3. Save the variables.

### Step 3: Set Your Production URL in Config
1. Open [public/config.yml](public/config.yml) in your repository.
2. Edit the `base_url` key to point to your Vercel deployment domain:
   ```yaml
   backend:
     name: github
     repo: itsadityapidurkar/ctf-writeups
     branch: main
     base_url: https://<your-project-name>.vercel.app
     auth_endpoint: api/auth
   ```
3. Commit and push this change to GitHub. Vercel will rebuild and publish your changes!

---

## 📝 Content Management

### Adding a Writeup
You have two ways to add new writeups:

#### Option A: Via Admin Dashboard
1. Go to `https://your-domain.vercel.app/admin` and log in via GitHub.
2. Click **New CTF Writeup**.
3. Fill out the fields (title, category, flag, difficulty, banner name).
4. Write your solution in Markdown.
5. Click **Publish**. Decap CMS will automatically make a commit to your GitHub repository, triggering Vercel to rebuild.

#### Option B: Manually in Code
Create a Markdown file inside the collections folder following this structure:
`src/content/writeups/<ctf-id>/<category>/<challenge-name>.md`

Ensure it contains frontmatter metadata:
```yaml
---
title: "Challenge Name"
ctfId: "picoctf"
category: "General Skills"
difficulty: "Easy"
flag: "picoCTF{flag_goes_here}"
banner: "placeholder.png"
---
# Challenge Name
## Solution
... content ...
```

### Adding a New CTF Event
To add a new CTF event to the homepage list:
1. Open [src/data/ctfs.json](src/data/ctfs.json).
2. Append your event object to the array:
   ```json
   {
     "id": "hackthebox",
     "name": "HackTheBox",
     "status": "active",
     "banner": "placeholder.png"
   }
   ```
3. Place custom event banners directly in the `public/assets/` folder.