from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
import random
import main.simulation.matrix as m
import json


app=Flask(__name__)



app.secret_key = "mysecretkey"

@app.route('/')
def home():
        flash('Thank you! Your ambulance will arrive soon')
        st = 3
        end = 44
        pst = location_info[st]
        pend = location_info[end] 
        path_list = m.get_route_for_map(graph,n,st,end)
        print(path_list)
        support_points = m.get_support_points(path_list,location_info)
        print(support_points)
        j = m.get_points_using_supporting_points(support_points,pst,pend)   # Replace this with node ordering. 
        origin=pst
        dest=pend
        print(j[0]['numofpoints'])
        lat = []
        lon=[]
        lat=j[0]['latpoints']
        lon=j[0]['longpoints']        
        return render_template('map.html',lat=lat,long=lon,origin=origin,dest=dest)

if __name__ == '__main__':
    graph,location_info,n = m.load_data()
    print(location_info)
    app.run(debug=True,port=5000)