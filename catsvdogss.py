import streamlit as st
import pandas as pd
import numpy as np
import scipy as sp
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.graph_objs import *
init_notebook_mode()
import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly

### Inserting an Image

from PIL import Image
image = 'https://www.gannett-cdn.com/-mm-/8b15e053fba5438a91d1bff3d4704868a0ce7579/c=68-0-731-373/local/-/media/2018/05/10/USATODAY/usatsports/MotleyFool-TMOT-816b1ceb-0ece06e3.jpg?auto=webp&format=pjpg&width=1200'
st.image(image)


### Title of the page

st.title('Cats and Dogs Households in USA')

### subheader

st.write('Data Link : https://www.kaggle.com/yamqwe/cat-vs-dog-popularity-in-u-se ')

### Loading Data

df = pd.read_csv('https://raw.githubusercontent.com/sarakaddoura/turbo-tribble/main/catsvdogs.csv')


### Insert Sidebar of plots

add_selectbox = st.sidebar.selectbox(
    "What would you like to see?",
    ["View all :)", "Explore Data","Bar Plot 1", "Bar Plot 2", "Bar Plot 3",
     "3D Plot 1","3D Plot 2", "Interactive Map", "Animation"]
)

### View all
st.balloons()
if add_selectbox == 'View all :)':
        ### Exploring Data
        st.subheader('Exploring the Data')
        st.write(df.head())
        st.text('The data i chose is about how frequent Cats and dogs are found in USA households')

        ### Bar Plot 1
        data = [Bar(x=df.Location,
                    y=df['Number of Households (in 1000)'])]

        layout_1 = Layout(title = 'Number of household/Each state', xaxis_title = 'State', yaxis_title = 'Number of Household')
        fig1 = dict(data = data, layout = layout_1)

        iplot(fig1)
        st.write(fig1)
        st.text('''This visualization explains how many households
        there are in each state in USA. It is clear that California,
        New York and Texas have the highest number of households''')

        ### Bar Plot 2
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Bar Plot 2"}</h1>', unsafe_allow_html=True)
        data = [Bar(x=df['Location'],
                y=df['Cat Owning Households'])]

        layout_3 = Layout(title = 'Cat Owning Households/State', xaxis_title = 'State', yaxis_title = 'Cat Owning Households')
        fig2 = dict(data = data, layout = layout_3)
        iplot(fig2)
        st.write(fig2)
        st.text(''' The following bar plot shows how many households have cats
        It is obvious that California, New York and Texas have
        the highest number of households with cats''')

        ### Bar Plot 3
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Bar Plot 3"}</h1>', unsafe_allow_html=True)


        data = [Bar(x=df['Location'],
                    y=df['Dog Owning Households (1000s)'])]

        layout_3 = Layout(title = 'Dog Owning Households/State', xaxis_title = 'State', yaxis_title = 'Dog Owning Households')
        fig3 = dict(data = data, layout = layout_3)

        iplot(fig3)
        st.write(fig3)
        st.text('''The following bar plot shows how many households have Dogs
        It is obvious that California, Florida and Texas have the
        highest number of households with Dogs''')

        ### 3D Plot 1
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"3D Plot 1"}</h1>', unsafe_allow_html=True)


        fig4 = px.scatter_3d(df, y = 'Number of Households (in 1000)', x = 'Dog Owning Households (1000s)', z = 'Cat Owning Households', color = 'Location')
        fig4.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        fig4.show()
        st.write(fig4)

        st.text('''The following 3D scatter plot explains from the
        total number of householdshow many of them are
        cats and dogs owning households''')

        ### 3D Plot 2
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"3D Plot 2"}</h1>', unsafe_allow_html=True)

        fig5 = px.scatter_3d(df, y = 'Percentage of Dog Owners', x = 'Percentage of households with pets', z = 'Percentage of Cat Owners', color = 'Location')
        fig5.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        fig5.show()
        st.write(fig5)

        st.text('''The following 3D scatter plot explains the percentage of dogs
        and cats owners from the total percentage of households with pets''')

        ### Interactive map
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Interactive Map"}</h1>', unsafe_allow_html=True)

        us_state_to_abbrev = {

            "Alabama": "AL",
            "Arizona": "AZ",
            "Arkansas": "AR",
            "California": "CA",
            "Colorado": "CO",
            "Connecticut": "CT",
            "Delaware": "DE",
            "Florida": "FL",
            "Georgia": "GA",
            "Hawaii": "HI",
            "Idaho": "ID",
            "Illinois": "IL",
            "Indiana": "IN",
            "Iowa": "IA",
            "Kansas": "KS",
            "Kentucky": "KY",
            "Louisiana": "LA",
            "Maine": "ME",
            "Maryland": "MD",
            "Massachusetts": "MA",
            "Michigan": "MI",
            "Minnesota": "MN",
            "Mississippi": "MS",
            "Missouri": "MO",
            "Montana": "MT",
            "Nebraska": "NE",
            "Nevada": "NV",
            "New Hampshire": "NH",
            "New Jersey": "NJ",
            "New Mexico": "NM",
            "New York": "NY",
            "North Carolina": "NC",
            "North Dakota": "ND",
            "Ohio": "OH",
            "Oklahoma": "OK",
            "Oregon": "OR",
            "Pennsylvania": "PA",
            "Rhode Island": "RI",
            "South Carolina": "SC",
            "South Dakota": "SD",
            "Tennessee": "TN",
            "Texas": "TX",
            "Utah": "UT",
            "Vermont": "VT",
            "Virginia": "VA",
            "Washington": "WA",
            "West Virginia": "WV",
            "Wisconsin": "WI",
            "Wyoming": "WY"
        }

        # invert the dictionary
        abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
        df['abbrev_to_us_state'] = abbrev_to_us_state

        fig6 = px.choropleth(df,
                            locations="abbrev_to_us_state",
                            color="Number of Pet Households (in 1000)",
                            hover_name="Location",
                            locationmode = 'USA-states',
                           color_continuous_scale=px.colors.sequential.Plasma)
        fig6.update_layout(
            title_text = 'Number of pet Households',
            geo_scope='usa',
        )

        fig6.show()
        st.write(fig6)
        st.text(''' The following Map explains the number of pet households in USA
        states and it is clear that California and Texas have the highest
        number of Households with pets''')

        ### Animation
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Animation"}</h1>', unsafe_allow_html=True)

        fig7 = px.bar(df, x = "Location", y = "Dog Owning Households (1000s)",
                     animation_frame = "Number of Pet Households (in 1000)",
                     range_y=[0,10000])
        fig7.show()
        st.write(fig7)
        st.text(''' This animation explains the variation of dog owning households
        in each state''')



