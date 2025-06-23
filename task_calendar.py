import streamlit as st
import datetime
from sqlalchemy.orm import Session
from database import Session as DBSession
from models import Task

def calendar_view():
    st.header("Calendar")
    session = DBSession()

    with st.form("Add Task"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")
        is_important = st.checkbox("Important")
        is_urgent = st.checkbox("Urgent")
        submitted = st.form_submit_button("Add Task")

        if submitted:
            task = Task(title=title, description=description, due_date=due_date,
                        is_important=is_important, is_urgent=is_urgent)
            session.add(task)
            session.commit()
            st.success("Task added")

    st.subheader("Upcoming Tasks")
    today = datetime.date.today()
    tasks = session.query(Task).filter(Task.due_date >= today).all()
    for task in tasks:
        st.write(f"{task.due_date}: {task.title}")