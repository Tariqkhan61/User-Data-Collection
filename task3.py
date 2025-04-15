import streamlit as st

# Set the title with green color
st.markdown("<h1 style='color:green;'>🚮 User Data Collection</h1>", unsafe_allow_html=True)

# Add instructions with large font size
st.markdown("<h3 style='color:red;'>Please enter your information below:</h3>", unsafe_allow_html=True)

# Collect data from the user using Streamlit widgets with emphasis on font size and colors
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
height = st.number_input("Enter your height in meters:", format="%.2f")
student = st.radio("Are you a student?", ("Yes", "No"))

# Display the collected data when the user inputs values
if st.button("Submit"):
    user_data = {
        "Name": name,
        "Age": age,
        "Height": height,
        "Student Status": student
    }
    st.success("Data collected successfully!")
    
    # Colorful display of the data
    st.markdown("<h3 style='color:green;'>Collected Data:</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;'>Name: <b style='color:purple;'>{name}</b></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;'>Age: <b style='color:orange;'>{age}</b></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;'>Height: <b style='color:teal;'>{height} meters</b></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;'>Student Status: <b style='color:crimson;'>{student}</b></p>", unsafe_allow_html=True)

# Add a footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: orange; font-size: 25px;">Created by™️: Muhammad Tariq Mahboob</p>',
    unsafe_allow_html=True
)