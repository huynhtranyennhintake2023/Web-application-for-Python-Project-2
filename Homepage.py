import streamlit as st

from streamlit_space import space
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import time

st.set_page_config(page_title="Web application", layout="wide", page_icon="📍")
st.balloons()
#expander = st.expander('What is this?')
#expander.write("""
#This web app (run by Python 🐍 + Streamlit 🎈) serves as an illustration for an Interactive Web Application for Python Project 2.

#It allows users to view population, GDP per capita and life expectancy of 1xx countries around the world 🌍 from :blue[1952] to :blue[2007] by interacting with the plots.

#Spend some time exploring this web application and have some fun.


#   Personal information:
    
#    \n :orange[Vietnamese-German University]
#    \n Author: Huỳnh Trần Yến Nhi
#    \n Major: Business Administration (Betriebswirtschaftslehre)
#    \n Intake: 2023""")
#st.write("🗓️: ", datetime.date(2024, 5, 16))
st.header("What is this❓")
st.write("This website is :blue[**a web application**].")
expander1 = st.expander("What is a web application?")
expander1.write("""A web application is a software that runs in an Internet browser. Any website implying interactive elements can be called a web app. This means that the user can interact with the platform by pressing buttons, filling out forms, requesting a price or making purchases. Similar to desktop computer software or a mobile application, a web app provides a user interface, offers utility or entertainment, and the ability to access, create, store, or modify data.""")

st.markdown("---")

st.header("What is this web application used for❓")
st.write("This web app or web application is used for my second project in Python class. With this web application, users can analyze the 🔗[gapminder](https://plotly.github.io/datasets/) dataset available in the 🔗[plotly.express](https://plotly.com/python/plotly-express/) package.")
expander2 = st.expander("What is a dataset?")
expander2.write("A dataset is a collection of data with which developers can work to meet their goals. In a dataset, the rows represent the number of data points and the columns represent the features of the Dataset. They are mostly used in fields like machine learning, business, and government to gain insights, make informed decisions, or train algorithms. Datasets may vary in size and complexity and they mostly require cleaning and preprocessing to ensure data quality and suitability for analysis or modeling.")
expander3 = st.expander("What is the 🔗[gapminder](https://plotly.github.io/datasets/) dataset available in the 🔗[plotly.express](https://plotly.com/python/plotly-express/) package?")
expander3.write("""This is a data frame with 1,704 observations on 8 variables. This dataset shows population, GDP per capita and life expectancy of 142 countries around the 🌍 from :blue[1952] to :blue[2007]. 
                \n For more information, please click on what you want to know which stand next to the symbol 🔗""")
expander4 = st.expander("Who am I?")
expander4.write("My name is Huỳnh Trần Yến Nhi. I'm a freshman from :orange[**Vietnamese-German University**]. My major is Business Administration or Betriebswirtschaftslehre in German, intake 2023.")

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

df = px.data.gapminder()

st.header("📌 Gapminder dataset")

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


