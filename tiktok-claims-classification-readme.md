# TikTok Claims Classification Project

## Project Overview
This project explores a TikTok dataset in a fictional scenario where the platform needs to classify videos as either claims or opinions. TikTok users can submit reports identifying videos that contain claims, which require review by moderators. Due to the high volume of user reports, TikTok is working on developing a predictive model to automatically determine whether a video contains a claim or offers an opinion.

The work documented here represents the initial data exploration phase, setting the foundation for future exploratory data analysis (EDA) and model development.

## Project Objectives
- Build and inspect a dataframe for the TikTok dataset
- Examine data types and structure
- Gather and analyze descriptive statistics
- Identify potential features for claims classification

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

### Distribution of Claims vs Opinions
The dataset shows a relatively balanced distribution between claims and opinions:
- Claims: 9,608 videos (49.6%)
- Opinions: 9,774 videos (50.4%)

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

### Key Correlations
1. Engagement level is strongly correlated with claim status
2. Author ban status correlates with higher raw engagement metrics
3. Videos with banned authors have significantly higher engagement than videos with active authors

## Next Steps
This initial exploration provides a foundation for further analysis. Future steps in this project will include:
1. Comprehensive exploratory data analysis (EDA)
2. Statistical testing of the observed correlations
3. Feature engineering for the classification model
4. Model selection, training, and evaluation
5. Model refinement and optimization

## Technologies Used
- Python
- Pandas for data manipulation
- NumPy for numerical operations

## Getting Started
```python
# Import required packages
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("tiktok_dataset.csv")

# View the first 10 rows
data.head(10)

# Get summary information
data.info()

# Get descriptive statistics
data.describe()
```

## Contact
[Your Name] - [Your Email/LinkedIn/GitHub]
