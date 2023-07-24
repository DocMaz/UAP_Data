import pandas as pd
import plotly.graph_objects as go
import webbrowser
import os

# Path to the UFO sightings dataset
file_path_ufos = "/Users/maz/Desktop/UFOs/ufo_sighting_data.csv"

# Read the dataset
df = pd.read_csv(file_path_ufos, low_memory=False)

# Convert 'Date_time' column to datetime format
df['Date_time'] = pd.to_datetime(df['Date_time'], errors='coerce')

# Drop rows with invalid or missing dates
df = df.dropna(subset=['Date_time'])

# Group data by month (you can change to 'Y' for yearly grouping if needed)
df['YearMonth'] = df['Date_time'].dt.to_period('M')
grouped_dates = df['YearMonth'].unique()

frames = []

for date in grouped_dates:
    subset = df[df['YearMonth'] == date]
    
    triangle_indices = subset[subset['UFO_shape'] == 'triangle'].index
    light_indices = subset[subset['UFO_shape'] == 'light'].index
    circle_indices = subset[(subset['UFO_shape'] != 'triangle') & (subset['UFO_shape'] != 'light')].index
    
    frame = go.Frame(
        data=[
            go.Scatter3d(
                x=subset.loc[triangle_indices, 'longitude'],
                y=subset.loc[triangle_indices, 'latitude'],
                z=[15] * len(triangle_indices),
                mode='markers',
                marker=dict(symbol='diamond', size=10, color='purple', opacity=0.7),
                text=subset.loc[triangle_indices, 'description'],
                hoverinfo='text'
            ),
            go.Scatter3d(
                x=subset.loc[light_indices, 'longitude'],
                y=subset.loc[light_indices, 'latitude'],
                z=[10] * len(light_indices),
                mode='markers',
                marker=dict(size=10, color='yellow', opacity=0.5),
                text=subset.loc[light_indices, 'description'],
                hoverinfo='text'
            ),
            go.Scatter3d(
                x=subset.loc[circle_indices, 'longitude'],
                y=subset.loc[circle_indices, 'latitude'],
                z=[5] * len(circle_indices),
                mode='markers',
                marker=dict(size=10, color='white', opacity=0.7),
                text=subset.loc[circle_indices, 'description'],
                hoverinfo='text'
            )
        ],
        name=str(date)
    )
    frames.append(frame)

# Create the layout for the plot
layout = go.Layout(
    title='3D Interactive Plot of UFO Sightings Over Time',
    scene=dict(
        xaxis=dict(title='Longitude', showbackground=True, backgroundcolor='black'),
        yaxis=dict(title='Latitude', showbackground=True, backgroundcolor='black'),
        zaxis=dict(title='UFO Shape', showbackground=False, backgroundcolor='black'),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
        aspectmode='manual',
        aspectratio=dict(x=2, y=1, z=0.5)
    ),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, mode='immediate loop')]
        )]
    )]
)

# Create the figure
fig = go.Figure(data=frames[0]['data'], layout=layout, frames=frames)

# Save the figure as an HTML file
file_path = "/Users/maz/Desktop/UFOs/3d_plot_animated.html"
fig.write_html(file_path)

# Open the saved HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath(file_path))
