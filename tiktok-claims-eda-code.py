#!/usr/bin/env python
# coding: utf-8

# TikTok Claims Classification Project - Exploratory Data Analysis
# This script contains code for visualizing and analyzing the TikTok dataset further.

# Import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("tiktok_dataset.csv")

# Display basic information about the dataset
print("Dataset shape:", data.shape)
print("\nDataset info:")
data.info()
print("\nDescriptive statistics:")
print(data.describe())

# ----- VISUALIZING VIDEO DURATION -----
# Create a boxplot for video duration
plt.figure(figsize=(5,1))
plt.title('video_duration_sec')
sns.boxplot(x=data['video_duration_sec'])
plt.tight_layout()
plt.savefig("video_duration_boxplot.png")
plt.close()

# Create a histogram for video duration
plt.figure(figsize=(5,3))
sns.histplot(data['video_duration_sec'], bins=range(0,61,5))
plt.title('Video duration histogram')
plt.tight_layout()
plt.savefig("video_duration_histogram.png")
plt.close()

# ----- VISUALIZING VIEW COUNT -----
# Create a boxplot for video view count
plt.figure(figsize=(5, 1))
plt.title('video_view_count')
sns.boxplot(x=data['video_view_count'])
plt.tight_layout()
plt.savefig("video_view_count_boxplot.png")
plt.close()

# Create a histogram for video view count
plt.figure(figsize=(5,3))
sns.histplot(data['video_view_count'], bins=range(0,(10**6+1),10**5))
plt.title('Video view count histogram')
plt.tight_layout()
plt.savefig("video_view_count_histogram.png")
plt.close()

# ----- VISUALIZING LIKE COUNT -----
# Create a boxplot for video like count
plt.figure(figsize=(10,1))
plt.title('video_like_count')
sns.boxplot(x=data['video_like_count'])
plt.tight_layout()
plt.savefig("video_like_count_boxplot.png")
plt.close()

# Create a histogram for video like count
plt.figure(figsize=(5,3))
ax = sns.histplot(data['video_like_count'], bins=range(0,(7*10**5+1),10**5))
labels = [0] + [str(i) + 'k' for i in range(100, 701, 100)]
ax.set_xticks(range(0,7*10**5+1,10**5), labels=labels)
plt.title('Video like count histogram')
plt.tight_layout()
plt.savefig("video_like_count_histogram.png")
plt.close()

# ----- VISUALIZING COMMENT COUNT -----
# Create a boxplot for video comment count
plt.figure(figsize=(5,1))
plt.title('video_comment_count')
sns.boxplot(x=data['video_comment_count'])
plt.tight_layout()
plt.savefig("video_comment_count_boxplot.png")
plt.close()

# Create a histogram for video comment count
plt.figure(figsize=(5,3))
sns.histplot(data['video_comment_count'], bins=range(0,(3001),100))
plt.title('Video comment count histogram')
plt.tight_layout()
plt.savefig("video_comment_count_histogram.png")
plt.close()

# ----- VISUALIZING SHARE COUNT -----
# Create a boxplot for video share count
plt.figure(figsize=(5,1))
plt.title('video_share_count')
sns.boxplot(x=data['video_share_count'])
plt.tight_layout()
plt.savefig("video_share_count_boxplot.png")
plt.close()

# Create a histogram for video share count
plt.figure(figsize=(5,3))
sns.histplot(data['video_share_count'], bins=range(0,(270001),10000))
plt.title('Video share count histogram')
plt.tight_layout()
plt.savefig("video_share_count_histogram.png")
plt.close()

# ----- VISUALIZING DOWNLOAD COUNT -----
# Create a boxplot for video download count
plt.figure(figsize=(5,1))
plt.title('video_download_count')
sns.boxplot(x=data['video_download_count'])
plt.tight_layout()
plt.savefig("video_download_count_boxplot.png")
plt.close()

# Create a histogram for video download count
plt.figure(figsize=(5,3))
sns.histplot(data['video_download_count'], bins=range(0,(15001),500))
plt.title('Video download count histogram')
plt.tight_layout()
plt.savefig("video_download_count_histogram.png")
plt.close()