### Data Exploration

if add_selectbox == 'Explore Data' :
    ### Exploring Data
    st.subheader('Exploring the Data')
    st.write(df.head())
    st.text('The data i chose is about how frequent Cats and dogs are found in USA households')

### Bar Plot 1

if add_selectbox == 'Bar Plot 1' :
    data = [Bar(x=df.Location,
                y=df['Number of Households (in 1000)'])]

    layout_1 = Layout(title = 'Number of household/Each state', xaxis_title = 'State', yaxis_title = 'Number of Household')
    fig1 = dict(data = data, layout = layout_1)

    iplot(fig1)
    st.write(fig1)
    st.text('''
    This visualization explains how many households there are in each state in USA.
    It is clear that California, New York and Texas have the highest number of households''')

### Bar Plot 2

if add_selectbox == 'Bar Plot 2':
    st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Bar Plot 2"}</h1>', unsafe_allow_html=True)
    data = [Bar(x=df['Location'],
            y=df['Cat Owning Households'])]

    layout_3 = Layout(title = 'Cat Owning Households/State', xaxis_title = 'State', yaxis_title = 'Cat Owning Households')
    fig2 = dict(data = data, layout = layout_3)
    iplot(fig2)
    st.write(fig2)
    st.text(''' The following bar plot shows how many households have cats.
It is obvious that California, New York and Texas have the highest number
of households with cats''')

### Bar Plot 3

