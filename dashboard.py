import pandas as pd
import streamlit as st
import plotly.express as px

# ============== LOAD DATA =================
df = pd.read_csv("DataHabitAcadamicPerm .csv")

# ============== SETUP STREAMLIT APP =================
st.set_page_config(page_title="Student Habit Dashboard", layout="wide")
st.title("📊 Student Habit & Academic Dashboard")

# ============== TABS =====================
tab1, tab2, tab3 = st.tabs(["📚 Study vs Exam Score", "📱 Social Media vs Mental Health", "😴 Sleep vs Attendance"])

# ============== TAB 1 =====================
with tab1:
    st.subheader("Study Hours vs Exam Score")
    fig1 = px.scatter(df, x='study_hours_per_day', y='exam_score',
                      color='gender', trendline='ols',
                      color_discrete_sequence=['#FF6361', '#58508D'],
                      title='Study Hours vs Exam Score')
    st.plotly_chart(fig1, use_container_width=True)

# ============== TAB 2 =====================
with tab2:
    st.subheader("Social Media vs Mental Health")
    fig2 = px.scatter(df, x='social_media_hours', y='mental_health_rating',
                      color='part_time_job', trendline='ols',
                      color_discrete_sequence=['#2ca02c', '#d62728'],
                      title='Social Media vs Mental Health')
    st.plotly_chart(fig2, use_container_width=True)

# ============== TAB 3 =====================
with tab3:
    st.subheader("Sleep Hours vs Attendance")
    fig3 = px.scatter(df, x='sleep_hours', y='attendance_percentage',
                      color='diet_quality', trendline='ols',
                      color_discrete_sequence=['#17becf', '#bcbd22', '#ff7f0e'],
                      title='Sleep Hours vs Attendance')
    st.plotly_chart(fig3, use_container_width=True)