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
st.balloons()
df = px.data.gapminder()

st.title(":green[Life expectancy]")
st.write("In this page, users can observe top countries in one continent having the highest life expectancy rates in the year 2007.")

option = st.selectbox('**Please choose one continent:**',
('Asia', 'Africa', 'Europe','Americas','Oceania'))
st.caption(f"You selected: {option}")

sub3= df[(df["continent"]==option)]
df3 = sub3.loc[:,['year','lifeExp', 'country']]    

option2=st.radio("**Choose a option:**",('Top 5 countries in 2007', 'Top 10 countries in 2007', 'Top 15 countries in 2007', 'Top 20 countries in 2007'))
df4 = df3.sort_values('lifeExp', ascending=False)
#sub1 = df4[(df4['year']==2007)]
#st.dataframe(sub1)
if option2 == 'Top 5 countries in 2007':    option2a = 5
elif option2 == 'Top 10 countries in 2007':    option2a = 10
elif option2 == 'Top 15 countries in 2007':    option2a = 15
else: option2a = 20

sub4 = df4[(df4['year']==2007)].head(option2a)

df6 = df4.merge(sub4, how = 'inner', on = 'country')

fig3 = px.line(df6, x='year_x', y='lifeExp_x',color='country', 
                labels={'year_x':'Year', 'lifeExp_x':'Life expectancy', 'country':'Country'}
                , width = 900, height = 600 )
fig3.update_layout(font_family="Courier New",font = dict (size = 50))
#fig3 = px.line(df3, x='year', y='lifeExp',color='country', labels={'year':'Year', 'lifeExp':'Life expectancy', 'country':'Country'} )
st.plotly_chart(fig3)

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

[data-testid="stSidebar"]
{
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(bgr_img,unsafe_allow_html= True)

df = px.data.gapminder()

st.title("Life expectancy")
st.write("In this page, users can observe top countries in one continent having the highest life expectancy rates in the year 2007.")

option = st.selectbox('**Please choose one continent:**',
('Asia', 'Africa', 'Europe','Americas','Oceania'))
st.caption(f"You selected: {option}")

sub3= df[(df["continent"]==option)]
df3 = sub3.loc[:,['year','lifeExp', 'country']]    

option2=st.radio("**Choose a option:**",('Top 5 countries in 2007', 'Top 10 countries in 2007', 'Top 15 countries in 2007', 'Top 20 countries in 2007'))
df4 = df3.sort_values('lifeExp', ascending=False)
#sub1 = df4[(df4['year']==2007)]
#st.dataframe(sub1)
if option2 == 'Top 5 countries in 2007':    option2a = 5
elif option2 == 'Top 10 countries in 2007':    option2a = 10
elif option2 == 'Top 15 countries in 2007':    option2a = 15
else: option2a = 20

sub4 = df4[(df4['year']==2007)].head(option2a)

df6 = df4.merge(sub4, how = 'inner', on = 'country')

fig3 = px.line(df6, x='year_x', y='lifeExp_x',color='country', 
                labels={'year_x':'Year', 'lifeExp_x':'Life expectancy', 'country':'Country'}
                , width = 900, height = 600 )
fig3.update_layout(font_family="Courier New",font = dict (size = 50))
#fig3 = px.line(df3, x='year', y='lifeExp',color='country', labels={'year':'Year', 'lifeExp':'Life expectancy', 'country':'Country'} )
st.plotly_chart(fig3)
'''
st.code(code, language='python')