if add_selectbox == 'Bar Plot 3' :
    st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Bar Plot 3"}</h1>', unsafe_allow_html=True)


    data = [Bar(x=df['Location'],
                y=df['Dog Owning Households (1000s)'])]

    layout_3 = Layout(title = 'Dog Owning Households/State', xaxis_title = 'State', yaxis_title = 'Dog Owning Households')
    fig3 = dict(data = data, layout = layout_3)

    iplot(fig3)
    st.write(fig3)
    st.text('''The following bar plot shows how many households have Dogs
It is obvious that California, Florida and Texas have the
highest number of households with Dogs''')

### 3D Plot 1

if add_selectbox == '3D Plot 1':
    st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"3D Plot 1"}</h1>', unsafe_allow_html=True)


    fig4 = px.scatter_3d(df, y = 'Number of Households (in 1000)', x = 'Dog Owning Households (1000s)', z = 'Cat Owning Households', color = 'Location')
    fig4.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig4.show()
    st.write(fig4)

    st.text('''The following 3D scatter plot explains from the
total number of householdshow many of them are
cats and dogs owning households''')

### 3D Plot 2

if add_selectbox == '3D Plot 2':
    st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"3D Plot 2"}</h1>', unsafe_allow_html=True)

    fig5 = px.scatter_3d(df, y = 'Percentage of Dog Owners', x = 'Percentage of households with pets', z = 'Percentage of Cat Owners', color = 'Location')
    fig5.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig5.show()
    st.write(fig5)

    st.text('''The following 3D scatter plot explains the percentage of dogs
and cats owners from the total percentage of households with pets''')

### Interactive map

if add_selectbox == 'Interactive map':
        st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Interactive Map"}</h1>', unsafe_allow_html=True)

        us_state_to_abbrev = {

            "Alabama": "AL",
            "Arizona": "AZ",
            "Arkansas": "AR",
            "California": "CA",
            "Colorado": "CO",
            "Connecticut": "CT",
            "Delaware": "DE",
            "Florida": "FL",
            "Georgia": "GA",
            "Hawaii": "HI",
            "Idaho": "ID",
            "Illinois": "IL",
            "Indiana": "IN",
            "Iowa": "IA",
            "Kansas": "KS",
            "Kentucky": "KY",
            "Louisiana": "LA",
            "Maine": "ME",
            "Maryland": "MD",
            "Massachusetts": "MA",
            "Michigan": "MI",
            "Minnesota": "MN",
            "Mississippi": "MS",
            "Missouri": "MO",
            "Montana": "MT",
            "Nebraska": "NE",
            "Nevada": "NV",
            "New Hampshire": "NH",
            "New Jersey": "NJ",
            "New Mexico": "NM",
            "New York": "NY",
            "North Carolina": "NC",
            "North Dakota": "ND",
            "Ohio": "OH",
            "Oklahoma": "OK",
            "Oregon": "OR",
            "Pennsylvania": "PA",
            "Rhode Island": "RI",
            "South Carolina": "SC",
            "South Dakota": "SD",
            "Tennessee": "TN",
            "Texas": "TX",
            "Utah": "UT",
            "Vermont": "VT",
            "Virginia": "VA",
            "Washington": "WA",
            "West Virginia": "WV",
            "Wisconsin": "WI",
            "Wyoming": "WY"
        }

        # invert the dictionary
        abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
        df['abbrev_to_us_state'] = abbrev_to_us_state

        fig6 = px.choropleth(df,
                            locations="abbrev_to_us_state",
                            color="Number of Pet Households (in 1000)",
                            hover_name="Location",
                            locationmode = 'USA-states',
                           color_continuous_scale=px.colors.sequential.Plasma)
        fig6.update_layout(
            title_text = 'Number of pet Households',
            geo_scope='usa',
        )

        fig6.show()
        st.write(fig6)
        st.text(''' The following Map explains the number of pet households in USA
        states and it is clear that California and Texas have the highest
        number of Households with pets''')


### Animation

if add_selectbox == 'Animation':
    st.markdown(f'<h1 style="color:#337BFF;font-size:24px;">{"Animation"}</h1>', unsafe_allow_html=True)

    fig7 = px.bar(df, x = "Location", y = "Dog Owning Households (1000s)",
                 animation_frame = "Number of Pet Households (in 1000)",
                 range_y=[0,10000])
    fig7.show()
    st.write(fig7)
    st.text(''' This animation explains the variation of dog owning households
in each state''')
