# LinkedIn Browser Automation

This project automates the process of logging into LinkedIn, scraping post details, extracting reactions, and collecting comments from each post.

## 📌 Features
- **Automated LinkedIn Login**: Logs into LinkedIn with provided credentials.
- **Profile Scraping**: Extracts posts, including text, images, videos, likes, and URLs.
- **Reaction Scraping**: Clicks each reaction button to retrieve reactor names and profile URLs.
- **Comment Scraping**: Loads all comments and scrapes commenter details.

---

## 🚀 How It Works

### 1️⃣ Login to LinkedIn
- The automation script logs in using the provided credentials.
- It redirects to the profile that needs to be scraped.

### 2️⃣ Scraping Post Details
- Extracts **post content**, **images**, **videos**, **number of likes**, and **post URL** from each post.

### 3️⃣ Extracting Reactions
- Locates all reaction buttons (like, celebrate, support, etc.).
- Clicks each button to open the overlay with the list of people who reacted.
- Scrapes **names** and **profile URLs** of all reactors.

### 4️⃣ Handling Bot Detection
- To avoid bot detection, the script logs in again before proceeding further.
- After I get the post urls and I need to redirect to those post urls to scrap the comments so again and again redirect may caught it as a bot.
- So before redirecting I again login as to avoid bot detection.
- Similarly we can again and again login to avoid bot detection but we need to login from different ids.
- Bot detection activity is not able to detect bot if after login the whole scrapping is done on the single page.
- Then before redirecting to any other page, we should again login.
- I tried it and the attempts in which I was detected as bot increased.

### 5️⃣ Scraping Comments
- Visits each **post URL** again one by one.
- Clicks the **"Load more comments"** button until all comments are visible.
- Extracts **comment text**, **commenter's name**, and **profile URL**.

---


---

## 📌 Explanation of Components

### 📂 `browser_use/src/`
- **`config/`** → Placeholder for configuration settings.
- **`log/`**
  - **`logging.py`** → Handles logging and debugging information.
- **`scrapper/`**
  - **`posts_scrapper.py`** → Extracts LinkedIn post details.
  - **`reaction_scrapper.py`** → Extracts names & profile URLs of reactors.
  - **`comments_scrapper.py`** → Extracts comments and commenter details.

### 📄 `.env`
- Stores sensitive credentials such as LinkedIn login details.

### 🏗️ `main.py`
- The **entry point** of the project. Runs the automation in sequential order.

### 📜 `app.log`
- Contains execution logs for debugging purposes.

### 📂 `linkedin_posts_data_xxx.json`
- Stores extracted LinkedIn data in **JSON format** for further processing.

---

## 🚀 How to Run the Project
```sh
pip install requirements.txt
playwright install
cd browser_use
python -m src.main
