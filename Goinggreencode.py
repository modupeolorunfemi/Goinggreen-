import streamlit as st
from PIL import Image
img = Image.open("customercare.png")
st.image(img, width=800)
st.title("Welcome to GoingGreen Consultancy....your satisfactioin in environmental consultancy")
st.header("Discover Friendliness to The Environment in Business")
st.subheader("Hello, Welcome to going green customer care,")
Name = st.text_input("Enter your name", "Type here...")
status = st.radio("select customer: ",('New Customer', 'Existing Customer'))
if (status=='New Customer'):
    st.success('New Customer')
else:
    st.success('Existing Customer')
st.write("kindly state your nearest location below")
Location = st.selectbox("Select Location: ",['Within Ibadan', 'outside Ibadan', 'outskirts of Ibadan','Inside Lagos', 'Far away from the North'])
st.write("You have selected: ", Location)
Nature_of_complaints = st.radio("select complaints: ",('unsatisfactory service delivery', 'unruly behaviour of personnel'))
if (Nature_of_complaints=='unsatisfactory service delivery'):
    st.success('We are trully sorry, kindly place another order which is free')
else:
    st.success("Our HR Manager will contact you for description of personnel unprofessionalism")
st.write("Thank you for choosing Goinggreen")
if (st.button("Submit")):
    result = Name
    st.success(result)
     