import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def plot_map():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Add map features such as coastlines, borders, and land
    ax.coastlines()
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
    ax.add_feature(cartopy.feature.LAND, edgecolor='black')

    # Set extent (optional) - adjust the values as needed
    ax.set_extent([-130, -60, 20, 60], crs=ccrs.PlateCarree())

    # Add title (optional)
    ax.set_title('Map Title')

    # Save the map to an image file
    plt.savefig('image.png', bbox_inches='tight')

# Call the function to plot the map
plot_map()
