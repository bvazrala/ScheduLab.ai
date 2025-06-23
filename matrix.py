import streamlit as st
from database import Session as DBSession
from models import Task

def show_matrix():
    st.header("Eisenhower Matrix")
    session = DBSession()
    tasks = session.query(Task).all()

    cols = st.columns(2)
    quadrants = [[], [], [], []]

    for task in tasks:
        idx = 0
        if task.is_important:
            idx += 1
        if task.is_urgent:
            idx += 2
        quadrants[idx].append(task)

    quadrant_titles = ["Not Important, Not Urgent", "Important, Not Urgent",
                       "Not Important, Urgent", "Important, Urgent"]

    for i in range(2):
        with cols[i]:
            st.subheader(quadrant_titles[i * 2])
            for task in quadrants[i * 2]:
                st.write(task.title)

            st.subheader(quadrant_titles[i * 2 + 1])
            for task in quadrants[i * 2 + 1]:
                st.write(task.title)