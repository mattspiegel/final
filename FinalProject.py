"""
Name: Matthew Spiegel
CS 230: Section SN2
Data: National Parks in New York
URL:

Description: This interactive program highlights and displays important information about
New York State historical sites and parks. First, it allows the user to chose specific columns in the
dataframe and select columns to sort the data, then presents the information in a table.
Then, a map is displayed with dots to signfiy the locations of all sites throughout NY. A chart
is also avaliable to view that displays the number of sites registered between the years of 1960
and 2019, and displays the average, median, standard deviation of the number of site registered
each year. Finally, the user can select a specific site from a dropdown menu to learn more information
about it. The program ends with 4 options the user can choose that brings them to external
websites to learn more information about their chosen selection.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk
import random

def customize_text(phrase='NEW YORK STATE HISTORICAL SITES'):
    st.markdown("""
    <style>
    .Customize {
        font-size:35px !important;
        color: blue;
        font-weight: bold;
        font-family: Modern Love Caps;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<p class="Customize">{phrase}</p>', unsafe_allow_html=True)

customize_text()

path = "National_Register_of_Historic_Places.csv"
df = pd.read_csv(path)

try:
    options = ['Resource Name','County','National Register Date','National Register Number','Longitude','Latitude','Georeference']
    st.sidebar.header('Customization Options')
    selections = st.sidebar.multiselect('Select site information to include in the table: ',options)
    customizedf = df[selections]
    sort = st.sidebar.selectbox('Sort by:', selections)
    customizedf = customizedf.sort_values(by=[sort],ascending=[True])
    st.subheader(f'New York Site Information, sorted by {sort.lower()}')
    st.write(customizedf)
except:
    st.write('***SELECT SITE INFORMATION ON THE LEFT PANEL TO BEGIN!***')

def view_map():
    df = pd.read_csv(path)
    Locations = []
    for name in df['Resource Name']:
        Locations.append(name)
    Longitude = []
    for longitude in df['Longitude']:
        Longitude.append(longitude)
    Latitude = []
    for latitude in df['Latitude']:
        Latitude.append(latitude)

    LOCATION = list(zip(Locations,Latitude,Longitude))

    df = pd.DataFrame(LOCATION,columns=["Park Name", "lat", "lon"])
    st.subheader("Customized NY State Historical Sites Map with Tool Tips")
    st.write("[ZOOM IN to the LIGHT GREEN DOTS to see parks throughout NY]")

    if st.button("Can't find any sites?"):
        st.write ("You must zoom further into New York to begin to see the green dots that symbolize a site.")
    else:
        st.write("So many sites to navigate!")



    view_state = pdk.ViewState(
        latitude=df["lat"].mean(),
        longitude=df["lon"].mean(),
        zoom = 7,
        pitch = 0)

    layer1 = pdk.Layer('ScatterplotLayer',
                      data = df,
                      get_position = '[lon, lat]',
                      get_radius = 200,
                      get_color = [102,204,0],
                      pickable = True)

    tool_tip = {"html": "Site Name:<br/> <b>{Park Name}</b> ",
                "style": { "backgroundColor": "steelblue",
                            "color": "white"}}
    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=view_state,
        layers=[layer1],
        tooltip= tool_tip
    )
    st.pydeck_chart(map)

def bar_graph(color='aqua',edgecolor='black'):
    df = pd.read_csv(path)
    df = df.dropna()
    listofDates = df['National Register Date'].tolist()
    y = {}
    x = []
    for date in listofDates:
        x.append(date)

    for value in x:
        z = value.split('/')
        if z[2] not in y:
            y[z[2]] = 1
        else:
            y[z[2]] += 1
    keyslist = list(sorted(y.keys()))
    values = list(y.values())
    plt.bar(keyslist,values,width=1,color=color,edgecolor=edgecolor)
    plt.title("Number of NY State Historical Sites Nationally Registered Per Year")
    plt.xlabel("Year")
    plt.ylabel("Num of NY State Historical Sites Registered")
    MAX = max(values)
    ylabels = np.arange(0,MAX*1.20,round(MAX*.16))
    plt.yticks(ylabels)
    plt.xticks(np.arange(0,60,4),rotation=90)


    avg_parks_registered_per_year = np.mean(values)
    std_parks_registered_per_year = np.std(values)
    med_parks_registered_per_year = np.median(values)

    st.write(f'DID YOU KNOW? On average, from 1960 to 2019, {round(avg_parks_registered_per_year,2)} NY state parks are registered yearly, with a standard deviation of {round(std_parks_registered_per_year)} and median of {round(med_parks_registered_per_year)}.')

    return plt #returns finalized bar graph

def show_bar_graph():
    if st.button("CLICK HERE to display a chart showing the number of historical sites registered each year!"):
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(bar_graph())

def park_information():
    customize_text("Historical Site Information")
    df = pd.read_csv(path)
    Locations = []
    for name in df['Resource Name']:
        Locations.append(name)
    Longitude = []
    for longitude in df['Longitude']:
        Longitude.append(longitude)
    Latitude = []
    for latitude in df['Latitude']:
        Latitude.append(latitude)

    LOCATION = list(zip(Locations,Latitude,Longitude))

    df = pd.DataFrame(LOCATION,columns=["Park Name", "lat", "lon"])

    park_name = st.selectbox('Select a historical site to learn more about it: ',df['Park Name'])

    st.write(df[df['Park Name'] == park_name])

    st.write(f"{park_name} is a great historical site! Have you visited it before?")
    choices = ['Yes','No']

    answer = st.radio("Yes or No: ", choices)
    if answer == "Yes":
        x = st.slider('Awesome! How would you rate your experience? ',0.0,10.0,1.0)
    else:
        st.write("Hopefully you can visit it soon!")

def show_image(park_name='Bryant Park', urlAddress='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/New-York_-_Bryant_Park.jpg/1024px-New-York_-_Bryant_Park.jpg'):
    st.write("Do you know the name of this famous park?")
    st.image(urlAddress,width=500)
    park_guess = st.text_input("Park Name: ", "").lower()
    if park_guess == park_name.lower():
        st.write(f"You got it right! Isn't {park_name} beautiful? ")
    elif park_guess == "":
        pass
    else:
        st.write(f"This is actually {park_name}!")

def next_steps():
    import webbrowser
    st.subheader("What's next?")
    options = ['New York City Landmarks','State Parks in Upstate NY','Hiking Trails in NY','Top Rated Tourist Attractions']
    response = st.radio("What do you want to learn more about? ", options)
    if response == options[0]:
        if st.button('New York City Landmarks'):
            webbrowser.open_new_tab('https://www.tripadvisor.com/Attractions-g60763-Activities-c47-New_York_City_New_York.html')
    elif response == options[1]:
        if st.button('State Parks in Upstate NY'):
            webbrowser.open_new_tab('https://www.mtnscoop.com/features/state-parks-in-upstate-new-york')
    elif response == options[2]:
        if st.button('Hiking Trails in NY'):
            webbrowser.open_new_tab('https://www.alltrails.com/us/new-york')
    elif response == options[3]:
        if st.button('Top Rated Tourist Attractions'):
            webbrowser.open_new_tab('https://www.planetware.com/tourist-attractions/new-york-usny.htm')


def main():
    view_map()
    show_bar_graph()
    show_image()
    park_information()
    next_steps()

main()


