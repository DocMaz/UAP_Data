import pandas as pd
import matplotlib.pyplot as plt

# Path to the UFO sightings dataset
file_path_ufos = "/Users/maz/Desktop/UFOs/ufo_sighting_data.csv"

# Read the dataset
df = pd.read_csv(file_path_ufos, low_memory=False)

# Filter for triangle UFOs
triangle_ufos = df[df['UFO_shape'] == 'triangle']

# Define bin edges for latitude in increments of 10
bin_edges = list(range(int(float(triangle_ufos['latitude'].min())), int(float(triangle_ufos['latitude'].max())) + 10, 10))

# Plot histogram
plt.figure(figsize=(12, 7))
plt.hist(triangle_ufos['latitude'], bins=bin_edges, color='purple', alpha=0.7)
plt.title('Distribution of Triangle UFO Sightings by Latitude', fontsize=16)
plt.xlabel('Latitude', fontsize=14)
plt.ylabel('Number of Sightings', fontsize=14)
plt.xticks(bin_edges, fontsize=12)  # Set x-axis ticks to match bin edges
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # Adjust layout for better label visibility
plt.show()
