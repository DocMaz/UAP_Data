import pandas as pd
import plotly.express as px

# Path to the dataset
file_path_ufos = "/Users/maz/Desktop/UFOs/ufo_sighting_data.csv"

# Read the dataset
df = pd.read_csv(file_path_ufos, low_memory=False)

# Filter the dataset for triangle UFO sightings
triangle_ufos = df[df['UFO_shape'] == 'triangle']

# Create the map plot
fig = px.scatter_geo(triangle_ufos,
                     lat='latitude',
                     lon='longitude',
                     scope='world',
                     title='Triangle UFO Sightings by Latitude',
                     template='plotly_dark',
                     opacity=0.5,
                     projection="natural earth",
                     color_discrete_sequence=['yellow'],
                     hover_name='city',
                     hover_data=['state/province', 'date_documented', 'description'])

# Update geos to show country borders in grey
fig.update_geos(showcoastlines=True, coastlinecolor="White", showland=True, landcolor="Black", showcountries=True, countrycolor="Grey")

# Show the plot
fig.show()
