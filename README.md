# Netflix_EDA
Netflix Dataset Analysis
This project explores the Netflix titles dataset, analyzing the distribution of content across countries, genres, years, types, and ratings. The dataset has been cleaned, optimized, and visualized to answer key business questions.
Data Cleaning and Preparation
Filled missing values in director, cast, country, rating, and duration.
Converted date_added to datetime.
Cleaned text columns (stripped whitespace, standardized capitalization).
Exploded multi-value columns (listed_in for genres, cast) for detailed analysis.
Removed duplicates and validated numeric ranges (release_year between 1900–2026).
Converted categorical columns (type, rating) to category type for memory efficiency.
Analysis and Findings
1. Top Countries Producing Netflix Content
United States produces the most content, followed by India and the United Kingdom.
"Unknown" entries were excluded to reflect actual content-producing countries.
2. Most Common Genres
Most common genres: Drama and Comedy, followed by Documentary, Action & Adventure, and Family-Kids.
Netflix focuses heavily on these popular categories.
3. Content Growth by Year
Netflix content has grown steadily, with a major spike around 2015–2016.
This aligns with global expansion of Netflix’s streaming service.
4. Split Between Movies and TV Shows
Slightly more Movies than TV Shows, but both types are well-represented.
5. Top Rating Categories
Most content is rated TV-MA, followed by TV-14 and PG-13.
Family-friendly content (TV-PG, G) is also represented, showing a balance.
Conclusion
United States and India dominate content production.
Dramas and Comedies are the most common genres.
Netflix has experienced rapid content growth over the past decade.
Both Movies and TV Shows are heavily represented, with adult and family ratings balanced.
This analysis provides insights into Netflix’s content strategy, guiding marketing, production, and recommendation decisions.
