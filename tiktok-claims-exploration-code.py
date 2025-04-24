#!/usr/bin/env python
# coding: utf-8

# TikTok Claims Classification Project - Data Exploration
# This script contains all code used to explore the TikTok dataset for the claims classification project.
# The code demonstrates data loading, inspection, and preliminary analysis of engagement metrics.

# Import necessary packages
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("tiktok_dataset.csv")

# Display and examine the first 10 rows of the dataframe
print("First 10 rows of the dataframe:")
print(data.head(10))
print("\n")

# Get summary info about the dataframe
print("Dataset information:")
print(data.info())
print("\n")

# Get summary statistics for numeric columns
print("Descriptive statistics:")
print(data.describe())
print("\n")

# Examine claim status distribution
print("Distribution of claim status:")
print(data['claim_status'].value_counts())
print("\n")

# Filter data by claim status
claims = data[data['claim_status'] == 'claim']
opinions = data[data['claim_status'] == 'opinion']

# Calculate average view counts for claims
print('Mean view count for claims:', claims['video_view_count'].mean())
print('Median view count for claims:', claims['video_view_count'].median())
print("\n")

# Calculate average view counts for opinions
print('Mean view count for opinions:', opinions['video_view_count'].mean())
print('Median view count for opinions:', opinions['video_view_count'].median())
print("\n")

# Get counts for each combination of claim status and author ban status
print("Count of videos by claim status and author ban status:")
print(data.groupby(['claim_status', 'author_ban_status']).count()[['#']])
print("\n")

# Calculate engagement metrics by author ban status
print("Engagement metrics by author ban status (mean and median):")
ban_status_engagement = data.groupby(['author_ban_status']).agg(
    {'video_view_count': ['mean', 'median'],
     'video_like_count': ['mean', 'median'],
     'video_share_count': ['mean', 'median']})
print(ban_status_engagement)
print("\n")

# Calculate median video share count by author ban status
print("Median video share count by author ban status:")
print(data.groupby(['author_ban_status']).median(numeric_only=True)[['video_share_count']])
print("\n")

# Get detailed engagement metrics by author ban status
print("Detailed engagement metrics by author ban status:")
detailed_engagement = data.groupby(['author_ban_status']).agg(
    {'video_view_count': ['count', 'mean', 'median'],
     'video_like_count': ['count', 'mean', 'median'],
     'video_share_count': ['count', 'mean', 'median']})
print(detailed_engagement)
print("\n")

# Create engagement rate columns
print("Creating engagement rate columns...")
data['likes_per_view'] = data['video_like_count'] / data['video_view_count']
data['comments_per_view'] = data['video_comment_count'] / data['video_view_count']
data['shares_per_view'] = data['video_share_count'] / data['video_view_count']

# Calculate engagement rates by claim status and author ban status
print("Engagement rates by claim status and author ban status:")
engagement_rates = data.groupby(['claim_status', 'author_ban_status']).agg(
    {'likes_per_view': ['count', 'mean', 'median'],
     'comments_per_view': ['count', 'mean', 'median'],
     'shares_per_view': ['count', 'mean', 'median']})
print(engagement_rates)
print("\n")

# Summary statistics for key findings
print("SUMMARY FINDINGS:")
print(f"Total number of observations: {len(data)}")
print(f"Percentage of claims: {len(claims)/len(data)*100:.2f}%")
print(f"Percentage of opinions: {len(opinions)/len(data)*100:.2f}%")
print(f"Mean view ratio (claims/opinions): {claims['video_view_count'].mean()/opinions['video_view_count'].mean():.2f}")
print(f"Median view ratio (claims/opinions): {claims['video_view_count'].median()/opinions['video_view_count'].median():.2f}")

# Additional insights about banned authors
banned = data[data['author_ban_status'] == 'banned']
active = data[data['author_ban_status'] == 'active']
under_review = data[data['author_ban_status'] == 'under review']

print(f"\nPercentage of videos from banned authors: {len(banned)/len(data)*100:.2f}%")
print(f"Percentage of videos from active authors: {len(active)/len(data)*100:.2f}%")
print(f"Percentage of videos from authors under review: {len(under_review)/len(data)*100:.2f}%")

# Print out the correlation between claim_status and engagement metrics
# First, create a numeric version of claim_status (1 for claim, 0 for opinion)
data['claim_numeric'] = data['claim_status'].apply(lambda x: 1 if x == 'claim' else 0)

print("\nCorrelation between claim status and engagement metrics:")
correlation_data = data[['claim_numeric', 'video_view_count', 'video_like_count', 
                        'video_share_count', 'video_comment_count']].corr()
print(correlation_data['claim_numeric'])
