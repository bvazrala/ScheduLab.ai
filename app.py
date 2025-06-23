import streamlit as st
from task_calendar import calendar_view
from matrix import show_matrix
from prioritization import prioritize_view
from progress import show_progress
from database import init_db

st.set_page_config(page_title="ScheduLab", layout="wide")

init_db()

st.sidebar.title("ScheduLab")
page = st.sidebar.radio("Navigation", ["Calendar", "Matrix", "Prioritization", "Progress"])

if page == "Calendar":
    calendar_view()
elif page == "Matrix":
    show_matrix()
elif page == "Prioritization":
    prioritize_view()
elif page == "Progress":
    show_progress()