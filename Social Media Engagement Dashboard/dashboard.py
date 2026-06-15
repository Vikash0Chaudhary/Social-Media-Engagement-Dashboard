import streamlit as st
import pandas as pd
import plotly.express as px
import os
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Social Media Dashboard",
    page_icon="📱",
    layout="wide"
)

def load_css():

    css_path = os.path.join(
        os.path.dirname(__file__),
        "styles",
        "style.css"
    )

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()



# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("social_media_data_1000.csv")

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style='
background: linear-gradient(135deg,#ffb3c6,#ffc8dd,#ffd6e7);
padding:35px;
border-radius:25px;
text-align:center;
box-shadow:0px 8px 25px rgba(0,0,0,0.15);
'>

<h1 style='color:#444;'>
📱 Social Media Engagement Dashboard
</h1>

<h3 style='color:#555;'>
Analytics • Engagement • Growth Insights
</h3>

</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 Filters")

platform = st.sidebar.multiselect(
    "Platform",
    df["Platform"].unique(),
    default=df["Platform"].unique()
)

content = st.sidebar.multiselect(
    "Content Type",
    df["ContentType"].unique(),
    default=df["ContentType"].unique()
)

month = st.sidebar.multiselect(
    "Month",
    df["Month"].unique(),
    default=df["Month"].unique()
)

filtered_df = df[
    (df["Platform"].isin(platform))
    &
    (df["ContentType"].isin(content))
    &
    (df["Month"].isin(month))
]

# =====================================
# KPI CARDS
# =====================================

total_posts = len(filtered_df)

total_likes = filtered_df["Likes"].sum()

total_comments = filtered_df["Comments"].sum()

total_shares = filtered_df["Shares"].sum()

engagement = round(
    filtered_df["EngagementRate"].mean(),
    2
)
col1,col2,col3,col4,col5 = st.columns(5)

cards = [
    ("📱 Posts", total_posts, "#ff8fab"),
    ("❤️ Likes", f"{total_likes:,}", "#ff758f"),
    ("💬 Comments", f"{total_comments:,}", "#52b788"),
    ("🔄 Shares", f"{total_shares:,}", "#4cc9f0"),
    ("📈 Engagement", f"{engagement}%", "#c77dff")
]

for col, (title, value, color) in zip(
    [col1,col2,col3,col4,col5],
    cards
):
    with col:
        st.markdown(f"""
        <div style="
        background:{color};
        padding:25px;
        border-radius:25px;
        text-align:center;
        color:white;
        box-shadow:0px 8px 25px rgba(0,0,0,0.15);
        ">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# CHARTS
# =====================================

col1,col2 = st.columns(2)

with col1:

    platform_likes = (
        filtered_df
        .groupby("Platform")["Likes"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        platform_likes,
        names="Platform",
        values="Likes",
        title="Likes Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(
        filtered_df,
        x="ContentType",
        title="Content Type Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================

col3,col4 = st.columns(2)

with col3:

    monthly = (
        filtered_df
        .groupby("Month")["EngagementRate"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Month",
        y="EngagementRate",
        markers=True,
        title="Monthly Engagement Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col4:

    best_time = (
        filtered_df
        .groupby("PostingTime")["EngagementRate"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        best_time,
        x="PostingTime",
        y="EngagementRate",
        title="Best Posting Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# TOP POSTS
# =====================================

st.subheader("🔥 Top 20 Posts")

top_posts = filtered_df.sort_values(
    by="Likes",
    ascending=False
)

st.dataframe(
    top_posts.head(20),
    use_container_width=True
)

# =====================================
# INSIGHTS
# =====================================

st.subheader("📈 Recommendations")

st.success("""
✅ Focus on high-engagement content types.

✅ Post during the highest engagement hours.

✅ Increase posting frequency on top-performing platforms.

✅ Prioritize content with higher share rates.
""")

st.markdown("""
<hr>

<div style="
text-align:center;
color:#666;
">

🚀 Social Media Engagement Dashboard

</div>
""",
unsafe_allow_html=True)