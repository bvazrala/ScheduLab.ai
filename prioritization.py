import streamlit as st

def prioritize_view():
    st.header("Prioritization")
    use_ai = st.toggle("Use AI to help prioritize")

    if use_ai:
        st.info("AI support coming soon via VAPI integration.")
    else:
        priorities = st.text_area("List your priorities (one per line)")
        if priorities:
            priority_list = priorities.strip().split("\n")
            for i, p in enumerate(priority_list):
                st.write(f"{i+1}. {p}")