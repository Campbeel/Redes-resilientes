import osmnx as ox
import geopandas as gpd

# Define el área geográfica de Santiago
place = "Santiago, Chile"

# Cargar las calles de la zona
G = ox.graph_from_place(place, network_type="drive")

# Obtener las intersecciones como puntos GeoDataFrame
nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)

# Filtrar solo las intersecciones
intersections = nodes[nodes['street_count'] > 2]

# Exportar a GeoJSON
intersections.to_file("infraestructura.geojson", driver="GeoJSON")
