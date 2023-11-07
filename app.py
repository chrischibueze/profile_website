import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon="bar_chart", layout="wide")
#-----Header section------
with st.container():
    st.subheader("Hi, I am Chy : winking_face_with_tongue")
    st.title("A Data Analyst from United Kingdom")
    st.write("an MSc placement student at Nottingham Trent University, specialises in Data Science. His professional background includes a stint as a Network Performance Analyst at Nokia, followed by a role as a Data Science Intern at Bugendaitech. I am currently doing a placement program with The Data City leeds, United kingdom ")
    url = "https://www.linkedin.com/in/chibueze-nwoke-486712183/"
    st.write("[Learn More >](%s)" % url)

#----WHAT I Do----
with st.container():
    st.header("What I do")
    st.write("##")
    st.write(
    """
                1. Working on and with the data, ensuring the quality whilst understanding customers needs to drive improvements in the product and ease of downloading information

                2. Mapping the emerging economy with experts and also collaborate on projects with public sector bodies/consultancy.
    """
    )
