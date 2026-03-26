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

### 2. Most Common Genres
* **Drama** and **Comedy** are the dominant genres on the platform.
* Other major categories include **Documentary**, **Action & Adventure**, and **Family-Kids**, showing Netflix's focus on high-engagement categories.

### 3. Content Growth by Year
* Netflix content has shown steady growth, with a **major spike around 2015–2016**.
* This trend aligns with Netflix’s aggressive global expansion and pivot toward original content.

### 4. Split Between Movies and TV Shows
* There are slightly more **Movies** than **TV Shows** in the catalog, though both formats remain robustly represented.

### 5. Top Rating Categories
