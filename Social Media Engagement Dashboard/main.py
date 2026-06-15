import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("SOCIAL MEDIA ENGAGEMENT ANALYSIS SYSTEM")
print("=" * 60)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("social_media_data_1000.csv")

print("\nDataset Loaded Successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

# ==========================================
# BASIC STATISTICS
# ==========================================

print("\nDataset Statistics:")
print(df.describe())

# ==========================================
# TOTAL METRICS
# ==========================================

total_posts = len(df)

total_likes = df["Likes"].sum()

total_comments = df["Comments"].sum()

total_shares = df["Shares"].sum()

avg_engagement = round(
    df["EngagementRate"].mean(),
    2
)

print("\n")
print("=" * 60)
print("SOCIAL MEDIA INSIGHTS")
print("=" * 60)

print(f"Total Posts : {total_posts}")
print(f"Total Likes : {total_likes}")
print(f"Total Comments : {total_comments}")
print(f"Total Shares : {total_shares}")
print(f"Average Engagement Rate : {avg_engagement}%")

# ==========================================
# PLATFORM DISTRIBUTION
# ==========================================

plt.figure(figsize=(10,5))

sns.countplot(
    x="Platform",
    data=df
)

plt.title("Platform Distribution")

plt.savefig("platform_distribution.png")

plt.show()

# ==========================================
# CONTENT TYPE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10,5))

sns.countplot(
    x="ContentType",
    data=df
)

plt.title("Content Type Distribution")

plt.savefig("content_type_distribution.png")

plt.show()

# ==========================================
# LIKES BY PLATFORM
# ==========================================

plt.figure(figsize=(10,5))

sns.barplot(
    x="Platform",
    y="Likes",
    data=df
)

plt.title("Likes By Platform")

plt.savefig("likes_by_platform.png")

plt.show()

# ==========================================
# COMMENTS BY PLATFORM
# ==========================================

plt.figure(figsize=(10,5))

sns.barplot(
    x="Platform",
    y="Comments",
    data=df
)

plt.title("Comments By Platform")

plt.savefig("comments_by_platform.png")

plt.show()

# ==========================================
# SHARES BY PLATFORM
# ==========================================

plt.figure(figsize=(10,5))

sns.barplot(
    x="Platform",
    y="Shares",
    data=df
)

plt.title("Shares By Platform")

plt.savefig("shares_by_platform.png")

plt.show()

# ==========================================
# MONTHLY ENGAGEMENT
# ==========================================

monthly = df.groupby(
    "Month"
)["EngagementRate"].mean()

plt.figure(figsize=(12,5))

monthly.plot(
    marker="o"
)

plt.title("Monthly Engagement Trend")

plt.savefig("monthly_engagement.png")

plt.show()

# ==========================================
# BEST POSTING TIME
# ==========================================

best_time = df.groupby(
    "PostingTime"
)["EngagementRate"].mean()

plt.figure(figsize=(12,5))

best_time.plot(
    marker="o"
)

plt.title("Best Posting Time")

plt.savefig("best_posting_time.png")

plt.show()

# ==========================================
# TOP POSTS
# ==========================================

top_posts = df.sort_values(
    by="Likes",
    ascending=False
)

print("\nTop 10 Posts")

print(
    top_posts.head(10)
)

# ==========================================
# CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Social Media Correlation Heatmap"
)

plt.savefig("correlation_heatmap.png")

plt.show()

# ==========================================
# COMPLETE
# ==========================================

print("\n")
print("=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)