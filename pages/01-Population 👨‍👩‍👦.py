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

}
</style>
"""
st.markdown(bgr_img,unsafe_allow_html= True)



df = px.data.gapminder()

st.title(":red[Population]")
st.write("""The world population has undergone a remarkable transformation over the past several decades, with profound implications for the global economy and society. A closer examination of the population trends from 1952 to 2007 reveals a striking picture of exponential growth that demands our attention. 
         \n In 1952, the global population stood at a relatively modest 2.6 billion people. However, over the next 55 years, this figure skyrocketed, reaching an astounding 6.7 billion by 2007. This rapid expansion has had a profound impact on resource allocation, economic development, and the overall well-being of communities worldwide. 
         \n The implications of this population explosion are multifaceted and complex. Policymakers, economists, and social scientists must grapple with the challenges posed by this unprecedented growth, from the strain on infrastructure and public services to the need for sustainable development and equitable distribution of resources. Understanding the dynamics of this population shift is crucial in shaping the future of our global community.
         \n The bar chart below depicts each country population in a continent in each year recorded.""")


st.markdown("---")

option1 = st.selectbox('Please choose a continent:',
    ('Asia', 'Africa', 'Europe','Americas','Oceania'))
st.caption(f"You selected: {option1}")
sub1= df[(df["continent"]==option1)]
df1 = sub1.loc[:,['year','pop', 'country', 'iso_alpha']]

years = df['year'].unique()
selected_year = st.selectbox('Choose one year:', years)
sub1a =df[(df['year'] == selected_year)]
df1a = sub1a.loc[:,['pop', 'country', 'year', 'continent']]

    #df1b = df1a.merge(df1, how = 'inner', on = 'country')
df1b = df1a.merge(df1, how = 'inner')
    #st.dataframe(df1b)
    #fig1 = px.scatter_geo(df3, locations="iso_alpha", color="country",hover_name="country",
    #                      size="pop",animation_frame="year",projection="natural earth", title = 'Population', width = 700, height = 800)
fig1 = px.bar(df1b, x = 'country', y = 'pop', color = 'country', 
                  labels = {'pop':'Population', 'country':'Country', 'pop_y':'Population'}, width = 1000, height = 600, text = 'pop')
    
fig1.update_traces(texttemplate='%{text:.3s}', textposition='outside')
fig1.update_layout(uniformtext_minsize=6, xaxis_tickangle=45, showlegend = False)
fig1.update_layout(font_family="Courier New",font = dict (size = 18))
    #fig1.update_traces(textfont_size=12, textangle=45,marker_line_width = 1, marker_line_color = 'white')
st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)

st.markdown("---")

st.subheader("Wanna see one country distribution to the continent total population?")
st.subheader("Check the graph below 👇")

df1b['continent_population'] = df1b['pop'].sum()
df1b['pop_percentage'] = (df1b['pop']/df1b['continent_population'])*100
df1b['per_sum'] = df1b['pop_percentage'].sum()
df1b['per_other'] = df1b['per_sum'] - df1b['pop_percentage']

countries = df1b['country'].unique()
selected_country = st.selectbox('Choose a country:', countries)
sub1c =df1b[(df1b['country'] == selected_country)]
df1c = sub1c.loc[:,['pop', 'country', 'year', 'continent']]

df1d = df1c.merge(df1b, how = 'outer')
df1e = df1c.merge(df1b, how = 'inner')
   

def country_class(value):
       if value == selected_country:
            return selected_country
       if value != selected_country:
            return 'Others'

df1d['country2'] = df1d['country'].map(country_class)

    #df1d.loc[df1d['country'] != selected_country, 'country'] = 'Others'
    #df1d = pd.DataFrame(pd.pivot_table(df1d, values = 'pop', index='country', aggfunc = 'sum'))
df1d = df1d.groupby("country2").sum()
df1d['country2'] = df1d['country'].map(country_class)    
    
    #df['percentage']= df.apply(lambda row: ())
fig1b = px.pie(df1d, values = "pop", names = "country2", width = 800, hole = .3, opacity = 0.8, template='gridon')
    #fig1b = go.Figure(data = [go.Pie(labels = df1d[0:], values = df1d[1:])])
fig1b.update_layout(uniformtext_minsize=8, xaxis_tickangle=45, showlegend = True)
fig1b.update_traces(textfont_size=20,marker=dict( line=dict(color='#000000', width=2)))
fig1b.update_traces(pull=0.05)
st.plotly_chart(fig1b, theme = "streamlit", use_container_width=True)
 
st.header(":red[Are you curious about the code to draw these plots?]")
expander = st.expander("Click this box")  
expander.write ('''
import streamlit as st
\n import plotly.express as px
\n import pandas as pd
\n import numpy as np
\n import datetime

df = px.data.gapminder()

\n option1 = st.selectbox('**Please choose a continent:**',('Asia', 'Africa', 'Europe','Americas','Oceania'))
\n st.caption(f"You selected: {option1}")
\n sub1= df[(df["continent"]==option1)]
\n df1 = sub1.loc[:,['year','pop', 'country', 'iso_alpha']]

\n years = df['year'].unique()
\n selected_year = st.selectbox('**Choose a country:**', years)

\n sub1a =df[(df['year'] == selected_year)]

\n df1a = sub1a.loc[:,['pop', 'country', 'year']]

\n df1b = df1a.merge(df1, how = 'inner')
\n fig1 = px.bar(df1b, x = 'country', y = 'pop', color = 'country', 
                labels = {'pop':'Population', 'country':'Country', 'pop_y':'Population'}, width = 950, height = 600, text = 'pop')

\n fig1.update_traces(texttemplate='%{text:.3s}', textposition='outside')
\n fig1.update_layout(uniformtext_minsize=6, xaxis_tickangle=45, showlegend = False)
\n fig1.update_layout(font_family="Courier New",font = dict (size = 18))

\n st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)

\n st.markdown("---")

\n df1b['continent_population'] = df1b['pop'].sum()
\n df1b['pop_percentage'] = (df1b['pop']/df1b['continent_population'])*100
\n df1b['per_sum'] = df1b['pop_percentage'].sum()
\n df1b['per_other'] = df1b['per_sum'] - df1b['pop_percentage']

\ncountries = df1b['country'].unique()
\n selected_country = st.selectbox('Choose a country:', countries)
\n sub1c =df1b[(df1b['country'] == selected_country)]
\n df1c = sub1c.loc[:,['pop', 'country', 'year', 'continent']]
\n df1d = df1c.merge(df1b, how = 'outer')
\n df1e = df1c.merge(df1b, how = 'inner')
\n def country_class(value):
       if value == selected_country:
            return selected_country
       if value != selected_country:
            return 'Others'

\n df1d['country2'] = df1d['country'].map(country_class)
\n df1d = df1d.groupby("country2").sum()
\n df1d['country2'] = df1d['country'].map(country_class)    
    
\n fig1b = px.pie(df1d, values = "pop", names = "country2", width = 800, hole = .3, opacity = 0.8, template='gridon')
    
\n fig1b.update_layout(uniformtext_minsize=8, xaxis_tickangle=45, showlegend = True)
\n fig1b.update_traces(textfont_size=20,marker=dict( line=dict(color='#000000', width=2)))
\n fig1b.update_traces(pull=0.05)
\n st.plotly_chart(fig1b, theme = "streamlit", use_container_width=True)''')
st.write("---")
st.write ("""Huỳnh Trần Yến Nhi 
          \n Freshman at Vietnamese-German University
          \n Location: 🏠 Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat City, Binh Duong Province
          \n My Uni website: https://vgu.edu.vn/
          \n My email: 10623034@student.vgu.edu.vn """)

