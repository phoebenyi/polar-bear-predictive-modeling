import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
data = pd.read_csv('processed_data/processed_population_dynamics_data_with_trends.csv')

# Separate data by region for visualization
regions = data['REGION'].unique()

# Create trend visualizations
for region in regions:
    region_data = data[data['REGION'] == region]

    # Time series plot for SEA_ICE_EXTENT
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['DAY'], region_data['SEA_ICE_EXTENT'], label='Daily Sea Ice Extent', alpha=0.5)
    plt.plot(region_data['DAY'], region_data['SEA_ICE_EXTENT_7D_AVG'], label='7-Day Rolling Avg', linewidth=2)
    plt.title(f"Sea Ice Extent Trends - {region}")
    plt.xlabel('Day of the Year')
    plt.ylabel('Sea Ice Extent (km²)')
    plt.legend()
    plt.grid()
    plt.savefig(f"visualizations/{region}_sea_ice_extent_trend.png")
    plt.show()

    # Time series plot for SEA_ICE_AREA
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['DAY'], region_data['SEA_ICE_AREA'], label='Daily Sea Ice Area', alpha=0.5)
    plt.plot(region_data['DAY'], region_data['SEA_ICE_AREA_7D_AVG'], label='7-Day Rolling Avg', linewidth=2)
    plt.title(f"Sea Ice Area Trends - {region}")
    plt.xlabel('Day of the Year')
    plt.ylabel('Sea Ice Area (km²)')
    plt.legend()
    plt.grid()
    plt.savefig(f"visualizations/{region}_sea_ice_area_trend.png")
    plt.show()

    # Daily differences visualization for SEA_ICE_EXTENT
    plt.figure(figsize=(10, 6))
    plt.plot(region_data['DAY'], region_data['SEA_ICE_EXTENT_DIFF'], label='Daily Change in Sea Ice Extent', color='orange')
    plt.axhline(0, color='black', linestyle='--', alpha=0.7)
    plt.title(f"Daily Changes in Sea Ice Extent - {region}")
    plt.xlabel('Day of the Year')
    plt.ylabel('Change in Sea Ice Extent (km²)')
    plt.legend()
    plt.grid()
    plt.savefig(f"visualizations/{region}_sea_ice_extent_diff.png")
    plt.show()
