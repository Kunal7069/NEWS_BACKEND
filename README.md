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

### 5️⃣ Scraping Comments
- Visits each **post URL** again one by one.
- Clicks the **"Load more comments"** button until all comments are visible.
- Extracts **comment text**, **commenter's name**, and **profile URL**.

---

## 🛠️ Technologies Used
- **Selenium** for browser automation
- **BeautifulSoup** for parsing HTML data
- **Python** for scripting automation logic
- **LinkedIn** web scraping

---

## ⚠️ Disclaimer
This project is for educational purposes only. Scraping LinkedIn violates its [Terms of Service](https://www.linkedin.com/legal/user-agreement), and excessive automated actions may result in account restrictions.

---

## 🔗 Contributing
Feel free to contribute by creating a pull request or reporting issues.

---

## 📧 Contact
For any queries, reach out via [your_email@example.com](mailto:your_email@example.com).
