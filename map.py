import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import webbrowser
import os

# Path to the dataset
file_path_ufos = "/Users/maz/Desktop/UFOs/ufo_sighting_data.csv"

# Read the dataset
df = pd.read_csv(file_path_ufos, low_memory=False)

# Convert the 'latitude' column to numeric
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')

# Filter the dataset for triangle UFO sightings
triangle_ufos = df[df['UFO_shape'] == 'triangle']

# Create the base map
fig = sp.make_subplots(rows=1, cols=1, subplot_titles=["Triangle UFO Sightings by Latitude"])

# Add the triangle UFO sightings to the map
fig.add_trace(go.Scattergeo(
    lon=triangle_ufos['longitude'],
    lat=triangle_ufos['latitude'],
    mode='markers',
    marker=dict(color='yellow', opacity=0.5),
    hoverinfo='text',
    hovertext=triangle_ufos['city'] + ', ' + triangle_ufos['state/province'] + '<br>' + triangle_ufos['date_documented'] + '<br>' + triangle_ufos['description']
))

# Add a shaded region for the predominant latitudinal range
fig.add_trace(go.Scattergeo(
    lon=[-180, 180, 180, -180, -180],
    lat=[39, 39, 53, 53, 39],
    mode='none',
    fill='toself',
    fillcolor='blue',
    opacity=0.5
))

# Update the layout to show a world map with country borders
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="White",
    showland=True,
    landcolor="Black",
    showcountries=True,
    countrycolor="Grey",
    projection_type="natural earth"
)

fig.update_layout(title_text='Triangle UFO Sightings by Latitude', template='plotly_dark')

# Save the figure as an HTML file
file_path = "/Users/maz/Desktop/UFOs/triangle_ufo_map.html"
fig.write_html(file_path)

# Open the saved HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath(file_path))
