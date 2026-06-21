import streamlit as st
st.title("💊 MediTime AI")
name = st.text_input("Patient Name")
medicine = st.text_input("Medicine Name")
time = st.selectbox(
    "Medicine Time",
    ["Morning", "Afternoon", "Night"]
)
if st.button("Set Reminder"):
    st.success(f"Reminder set for {medicine} at {time}")
st.subheader("Medicine Status")
taken = st.radio(
    "Did you take your medicine?",
    ["Yes", "No"]
)
if taken == "Yes":
    st.success("Great! Keep following your schedule.")
else:
    st.warning("Please take your medicine on time.")
