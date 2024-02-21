import osmnx as osm


def get_osm_data():
    road = osm.graph_from_place('Chennai, India', network_type = "drive")
    prj_road = osm.project_graph(road)
    osm.save_graph_shapefile(prj_road, filepath = r"./graphs/Chennai")
    
    
if __name__ == "__main__":
    get_osm_data()
    