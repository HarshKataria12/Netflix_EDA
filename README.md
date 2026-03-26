# Netflix Dataset Analysis

![Netflix](https://img.shields.io/badge/Data_Analysis-Netflix-E50914?style=for-the-badge&logo=netflix)

This repository explores the **Netflix Titles Dataset**, analyzing the distribution of content across countries, genres, years, types, and ratings. The dataset has been cleaned, optimized, and visualized to answer key business questions.

## 📖 Table of Contents
1. [Data Cleaning and Preparation](#-data-cleaning-and-preparation)
2. [Analysis and Findings](#-analysis-and-findings)
    * [Top Countries](#1-top-countries-producing-netflix-content)
    * [Most Common Genres](#2-most-common-genres)
    * [Content Growth](#3-content-growth-by-year)
    * [Movies vs TV Shows](#4-split-between-movies-and-tv-shows)
    * [Rating Categories](#5-top-rating-categories)
3. [Conclusion](#-conclusion)
4. [How to Use](#-how-to-use)

---

## 🛠 Data Cleaning and Preparation
To ensure data integrity and performance, the following steps were performed:

* **Handling Missing Values:** Filled null entries in `director`, `cast`, `country`, `rating`, and `duration`.
* **Date Conversion:** Formatted `date_added` into a standardized `datetime` object.
* **Text Processing:** Cleaned string columns by stripping whitespace and standardizing capitalization.
* **Data Expansion:** "Exploded" multi-value columns (like `listed_in` for genres and `cast`) to allow for accurate counts per category.
* **Validation:** Removed duplicates and validated `release_year` (filtered for 1900–2026).
* **Optimization:** Converted `type` and `rating` to **Categorical** types to reduce memory footprint.

---

## 📊 Analysis and Findings

### 1. Top Countries Producing Netflix Content
* The **United States** leads content production, followed by **India** and the **United Kingdom**.
* "Unknown" entries were excluded to focus on actual content-producing regions.
  <img width="918" height="538" alt="Screenshot 2026-03-26 at 1 46 35 AM" src="https://github.com/user-attachments/assets/be8c9b53-c816-4453-8bd9-a760daeb4f80" />


### 2. Most Common Genres
* **Drama** and **Comedy** are the dominant genres on the platform.
* Other major categories include **Documentary**, **Action & Adventure**, and **Family-Kids**, showing Netflix's focus on high-engagement categories.
* <img width="919" height="429" alt="Screenshot 2026-03-26 at 1 46 42 AM" src="https://github.com/user-attachments/assets/5021906f-fbb1-4709-8825-ba3fa7cb2b51" />


### 3. Content Growth by Year
* Netflix content has shown steady growth, with a **major spike around 2015–2016**.
* This trend aligns with Netflix’s aggressive global expansion and pivot toward original content.
<img width="960" height="529" alt="Screenshot 2026-03-26 at 1 46 51 AM" src="https://github.com/user-attachments/assets/18233a55-ba61-41a4-91d1-e7a8c0641683" />

### 4. Split Between Movies and TV Shows
* There are slightly more **Movies** than **TV Shows** in the catalog, though both formats remain robustly represented.
<img width="605" height="619" alt="Screenshot 2026-03-26 at 1 47 00 AM" src="https://github.com/user-attachments/assets/79a4aece-f5ed-4a48-a972-d51766c1dba2" />

### 5. Top Rating Categories
* **TV-MA** is the most frequent rating, followed by **TV-14** and **PG-13**.
* A balanced presence of family-friendly content (TV-PG, G) indicates a strategy to capture a diverse age demographic.
<img width="952" height="577" alt="Screenshot 2026-03-26 at 1 47 07 AM" src="https://github.com/user-attachments/assets/dc34bb05-d615-4f38-9ba6-2f1b42bde5b6" />

---

## 🏁 Conclusion
* **Production Hubs:** The US and India remain the primary engines of content.
* **Genre Strategy:** Dramas and Comedies are the core pillars of the Netflix library.
* **Growth:** The platform has seen rapid, exponential growth over the last decade.
* **Library Balance:** Netflix maintains a diverse split between Movies and TV Shows while balancing adult-oriented and family-friendly ratings.

This analysis provides valuable insights into **Netflix’s content strategy**, serving as a guide for potential marketing, production, and recommendation engine improvements.

---
