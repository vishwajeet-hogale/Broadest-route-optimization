import json
import urlfetch
from urllib.parse import quote
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from main.simulation.ucs import *

def convert_cooridinates_csv_to_json(df):
    all_coords = [ [float(i.split(",")[0].strip()),float(i.split(",")[1].strip())] for i in df["Coordinates"].to_list()]
    nodes = df["Node"].to_list()
    big_dict = dict()
    for i,j in zip(nodes,all_coords):
        big_dict[i] = j
    return big_dict
def create_adjacency_matrix(df,n):
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for i,row in df.iterrows():
        graph[int(row["source"])][int(row["destination"])] = row["width"]
        # graph[int(row["destination"])][int(row["source"])] = row["width"]
        # print(row["source"])
        
    return graph
 
def load_data():
    excel_file_path = 'dataset4POC 3.xlsx'  # path of the excel file
    df_graph_info = pd.read_excel(excel_file_path,"graph")
    df_coords_info = pd.read_excel(excel_file_path,"coordinates")
    location_info = convert_cooridinates_csv_to_json(df_coords_info)
    total_nodes = len(location_info.keys())
    graph = create_adjacency_matrix(df_graph_info,44)
    # print(graph)
    return graph,location_info,total_nodes

def get_route_for_map(graph,n,st,end):
    path,dis,path_list = ucs(graph,n+1,st,end)
    # print(dis)
    print(path_list)
    return path_list
def get_all_points_for_ucs_route(path_list,location_info):
    n = len(path_list)
    lat = []
    longi = []
    for i in range(0,n-1):
        p1 = location_info[path_list[i]]
        p2 = location_info[path_list[i+1]]
        print(p1)
        print(p2)
        la,lo = getpoints(p1[0],p1[1],p2[0],p2[1])
        lat.extend(la)
        longi.extend(lo)
    return [{'latpoints':lat,'longpoints':longi,'numofpoints':len(lat)}]
def get_drive_time(o_lat,o_long,d_lat,d_long):
    
    url = """https://api.tomtom.com/routing/1/calculateRoute/{},{}:{},{}/json?key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak&routeType=shortest""".format(o_lat,o_long,d_lat,d_long)
    #url = "https://api.tomtom.com/traffic/map/4/tile/flow/{style}/{zoom}/{x}/{y}.{mimeType}?key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak".format(style='absolute',zoom=12,x=1207,y=1539,mimeType='.png')
    #url="https://api.tomtom.com/map/1/wms/?request=GetMap&srs=EPSG%3A4326&bbox=-0.489%2C51.28%2C0.236%2C51.686&width=512&height=512&format=image%2Fjpeg&layers=basic&styles=&service=WMS&version=1.1.1&key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak"
    response = urlfetch.get(url)
    try:
        
        response_json = json.loads(response.content)
        distance = response_json['routes'][0]['summary']['lengthInMeters'] #in meters
        drivetime = response_json['routes'][0]['summary']['travelTimeInSeconds'] 
    except:
        print('ERROR: in get_drive_time')
        return 0

    return [distance/1000,drivetime/60] # [distnace,timeinmins]

# j = get_drive_time(12.9078462, 77.60113103400322, 12.96384535, 77.72024040170766)
# print(j)
def getpoints(o_lat,o_long,d_lat,d_long):
    url = "https://api.tomtom.com/routing/1/calculateRoute/{},{}:{},{}/json?key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak".format(o_lat,o_long,d_lat,d_long)
    response = urlfetch.get(url)
    latitude=[]
    longitude=[]
    try:
        response_json = json.loads(response.content)
        points = response_json['routes'][0]['legs'][0]['points']
        for i in points:
            
            if len(i)==2:
                latitude.append(i['latitude'])
                longitude.append(i['longitude'])
            else:
                print(i)
        # return [{'latpoints':latitude,'longpoints':longitude,'numofpoints':len(latitude)}]
        return latitude,longitude
    except:
        print('Error in getting the points')
            

        
def get_latlong(origin_add, dest_add):
    try:
        geolocator = Nominatim(user_agent = "ram")
        location_origin = geolocator.geocode(origin_add,timeout=100,language="en")
        location_dest = geolocator.geocode(dest_add,timeout=100,language="en")
        return [[location_origin.latitude, location_origin.longitude], [location_dest.latitude, location_dest.longitude]]
    except Exception as e:
        print("Error in lat long function:", str(e))

def get_reverse_geo(lat,lon):
    url="https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={}&lon={}".format(lat,lon)
    response = urlfetch.get(url)
    
    try:
        r_json = json.loads(response.content)
        roadname = r_json['display_name']
        
        return roadname
    except:
        print("Error in reverse geo code")

if __name__ == "__main__":
    df_coords_info = pd.read_excel('dataset4POC 3.xlsx',"coordinates")
    location_info = convert_cooridinates_csv_to_json(df_coords_info)
    total_nodes = len(location_info.keys())
    print(total_nodes)