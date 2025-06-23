import streamlit as st
from database import Session as DBSession
from models import Task

def show_progress():
    st.header("Progress Tracking")
    session = DBSession()
    total = session.query(Task).count()
    completed = session.query(Task).filter(Task.is_completed == True).count()

    st.metric("Tasks Completed", f"{completed}/{total}")
    if total:
        st.progress(completed / total)