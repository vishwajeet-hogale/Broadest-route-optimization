from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, Response
# from flask_mysqldb import MySQL
import random
import main.simulation.matrix as m
import json
import main.simulation.traversal as traversal

app=Flask(__name__)



app.secret_key = "mysecretkey"


@app.route('/')
def home():
        flash('Thank you! Your ambulance will arrive soon')
        st = 42
        end = 3
        pst = location_info[st]
        pend = location_info[end] 
        dist,avg_width,path_list = traversal.findpath('dataset4POC 3.xlsx',st-1,end-1)
        support_points = m.get_support_points(path_list,location_info)
        # print(support_points)
        j = m.get_points_using_supporting_points(support_points,pst,pend)   # Replace this with node ordering. 
        origin=pst
        dest=pend
        # print(j[0]['numofpoints'])
        lat = []
        lon=[]
        lat=j[0]['latpoints']
        lon=j[0]['longpoints']
       
        return render_template('map.html',lat=lat,long=lon,origin=origin,dest=dest)

@app.route("/getNodes",methods=["GET"])
def getNodes():
        return_json = []
        for i in location_info:
                temp = dict()
                temp["nodeName"] = str(i)
                temp["address"] = m.get_reverse_geo(location_info[i][0],location_info[i][1])
                return_json.append(temp)
        return return_json


@app.route('/route')
def route():
        st = int(request.args.get('origin'))
        end = int(request.args.get('destination'))
        pst = location_info[st]
        pend = location_info[end] 
        dist, avg_width, path_list_width_dist, path_list_dist = traversal.findpath('dataset4POC 3.xlsx',st-1,end-1)
        support_points_width_dist = m.get_support_points(path_list_width_dist,location_info)
        support_points_dist = m.get_support_points(path_list_dist,location_info)
        # print(support_points)
        j_wd = m.get_points_using_supporting_points(support_points_width_dist,pst,pend)   # Replace this with node ordering. 
        j_d = m.get_points_using_supporting_points(support_points_dist,pst,pend)   # Replace this with node ordering. 

        origin=pst
        dest=pend

        lat_wd=j_wd[0]['latpoints']
        lon_wd=j_wd[0]['longpoints']

        lat_d=j_d[0]['latpoints']
        lon_d=j_d[0]['longpoints']

        print(lat_wd,lat_d)
        print(lon_wd,lon_d)

        data = {
               'route_dist' : {
                        'latitude':lat_d,
                        'longitude': lon_d,
                        'distance':dist, 
                        'avg_width':avg_width
                },
                'route_width_dist' : {
                        'latitude':lat_wd,
                        'longitude': lon_wd,
                        'distance':dist, 
                        'avg_width':avg_width
                },
                'origin':origin,
                'destination':dest,
        }

        response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
        return response


if __name__ == '__main__':
    graph,location_info,n = m.load_data()
#     print(location_info)
    app.run(debug=True,port=5000)