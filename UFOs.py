import pandas as pd
import plotly.graph_objects as go
import webbrowser
import os

# Path to the UFO sightings dataset
file_path_ufos = "/Users/maz/Desktop/UFOs/ufo_sighting_data.csv"

# Read the dataset
df = pd.read_csv(file_path_ufos)

# Filter out rows with NaN values for latitude and longitude
df = df.dropna(subset=['latitude', 'longitude'])

# Create markers for triangle, light, and other UFO shapes
triangle_indices = df[df['UFO_shape'] == 'triangle'].index
light_indices = df[df['UFO_shape'] == 'light'].index
circle_indices = df[(df['UFO_shape'] != 'triangle') & (df['UFO_shape'] != 'light')].index

# Create a 3D scatter plot using graph_objects
trace_triangles = go.Scatter3d(
    x=df.loc[triangle_indices, 'longitude'],
    y=df.loc[triangle_indices, 'latitude'],
    z=[15] * len(triangle_indices),  # Highest on the z-axis
    mode='markers',
    marker=dict(
        symbol='diamond',  # Using diamond to represent triangle-shaped UFOs
        size=10,
        color='purple',
        opacity=0.7
    ),
    text=df.loc[triangle_indices, 'description'],
    hoverinfo='text'
)

trace_lights = go.Scatter3d(
    x=df.loc[light_indices, 'longitude'],
    y=df.loc[light_indices, 'latitude'],
    z=[10] * len(light_indices),  # Middle on the z-axis
    mode='markers',
    marker=dict(
        size=10,
        color='yellow',
        opacity=0.5  # 50% opacity
    ),
    text=df.loc[light_indices, 'description'],
    hoverinfo='text'
)

trace_circles = go.Scatter3d(
    x=df.loc[circle_indices, 'longitude'],
    y=df.loc[circle_indices, 'latitude'],
    z=[5] * len(circle_indices),  # Lowest on the z-axis
    mode='markers',
    marker=dict(
        size=10,
        color='white',
        opacity=0.7
    ),
    text=df.loc[circle_indices, 'description'],
    hoverinfo='text'
)

# Create the layout for the plot
layout = go.Layout(
    title='3D Interactive Plot of UFO Sightings Over Time',
    scene=dict(
        xaxis=dict(title='Longitude', showbackground=True, backgroundcolor='black'),
        yaxis=dict(title='Latitude', showbackground=True, backgroundcolor='black'),
        zaxis=dict(title='UFO Shape', showbackground=False, backgroundcolor='black'),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
        aspectmode='manual',
        aspectratio=dict(x=2, y=1, z=0.5)  # Adjust the aspect ratio for better view of the world map
    ),
    plot_bgcolor='black',  # Set the plot background color to black
    paper_bgcolor='black',  # Set the paper background color to black
    font=dict(color='white')
)

# Create the figure
fig = go.Figure(data=[trace_triangles, trace_lights, trace_circles], layout=layout)

# Save the figure as an HTML file
file_path = "/Users/maz/Desktop/UFOs/3d_plot.html"
fig.write_html(file_path)

# Open the saved HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath(file_path))
