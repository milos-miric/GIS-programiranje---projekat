from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

t1 = Point(7339824.567626324, 5084260.358846478) # Zoo vrt Kolut
t2 = Point(7403997.547890707, 5106957.233350199) # Zoo vrt Palic
t3 = Point(7457272.620357253, 4964639.579988737) # Zoo vrt Beograd
t4 = Point(7521752.537408494, 4868995.806786649) # Zoo vrt Jagodina

lista = [(t1, 'Zoo vrt Kolut'), (t2, 'Zoo vrt Palic'), (t3, 'Zoo vrt Beograd'), (t4, 'Zoo vrt Jagodina')]

# Kreiranje GeoDataFrame-e
df = gpd.GeoDataFrame()
df['geometry'] = None

for id, (lokacija, naziv) in enumerate(lista):
    df.loc[id, 'geometry'] = lokacija
    df.loc[id, 'Ime lokacije'] = naziv

df.crs = from_epsg(6316)
df.plot(facecolor='green')
plt.title("Zoo vrtovi")
plt.show()

out_file = r'D:\GIS programiranje\Projekat_ZooTour\Projekat_ZooTour\Lokacija_Zoo_vrtova.shp'
df.to_file(out_file)

fp = "D:\GIS programiranje\Projekat_ZooTour\Projekat_ZooTour\Opstine SRB.shp"

df_loc = gpd.read_file(fp)
print(df_loc)
print(df_loc.crs)
print(df_loc['geometry'].head())

df_loc = df_loc.rename(columns={'Opstina': 'Naziv opstine'})
print(df_loc.columns)
print(df_loc)

df_loc['Povrsina'] = df_loc['geometry'].area / 1000000
print(df_loc['Povrsina'].head())

df_loc.crs = from_epsg(6316)
print(df_loc.crs)

df_loc.plot(column='Naziv opstine', cmap='tab10', legend=False)
plt.title('Opstine Srbije')
plt.tight_layout()
plt.show()

out_file2 = "D:\GIS programiranje\Projekat_ZooTour\Opstine Srbije"

print(df.crs)

# Preklapanje
df.to_crs(df_loc.crs, inplace=True)
preklapanje = df.geometry._append(df_loc.geometry)
print(preklapanje.crs)
print(preklapanje)

preklapanje.plot(cmap="Pastel1")
plt.title("Zooloski vrtovi na teritoriji Srbije")
plt.show()

print(plt.show)



















