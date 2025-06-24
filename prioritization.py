# prioritization.py
import streamlit as st
from vapi_client import create_call
import asyncio

def prioritize_view():
    st.header("Prioritization")

    use_ai = st.toggle("Use AI to help prioritize")

    if use_ai:
        st.info("AI support coming soon via VAPI integration.")

        customer_number = st.text_input("Enter your phone number (e.g., +1234567890)")

        if st.button("Call Me"):
            if customer_number.startswith("+") and len(customer_number) > 4:
                try:
                    asyncio.run(create_call(customer_number))
                    st.success("Call initiated. Please wait for your phone to ring.")
                except Exception as e:
                    st.error(f"Failed to initiate call: {e}")
            else:
                st.warning("Please enter a valid phone number including country code.")
    else:
        priorities = st.text_area("List your priorities (one per line)")
        if priorities:
            priority_list = priorities.strip().split("\n")
            for i, p in enumerate(priority_list):
                st.write(f"{i+1}. {p}")
