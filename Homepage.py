import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import streamlit_lottie as st_lottie
st.set_page_config(page_title="Web application", layout="wide", page_icon="📍")
st.balloons()

bgr_img ="""
<style>
[data-testid="stAppViewContainer"]
{
background-image: url("https://i.postimg.cc/4d4pXvdy/growth-economy-with-coins-concept.jpg");
background-size:cover;
}

[data-testid="stHeader"]
{
background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"]
{
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(bgr_img,unsafe_allow_html= True)
st.divider()

tab1, tab2 = st.tabs(["Introduction", "Gapminder dataset"])

with tab1:
    
    #col1, col2 = st.columns((2))
    #with col1:
    st.write("""Hi, my name is Huỳnh Trần Yến Nhi. I'm a freshman at :orange[**Vietnamese-German University**]. My major is Business Administration or Betriebswirtschaftslehre in German, intake 2023.
            \n As you can see, I'm the creator of this web application. This web application was made for my Python Project 2 in IT business math class.
            \n For more information, please keep discovering my web app.""")

    #with col2:
    #    st.lottie("https://lottie.host/2b00fde3-db2c-406c-a19f-a53c0a8eef95/X4M0fAvvb9.json")

    st.markdown("---")
    #st.header("What is :blue[**a web application**]❓")
    #st.write(":blue[**A web application**] is a software that runs in an Internet browser. Any website implying interactive elements can be called a web app. This means that the user can interact with the platform by pressing buttons, filling out forms, requesting a price or making purchases. Similar to desktop computer software or a mobile application, a web app provides a user interface, offers utility or entertainment, and the ability to access, create, store, or modify data.")
    
    #st.header("What is this web application used for❓")
    #st.write("This web app or web application is used for my second project in Python class. With this web application, users can analyze the 🔗[gapminder](https://plotly.github.io/datasets/) dataset available in the 🔗[plotly.express](https://plotly.com/python/plotly-express/) package.")
    st.subheader("General questions")
    expander1 = st.expander("❓What is :blue[**a web application**]?")
    expander1.write(":blue[**A web application**] is a software that runs in an Internet browser. Any website implying interactive elements can be called :blue[**a web app**]. This means that the user can interact with the platform by pressing buttons, filling out forms, requesting a price or making purchases. Similar to desktop computer software or a mobile application, a web app provides a user interface, offers utility or entertainment, and the ability to access, create, store, or modify data.")
    expander2 = st.expander("❓Why did I create this web app for my project?")
    expander2.write("""The main requirement for my project is to make a web application with interactive elements for visitors to interact with the graphs I draw with the raw from a dataset.
                    So I chose the :blue[**gapminder dataset**] and made this web app to complete my project.  """)
    expander3 = st.expander("❓What is a dataset?")
    expander3.write("A dataset is a collection of data with which developers can work to meet their goals. In a dataset, the rows represent the number of data points and the columns represent the features of the Dataset. They are mostly used in fields like machine learning, business, and government to gain insights, make informed decisions, or train algorithms. Datasets may vary in size and complexity and they mostly require cleaning and preprocessing to ensure data quality and suitability for analysis or modeling.")
    
    #st.markdown("---")

    #st.header("Who am I?")
    #st.write("My name is Huỳnh Trần Yến Nhi. I'm a freshman from :orange[**Vietnamese-German University**]. My major is Business Administration or Betriebswirtschaftslehre in German, intake 2023.")

with tab2: 
    df = px.data.gapminder()

    st.header("📌 Gapminder dataset")
    st.write("""This is a data frame with 1,704 observations on 8 variables. This dataset shows population, GDP per capita and life expectancy of 142 countries around the 🌍 from :blue[1952] to :blue[2007]. 
                \n If you want to know more about this 🔗[gapminder](https://plotly.github.io/datasets/) dataset or 🔗[plotly.express](https://plotly.com/python/plotly-express/) package, please click on it. """)
    st.markdown("---")
    st.dataframe(df, width = 1000)

    st.markdown(
    """
    - **Explanation for variables**:
    1. :blue[**country**]: a factor shows countries around the world
    2. :blue[**continent**]: a factor shows continent that include the country selected
    3. :blue[**year**]: a factor shows the year when live expectancy was recorded
    4. :blue[**lifexp**]: a numeric vector, showing life expectancy of each country
    5. :blue[**pop**]: a numeric vector, showing the population of each country
    6. :blue[**gdpPercap**]: a numeric vector, showing GDP per capital of each country
    7. :blue[**iso_alpha**]: a factor shows the ISO abbreviation of each country
    8. :blue[**iso_num**]: a factor shows the ISO number of each country
    """)


st.title("**Thanks for your visit! ❤️**")
#with col4:
#    st.lottie("https://lottie.host/ccd11e3f-5d5b-42fb-8565-cd429ccf1779/GEDXMKmSSc.json")

st.write("---")
st.write ("""Huỳnh Trần Yến Nhi 
          \n Freshman at Vietnamese-German University
          \n Location: 🏠 Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat City, Binh Duong Province
          \n My Uni website: https://vgu.edu.vn/
          \n My email: 10623034@student.vgu.edu.vn """)


