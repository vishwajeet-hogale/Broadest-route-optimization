from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
import random
import main.simulation.matrix as m
import json


app=Flask(__name__)

# Mysql Connection
# app.config['MYSQL_HOST'] = 'localhost' 
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Mysteriousman307'
# app.config['MYSQL_DB'] = 'ambulance'
# mysql = MySQL(app)

app.secret_key = "mysecretkey"
oadd = None
dadd = None
@app.route('/')
def home():
    
        global oadd
        global dadd
        
       
        flash('Thank you! Your ambulance will arrive soon')
       
        oadd = "Vega City" + ',' + "Bangalore"

        dadd = "Brigade Tech Gardens" + ',' + "Bangalore"
        points = m.get_latlong(oadd,dadd)
        j = m.getpoints(points[0][0],points[0][1],points[1][0],points[1][1])   # Replace this with node ordering. 
        origin=[points[0][0],points[0][1]]
        dest=[points[1][0],points[1][1]]
        print(j[0]['numofpoints'])
        lat = []
        lon=[]
        lat=j[0]['latpoints']
        lon=j[0]['longpoints']        
        return render_template('map.html',lat=lat,long=lon,origin=origin,dest=dest)
# @app.route('/getdata',methods=['POST','GET'])
# def formfill():
    
      
# @app.route('/ouranalysis')
# def getanalysis():
#     global oadd
#     global dadd
#     print(oadd)
#     cur=mysql.connection.cursor()
#     cur.execute("SELECT * FROM trafficsignals")
#     data = cur.fetchall()
#     l=[]
#     cur.close()
    

#     for i in range(0,len(data)):
#         b=m.get_reverse_geo(data[i][1],data[i][2])
#         b = b.split(',')
#         b = b[0:5]
#         l.append(','.join(b))
    
#     return render_template('analysis.html',signals = data,l=l,length=len(l),origin=oadd,dest=dadd)
        
if __name__ == '__main__':
    app.run(debug=True,port=5000)