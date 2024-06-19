import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

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

df = px.data.gapminder()

st.title(":blue[GDP]")
st.write("In this page, users can see changes of each country GDP during the period from 1952 to 2007 by adjusting the slider or clicking on the button ▶️.")

st.markdown("---")

custom_color_scale = px.colors.qualitative.Pastel[:len(df)] 
fig2 = px.choropleth(df, locations='iso_alpha', color='gdpPercap', hover_name='country',
                    projection='natural earth', animation_frame='year',width = 700, height = 800,
                    color_continuous_scale="Rainbow", color_discrete_sequence=custom_color_scale,
                    labels = {'gdpPercap':'GDP per capita'}                    )
fig2.update_traces(marker_line_width = 0.7, marker_line_color = 'white')
fig2.update_geos(resolution=50,
showcoastlines=True, coastlinecolor="Gray",
showland=True, landcolor="LightGrey",
showocean=True, oceancolor="LightBlue")

sliders = [dict(currentvalue={"prefix": "Year = "})]

fig2.update_layout(sliders=sliders)
fig2.update_layout(font_family="Courier New",font = dict (size = 20))
    
st.plotly_chart(fig2, theme = "streamlit", use_container_width=True)

st.header("***Are you curious about the code to draw this plot?***")
expander = st.expander("***Click this box***") 
expander.write ('''
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

df = px.data.gapminder()

st.title("GDP")
st.write("In this page, users can see changes of each country GDP during the period from 1952 to 2007 by adjusting the slider or clicking on the button ▶️.")

st.markdown("---")

custom_color_scale = px.colors.qualitative.Pastel[:len(df)] 
fig2 = px.choropleth(df, locations='iso_alpha', color='gdpPercap', hover_name='country',
                    projection='natural earth', animation_frame='year',width = 700, height = 800,
                    color_continuous_scale="Rainbow", color_discrete_sequence=custom_color_scale,
                    labels = {'gdpPercap':'GDP per capita'}                    )
fig2.update_traces(marker_line_width = 0.7, marker_line_color = 'white')
fig2.update_geos(resolution=50,
showcoastlines=True, coastlinecolor="Gray",
showland=True, landcolor="LightGrey",
showocean=True, oceancolor="LightBlue")

sliders = [dict(currentvalue={"prefix": "Year = "})]

fig2.update_layout(sliders=sliders)
fig2.update_layout(font_family="Courier New",font = dict (size = 20))
    
st.plotly_chart(fig2, theme = "streamlit", use_container_width=True)''')

