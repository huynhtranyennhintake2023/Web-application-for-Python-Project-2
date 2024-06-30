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
st.write("""The global economy has experienced significant growth over the past several decades, as evidenced by the steady rise in world GDP from 1952 to 2007. This remarkable trend can be attributed to a number of factors, including population growth, technological advancements, and the expansion of international trade. 
         \n The graph depicting world GDP during this period paints a clear picture of the world's economic progress. It shows a consistent upward trajectory, with GDP increasing from a relatively modest level in the early 1950s to a much more substantial figure by the mid-2000s. This growth reflects the increasing productivity and prosperity of nations around the globe, as they have harnessed their resources and human capital to drive economic development. While there have been some fluctuations and periods of slower growth along the way, the overall trend is undeniable. The world's population has also expanded significantly during this time, further contributing to the expansion of economic activity and the demand for goods and services. As more people have entered the global workforce and consumer markets, the opportunities for economic growth have multiplied. Ultimately, the data on world GDP from 1952 to 2007 serves as a powerful testament to the resilience and adaptability of the global economy. It demonstrates the remarkable progress that can be achieved through the collective efforts of nations, businesses, and individuals working towards a more prosperous future.
         """)

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

st.header(":blue[Are you curious about the code to draw this plot?]")
expander = st.expander("**Click this box**") 
expander.write ('''
import streamlit as st
\nimport plotly.express as px
\nimport pandas as pd
\nimport numpy as np
\nimport datetime

\ndf = px.data.gapminder()

\ncustom_color_scale = px.colors.qualitative.Pastel[:len(df)] 
\nfig2 = px.choropleth(df, locations='iso_alpha', color='gdpPercap', hover_name='country',
                    projection='natural earth', animation_frame='year',width = 700, height = 800,
                    color_continuous_scale="Rainbow", color_discrete_sequence=custom_color_scale,
                    labels = {'gdpPercap':'GDP per capita'}                    )
\nfig2.update_traces(marker_line_width = 0.7, marker_line_color = 'white')
\nfig2.update_geos(resolution=50, showcoastlines=True, coastlinecolor="Gray",
showland=True, landcolor="LightGrey",
showocean=True, oceancolor="LightBlue")

\nsliders = [dict(currentvalue={"prefix": "Year = "})]

\nfig2.update_layout(sliders=sliders)
\nfig2.update_layout(font_family="Courier New",font = dict (size = 20))
    
\nst.plotly_chart(fig2, theme = "streamlit", use_container_width=True)''')
st.write("---")
st.write ("""Huỳnh Trần Yến Nhi 
          \n Freshman at Vietnamese-German University
          \n Location: 🏠 Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat City, Binh Duong Province
          \n My Uni website: https://vgu.edu.vn/
          \n My email: 10623034@student.vgu.edu.vn """)
