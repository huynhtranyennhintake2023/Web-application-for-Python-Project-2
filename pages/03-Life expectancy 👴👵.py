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
st.markdown(ngr_img,unsafe_allow_html= True)

df = px.data.gapminder()

st.title(":green[Life expectancy]")
st.write(":black[On this page, users can observe top countries in one continent having the highest life expectancy rates in the year 2007.]")

option = st.selectbox('**Please choose one continent:',
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

st.header(":green[Are you curious about the code to draw this plot?]")
expander = st.expander("**Click this box**") 
expander.write ('''
import streamlit as st
\nimport plotly.express as px
\nimport pandas as pd
\nimport numpy as np
\nimport datetime

\ndf = px.data.gapminder()

\noption = st.selectbox('**Please choose one continent:**', ('Asia', 'Africa', 'Europe','Americas','Oceania'))
\nst.caption(f"You selected: {option}")

\nsub3= df[(df["continent"]==option)]
\ndf3 = sub3.loc[:,['year','lifeExp', 'country']]    

\noption2=st.radio("**Choose a option:**",('Top 5 countries in 2007', 'Top 10 countries in 2007', 'Top 15 countries in 2007', 'Top 20 countries in 2007'))
\ndf4 = df3.sort_values('lifeExp', ascending=False)
\nif option2 == 'Top 5 countries in 2007':    option2a = 5
\nelif option2 == 'Top 10 countries in 2007':    option2a = 10
\nelif option2 == 'Top 15 countries in 2007':    option2a = 15
\nelse: option2a = 20

\nsub4 = df4[(df4['year']==2007)].head(option2a)

\ndf6 = df4.merge(sub4, how = 'inner', on = 'country')

\nfig3 = px.line(df6, x='year_x', y='lifeExp_x',color='country', 
                labels={'year_x':'Year', 'lifeExp_x':'Life expectancy', 'country':'Country'}
                , width = 900, height = 600 )
\nfig3.update_layout(font_family="Courier New",font = dict (size = 50))
\n st.plotly_chart(fig3)''')
st.write("---")
st.write ("""Huỳnh Trần Yến Nhi 
          \n Freshman at Vietnamese-German University
          \n Location: 🏠 Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat City, Binh Duong Province
          \n My Uni website: https://vgu.edu.vn/
          \n My email: 10623034@student.vgu.edu.vn """)