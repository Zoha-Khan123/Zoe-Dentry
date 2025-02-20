import streamlit as st
import pandas as pd


st.set_page_config(page_title="🦷 Zoe Dental", layout="wide")


st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-bottom: 40px;">
    <h1 style="color: #c1713b; font-size: 36px; margin-bottom: 10px;">Book an Appointment at Zoe Dental Clinic</h1>
    <h3 style="font-size: larger; color: #c1713b; font-weight: bold; margin-top: 0;">Let's begin adventure together</h3>
</div>
""", unsafe_allow_html=True)

#Form
with st.form("appointment_form"):
    st.markdown("### Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name*", placeholder="Enter your first name")
    with col2:
        last_name = st.text_input("Last Name*", placeholder="Enter your last name")

    email = st.text_input("Email Address*", placeholder="Enter your email address")
    phone = st.text_input("Phone Number*", placeholder="Enter your phone number")

    st.markdown("### Appointment Details")
    appointment_date = st.date_input("Appointment Date*")
    appointment_time = st.time_input("Appointment Time*")
    service_type = st.selectbox(
        "Select Service*",
        ["General Checkup", "Teeth Cleaning", "Cavity Filling", "Root Canal", "Braces Consultation", "Other"]
    )
    dentist = st.selectbox(
        "Preferred Dentist (Optional)",
        ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "No Preference"]
    )
    additional_notes = st.text_area("Additional Notes (Optional)", placeholder="Any special requests or notes")

    st.markdown("### Confirmation")
    agree = st.checkbox("I agree to the terms and conditions*")

 # Submit Button
    submitted = st.form_submit_button("Book Appointment")
    if submitted:
        if not first_name or not last_name or not email or not phone or not appointment_date or not appointment_time or not service_type or not agree:
            st.error("Please fill out all required fields marked with *")
        else:
            # Store the form data in session state
            st.session_state.first_name = first_name
            st.session_state.last_name = last_name
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.appointment_date = appointment_date
            st.session_state.appointment_time = appointment_time
            st.session_state.service_type = service_type
            st.session_state.dentist = dentist
            st.session_state.additional_notes = additional_notes
            st.session_state.agree = agree
            st.session_state.submitted = True
            st.success("Your appointment has been successfully booked!")
            st.balloons()

# Second page to display the details in a table
if 'submitted' in st.session_state and st.session_state.submitted:
    st.markdown("<h1 style='text-align: center;'>Appointment Details</h1>", unsafe_allow_html=True)

    # Create a DataFrame to display the appointment details in a table
    appointment_data = {
        "Field": [
            "First Name", "Last Name", "Email Address", "Phone Number", 
            "Appointment Date", "Appointment Time", "Service Type", 
            "Preferred Dentist", "Additional Notes", "Agreed to Terms"
        ],
        "Details": [
            st.session_state.first_name,
            st.session_state.last_name,
            st.session_state.email,
            st.session_state.phone,
            st.session_state.appointment_date,
            st.session_state.appointment_time,
            st.session_state.service_type,
            st.session_state.dentist,
            st.session_state.additional_notes,
            st.session_state.agree
        ]
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(appointment_data)

    # Display the data in a table
    st.table(df)
