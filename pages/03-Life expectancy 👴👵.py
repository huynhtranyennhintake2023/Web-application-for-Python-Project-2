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

st.title(":green[Life expectancy]")
st.write("**The graph depicting life expectancy from 1952 to 2007 provides a compelling case for the significant advancements in economic and social development during this period. The steady increase in life expectancy across the globe is a testament to the remarkable progress achieved in areas such as healthcare, nutrition, and overall standard of living. The data showcases how countries have been able to invest in the well-being of their citizens, leading to improved access to medical services, better sanitation, and enhanced living conditions. This, in turn, has translated into longer lifespans and a higher quality of life for populations around the world. The upward trend in life expectancy is a clear indicator of the positive impact of economic growth and social policies implemented during this time frame. As nations continue to prioritize the health and welfare of their people, we can expect to see further improvements in life expectancy in the years to come.**")

option = st.selectbox('Please choose one continent:',
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