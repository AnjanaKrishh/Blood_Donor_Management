import streamlit as st
from blood_donor import BloodDonorManager
donor_instance = BloodDonorManager()
tab1, tab2 = st.tabs(["ADD", "VIEWS"])
with tab1:
    st.title("Add New Blood Donor")
    name=st.text_input("Enter Donor Name")
    blood_group =st.text_input("Enter Blood Group")
    phone = st.text_input("Enter Phone Number")
    city = st.text_input("Enter City")
    last_donation=st.text_input("Enter last Donation Date")
    if st.button("Add New Blood Donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Blood Donor Added Successfully...!")
with tab2:
    st.title("View Donor Details")
