python
import pandas as pd
import matplotlib.pyplot as plt
import folium

def load_data(file_path):
    """Load housing market data from a CSV file."""
    return pd.read_csv(file_path)

# Load the dataset
data = load_data('UAE_Housing_Market_Data.csv')

# Example: Filter data for a specific city and property type
city = 'Dubai'
property_type = 'Apartment'
filtered_data = data[(data['City'] == city) & (data['Property_Type'] == property_type)]

# Visualization: Plot average property prices by area
average_prices = filtered_data.groupby('Area')['Price'].mean()
plt.figure(figsize=(10, 6))
average_prices.plot(kind='bar', color='skyblue')
plt.title(f"Average Property Prices in {city} for {property_type}s")
plt.xlabel('Area')
plt.ylabel('Average Price (AED)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Interactive Map: Show housing availability
map_center = [25.276987, 55.296249]  # Dubai coordinates
housing_map = folium.Map(location=map_center, zoom_start=10)
for _, row in filtered_data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Price: {row['Price']} AED\nBeds: {row['Beds']}\nBaths: {row['Baths']}"
    ).add_to(housing_map)

# Save map as HTML
housing_map.save('housing_map.html')
