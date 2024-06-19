import streamlit as st

from streamlit_space import space
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

}
</style>
"""
st.set_page_config(layout="wide")
st.balloons()

st.markdown(bgr_img,unsafe_allow_html= True)

df = px.data.gapminder()

st.title(':red[Population]')
st.write("In this page, users can see each country population in 1 continent in the bar chart and its distribution to the continent total population in the pie chart.")

st.markdown("---")

option1 = st.selectbox('**Please choose a continent:**',
('Asia', 'Africa', 'Europe','Americas','Oceania'))
st.caption(f"You selected: {option1}")
sub1= df[(df["continent"]==option1)]
df1 = sub1.loc[:,['year','pop', 'country', 'iso_alpha']]

years = df['year'].unique()
selected_year = st.selectbox('**Choose a country:**', years)
sub1a =df[(df['year'] == selected_year)]
df1a = sub1a.loc[:,['pop', 'country', 'year']]

#df1b = df1a.merge(df1, how = 'inner', on = 'country')
df1b = df1a.merge(df1, how = 'inner')
#st.dataframe(df1b)
#fig1 = px.scatter_geo(df3, locations="iso_alpha", color="country",hover_name="country",
#                      size="pop",animation_frame="year",projection="natural earth", title = 'Population', width = 700, height = 800)
fig1 = px.bar(df1b, x = 'country', y = 'pop', color = 'country', 
                labels = {'pop':'Population', 'country':'Country', 'pop_y':'Population'}, width = 950, height = 600, text = 'pop')

fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig1.update_layout(uniformtext_minsize=8, xaxis_tickangle=45, showlegend = False)
fig1.update_layout(font_family="Courier New",font = dict (size = 50))
#fig1.update_traces(textfont_size=12, textangle=45,marker_line_width = 1, marker_line_color = 'white')
st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)

code = ''' 
import streamlit as st

from streamlit_space import space
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

}
</style>
"""
st.set_page_config(layout="wide")

st.markdown(bgr_img,unsafe_allow_html= True)

df = px.data.gapminder()

st.title(':white[Population]')
st.write("In this page, users can see each country population in 1 continent in the bar chart and its distribution to the continent total population in the pie chart.")

st.markdown("---")

option1 = st.selectbox('**Please choose a continent:**',
('Asia', 'Africa', 'Europe','Americas','Oceania'))
st.caption(f"You selected: {option1}")
sub1= df[(df["continent"]==option1)]
df1 = sub1.loc[:,['year','pop', 'country', 'iso_alpha']]

years = df['year'].unique()
selected_year = st.selectbox('**Choose a country:**', years)
sub1a =df[(df['year'] == selected_year)]
df1a = sub1a.loc[:,['pop', 'country', 'year']]

#df1b = df1a.merge(df1, how = 'inner', on = 'country')
df1b = df1a.merge(df1, how = 'inner')
#st.dataframe(df1b)
#fig1 = px.scatter_geo(df3, locations="iso_alpha", color="country",hover_name="country",
#                      size="pop",animation_frame="year",projection="natural earth", title = 'Population', width = 700, height = 800)
fig1 = px.bar(df1b, x = 'country', y = 'pop', color = 'country', 
                labels = {'pop':'Population', 'country':'Country', 'pop_y':'Population'}, width = 950, height = 600, text = 'pop')

fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig1.update_layout(uniformtext_minsize=8, xaxis_tickangle=45, showlegend = False)
fig1.update_layout(font_family="Courier New",font = dict (size = 50))
#fig1.update_traces(textfont_size=12, textangle=45,marker_line_width = 1, marker_line_color = 'white')
st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)'''

st.code(code, language='python')

