# TikTok Claims Classification Project

## Project Overview
This project explores a TikTok dataset in a fictional scenario where the platform needs to classify videos as either claims or opinions. TikTok users can submit reports identifying videos that contain claims, which require review by moderators. Due to the high volume of user reports, TikTok is working on developing a predictive model to automatically determine whether a video contains a claim or offers an opinion.

This repository contains both the initial data exploration and detailed exploratory data analysis (EDA) with visualizations, setting the foundation for future model development.

## Project Objectives
- Build and inspect a dataframe for the TikTok dataset
- Examine data types and structure
- Gather and analyze descriptive statistics
- Identify potential features for claims classification

## TikTok Claims Classification Project - Executive Summary

### Data Composition
- The dataset contains 19,382 videos with nearly equal distribution between claims (49.6%) and opinions (50.4%)
- Each video includes metadata like duration, author status, and various engagement metrics
- Some variables have missing values that required cleaning

### Claim vs. Opinion Characteristics

#### Engagement Differences
- **View Count**: Claims (median: 501,555) vs. Opinions (median: 4,953)
- Claims receive approximately 100x more views than opinions
- Claims dominate the total platform view count
- Similar patterns observed in likes, comments, shares, and downloads

#### User Behavior Patterns
- Verified users are significantly more likely to post opinions than claims
- Authors posting claims are more likely to be under review or banned
- Videos from banned authors receive substantially higher engagement across all metrics

### Distribution Analysis
- Video durations are uniformly distributed between 5-60 seconds
- All engagement metrics (views, likes, comments, shares, downloads) show extreme right-skewed distributions
- 12-19% of videos qualify as statistical outliers across different engagement metrics

## Business Implications

1. **Moderation Prioritization**
   - View count and other engagement metrics are strong predictors of claim status
   - High-engagement videos should be prioritized for review

2. **Risk Assessment**
   - Higher engagement correlates with higher likelihood of containing claims
   - Author ban status provides an additional signal for prioritization

3. **Model Development**
   - The clear separation in engagement metrics between claims and opinions suggests a classification model could achieve high accuracy
   - A combination of engagement metrics and author characteristics would likely yield the most effective predictive model


## Dataset
The dataset contains information about TikTok videos, including metadata and engagement metrics. Each row represents a distinct TikTok video that presents either a claim or an opinion.

### Data Dictionary

| Feature | Description | Data Type |
|---------|-------------|-----------|
| `#` | Row ID | int64 |
| `claim_status` | Whether the video contains a "claim" or an "opinion" | object |
| `video_transcription` | Text transcription of the video content | object |
| `video_view_count` | Number of views for the video | float64 |
| `video_like_count` | Number of likes for the video | float64 |
| `video_share_count` | Number of times the video was shared | float64 |
| `video_download_count` | Number of times the video was downloaded | float64 |
| `video_comment_count` | Number of comments on the video | float64 |
| `author_ban_status` | Whether the author is "active", "under review", or "banned" | object |

## Exploratory Analysis Findings

### Data Structure
- The dataset contains 19,382 observations
- Consists of 5 float64 columns, 3 int64 columns, and 4 object columns
- Some variables have missing values, including claim status, video transcription, and count variables

### Data Distribution
- **Video Duration**: Videos range from 5-60 seconds in length with a uniform distribution
- **View Count**: Highly right-skewed with more than half of videos receiving fewer than 100,000 views
- **Like Count**: Similar to view count, heavily right-skewed with most videos having fewer than 100,000 likes
- **Comment Count**: Extremely right-skewed with the majority of videos having fewer than 100 comments
- **Share Count**: Most videos have fewer than 10,000 shares with a right-skewed distribution
- **Download Count**: The majority of videos were downloaded fewer than 500 times

### Distribution of Claims vs Opinions
The dataset shows a relatively balanced distribution between claims and opinions:
- Claims: 9,608 videos (49.6%)
- Opinions: 9,774 videos (50.4%)


## Next Steps

1. **Model Development**
   - Create and evaluate machine learning models for claims classification
   - Develop a feature engineering strategy to handle the skewed distributions

2. **Implementation Strategy**
   - Design an automated scoring system for incoming videos
   - Integrate model predictions into the moderation workflow

3. **Ongoing Monitoring**
   - Establish performance metrics to evaluate classification accuracy
   - Implement feedback mechanisms to continuously improve the model

### Engagement Analysis
1. **Claim Status and Engagement:**
   - Videos labeled as claims have significantly higher view counts than opinion videos
   - Mean view count for claims: Approximately 4.5 times higher than opinions
   - Median view count for claims: Approximately 4.5 times higher than opinions

2. **Author Ban Status and Engagement:**
   - Videos from banned authors have substantially higher engagement metrics:
     - Median video share count for banned authors is 33 times higher than active authors
     - Banned authors and those under review get far more views, likes, and shares than active authors
     - In most groups, the mean is much greater than the median, indicating videos with very high engagement outliers

3. **Engagement Rate Analysis:**
   - Created derived metrics:
     - `likes_per_view`: likes divided by views
     - `comments_per_view`: comments divided by views
     - `shares_per_view`: shares divided by views
   - When analyzing by engagement rate (versus raw counts), claim videos have higher engagement rates than opinion videos
   - For claim videos, banned authors have slightly higher likes/view and shares/view rates than active authors

### Key Correlations and Insights
1. Engagement level is strongly correlated with claim status
2. Author ban status correlates with higher raw engagement metrics
3. Videos with banned authors have significantly higher engagement than videos with active authors
4. Verified users are much more likely to post opinions than claims
5. Authors who post claim videos are more likely to come under review or get banned
6. Median view count for claims (501,555) is dramatically higher than for opinions (4,953)
7. Claim videos dominate the total view count despite having roughly the same number of videos in the dataset
8. Significant outliers exist across all engagement metrics (12-19% of data points qualify as outliers)

## Visualizations
The exploratory data analysis includes various visualizations:

1. **Distribution Analysis**
   - Box plots and histograms for video duration and all engagement metrics
   - Pie chart showing total views by claim status

2. **Relationship Analysis**
   - Histograms showing claim status by verification status
   - Histograms showing claim status by author ban status
   - Bar plot of median view count by ban status
   - Scatter plots of view count vs. like count by claim status

3. **Outlier Analysis**
   - Identified outliers in all engagement metrics using IQR method
   - Found that 12-19% of data points qualify as outliers depending on the metric

## Next Steps
The exploratory data analysis has provided valuable insights. Future steps in this project will include:
1. Handling of outliers based on project requirements (keep, delete, or reassign)
2. Statistical testing of the observed correlations
3. Feature engineering for the classification model
4. Model selection, training, and evaluation
5. Model refinement and optimization

## Technologies Used
- Python
- Pandas for data manipulation
- NumPy for numerical operations
- Matplotlib and Seaborn for data visualization
- Tableau for creating interactive dashboards

## Conclusion
The exploratory data analysis reveals distinct patterns that differentiate claims from opinions, primarily through engagement metrics and author characteristics. These findings provide a strong foundation for developing an effective classification model that can automate and prioritize the moderation workflow.