# ----- CLAIM STATUS ANALYSIS -----
# Create histogram of claims by verification status
plt.figure(figsize=(7,4))
sns.histplot(data=data,
             x='claim_status',
             hue='verified_status',
             multiple='dodge',
             shrink=0.9)
plt.title('Claims by verification status histogram')
plt.tight_layout()
plt.savefig("claims_by_verification_histogram.png")
plt.close()

# Create histogram of claim status by author ban status
plt.figure(figsize=(7,4))
sns.histplot(data, x='claim_status', hue='author_ban_status',
             multiple='dodge',
             hue_order=['active', 'under review', 'banned'],
             shrink=0.9,
             palette={'active':'green', 'under review':'orange', 'banned':'red'},
             alpha=0.5)
plt.title('Claim status by author ban status - counts')
plt.tight_layout()
plt.savefig("claim_status_by_ban_status_histogram.png")
plt.close()

# ----- VIEW COUNT ANALYSIS -----
# Create bar plot of median view counts by ban status
ban_status_counts = data.groupby(['author_ban_status']).median(
    numeric_only=True).reset_index()

plt.figure(figsize=(5,3))
sns.barplot(data=ban_status_counts,
            x='author_ban_status',
            y='video_view_count',
            order=['active', 'under review', 'banned'],
            palette={'active':'green', 'under review':'orange', 'banned':'red'},
            alpha=0.5)
plt.title('Median view count by ban status')
plt.tight_layout()
plt.savefig("median_view_count_by_ban_status.png")
plt.close()

# Calculate median view count by claim status
median_views_by_claim = data.groupby('claim_status')['video_view_count'].median()
print("\nMedian view count by claim status:")
print(median_views_by_claim)

# ----- TOTAL VIEWS ANALYSIS -----
# Create pie chart of total views by claim status
plt.figure(figsize=(3,3))
plt.pie(data.groupby('claim_status')['video_view_count'].sum(), 
        labels=['claim', 'opinion'],
        autopct='%1.1f%%')
plt.title('Total views by video claim status')
plt.tight_layout()
plt.savefig("total_views_by_claim_status_pie.png")
plt.close()

# ----- OUTLIER ANALYSIS -----
# Calculate outliers for count variables
count_cols = ['video_view_count',
              'video_like_count',
              'video_share_count',
              'video_download_count',
              'video_comment_count']

print("\nOutlier Analysis:")
for column in count_cols:
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    median = data[column].median()
    outlier_threshold = median + 1.5*iqr
    
    # Count the number of values that exceed the outlier threshold
    outlier_count = (data[column] > outlier_threshold).sum()
    outlier_percentage = (outlier_count / len(data)) * 100
    print(f'Number of outliers, {column}: {outlier_count} ({outlier_percentage:.2f}%)')

# ----- CORRELATION VISUALIZATION -----
# Create scatterplot of view count vs. like count by claim status
plt.figure(figsize=(8,5))
sns.scatterplot(x=data["video_view_count"], y=data["video_like_count"],
                hue=data["claim_status"], s=10, alpha=.3)
plt.title('Video Views vs. Likes by Claim Status')
plt.tight_layout()
plt.savefig("views_vs_likes_scatterplot.png")
plt.close()

# Create scatterplot for opinions only
opinion = data[data['claim_status']=='opinion']
plt.figure(figsize=(8,5))
sns.scatterplot(x=opinion["video_view_count"], y=opinion["video_like_count"],
                s=10, alpha=.3)
plt.title('Video Views vs. Likes (Opinions Only)')
plt.tight_layout()
plt.savefig("views_vs_likes_opinions_scatterplot.png")
plt.close()

# Print summary statistics for claims vs opinions
print("\nSummary statistics for claims:")
print(data[data['claim_status']=='claim'][count_cols].describe())
print("\nSummary statistics for opinions:")
print(data[data['claim_status']=='opinion'][count_cols].describe())
