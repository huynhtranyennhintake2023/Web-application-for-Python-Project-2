import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
#import streamlit_lottie as st_lottie
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

ngr_img ="""
<style>
[data-testid="stSidebar"]
{
background-image: url("https://cdn.wallpapersafari.com/10/98/LNMmTg.jpeg");
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
gif = """
<iframe src="https://giphy.com/embed/AduQoFjjHQPb8dW2MG" width="280" height="280" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/stickers/mintostudio-rabbit-character-usagyuuun-AduQoFjjHQPb8dW2MG"></p>
"""
st.markdown(ngr_img,unsafe_allow_html= True)

#st.divider()

tab1, tab2 = st.tabs(["Introduction", "Gapminder dataset"])

with tab1:
    
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Self-introduction")
        st.write("""Hi, my name is :purple[**Huỳnh Trần Yến Nhi**]. I'm a freshman at :orange[**Vietnamese-German University**]. My major is Business Administration or Betriebswirtschaftslehre in German, intake 2023.
            \n As you can see, I'm the creator of this web application. This web application was made for my Python Project 2 in IT business math class.
            \n For more information, please keep discovering my web app.""")

    with col2:
        st.markdown(gif,unsafe_allow_html= True)
        
        

    st.markdown("---")
    #st.header("What is :blue[**a web application**]❓")
    #st.write(":blue[**A web application**] is a software that runs in an Internet browser. Any website implying interactive elements can be called a web app. This means that the user can interact with the platform by pressing buttons, filling out forms, requesting a price or making purchases. Similar to desktop computer software or a mobile application, a web app provides a user interface, offers utility or entertainment, and the ability to access, create, store, or modify data.")
    
    #st.header("What is this web application used for❓")
    #st.write("This web app or web application is used for my second project in Python class. With this web application, users can analyze the 🔗[gapminder](https://plotly.github.io/datasets/) dataset available in the 🔗[plotly.express](https://plotly.com/python/plotly-express/) package.")
    st.subheader("General questions")
    expander1 = st.expander("❓What is :blue[**a web application**]?")
    expander1.write(":blue[**A web application**] is a software that runs in an Internet browser. Any website implying interactive elements can be called :blue[**a web app**]. This means that the user can interact with the platform by pressing buttons, filling out forms, requesting a price or making purchases. Similar to desktop computer software or a mobile application, a web app provides a user interface, offers utility or entertainment, and the ability to access, create, store, or modify data.")
    expander2 = st.expander("❓Why did I create this web app?")
    expander2.write("""The main requirement for my Python Project 2 in IT business math class is to make a web application with interactive elements for visitors to interact with the graphs I draw with the raw from a dataset.
                    So I chose the :blue[**gapminder dataset**] and made this web app to complete my project.  """)
    expander3 = st.expander("❓How could I create this web app?")
    expander3.write("""There are several steps for creating this web app:
                    \n :blue[**Step 1**]: Download Python language and the application for providing coding environment. Here I use [Visual Studio Code](https://code.visualstudio.com/) 
                    \n :blue[**Step 2**]: Download needed packages. Here I mainly use [streamlit](https://streamlit.io/), [plotly.express](https://plotly.com/python/plotly-express/)
                    \n :blue[**Step 3**]: Create a basic Streamlit app to be familiar with Python and Streamlit
                    \n :blue[**Step 4**]: Choose a dataset you want and analyze the dataset to decide what to draw 
                    \n :blue[**Step 5**]: Use Streamlit and plotly.express to draw
                    \n :blue[**Step 6**]: Run the web app on your laptop (locally) to see if it works 
                    \n :blue[**Step 7**]: If all things go well, create a [GitHub](https://github.com/) account and then a [Streamlit](https://streamlit.io/) account. It is important that you connect your Streamlit account to the Github account.  
                    \n :blue[**Step 8**]: If your app runs smoothly, upload it to Github.
                    \n :blue[**Step 9**]: Once you are done with Step 8, go to your Streamlit account and click on New app
                    """)
    expander4 = st.expander("❓What is :blue[**a dataset**]?")
    expander4.write("A dataset is a collection of data with which developers can work to meet their goals. In a dataset, the rows represent the number of data points and the columns represent the features of the Dataset. They are mostly used in fields like machine learning, business, and government to gain insights, make informed decisions, or train algorithms. Datasets may vary in size and complexity and they mostly require cleaning and preprocessing to ensure data quality and suitability for analysis or modeling.")
    expander5 = st.expander("❓What is the :blue[**gapminder dataset**]?")
    expander5.write("If you want to know more about this dataset, please visit the tab named :blue[Gapminder dataset].")
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


