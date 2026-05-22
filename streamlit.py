import streamlit as st

st.title("Hello World")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("This is a text")
st.markdown("This is a markdown")
st.write("This is a write")
st.divider()

st.subheader("Input Widgets")
st.text("Text Input")


#form

st.text_input("Name", placeholder="Enter your name")
st.text_input("Email", placeholder="Enter your email")
st.text_area("Message", placeholder="Enter your message")
st.number_input("Age", min_value=0, max_value=100, value=25)
st.date_input("Date of Birth")
st.selectbox("Country", ["Pakistan","USA", "Canada", "UK", "Australia", "others"])
st.multiselect("Hobbies", ["Reading", "Traveling", "Cooking", "Sports"])
st.checkbox("I agree to the terms and conditions")

st.spinner("Loading...")
st.success("Data loaded successfully!")

#percentage calculator
obtained_marks = st.number_input("Obtained Marks", min_value=0, max_value=1100, value=0)
total_marks = st.number_input("Total Marks", min_value=1, max_value=1100, value=100)

if st.button("Calculate Percentage"):
    percentage = (obtained_marks / total_marks) * 100
    st.write(f"Your percentage is: {percentage:.2f}%")