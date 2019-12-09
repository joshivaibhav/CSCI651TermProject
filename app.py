from flask import Flask, request
from flask import render_template
from flask_mysqldb import MySQL
from flask import jsonify,make_response
import pandas as pd
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xxxxxxxx'
app.config['MYSQL_DB'] = 'ATNT'

mysql = MySQL(app)


@app.route('/',methods=['GET','POST'])
def index1():
    if request.method == "POST":
        city_map = {'NewYork':'NY54',
            'Chicago':'CHCG',
            'Cambridge':'CMBR',
            'Cleveland':'CLEV',
            'Raleigh':'RLGH',
            'Philadelphia':'PHLA',
            'Nashville':'NSVL',
            'St.Louis':'STLS',
            'NewOrleans':'NWOR',
            'Houston':'HSTN',
            'SanAntonio':'SNAN',
            'Dallas':'DLLS',
            'Orlando':'ORLD',
            'Denver':'DNVR',
            'KansasCity':'KSCY',
            'SanFrancisco':'SNFN',
            'Sacramento':'SCRM',
            'Seattle':'STTL',
            'SaltLakeCity':'SLKC',
            'LosAngeles':'LA03',
            'SanDiego':'SNDG',
            'Phoenix':'PHNX',
            'Atlanta':'ATLN',
            'Washington':'WASH',
            'Portland':'PTLD'
            }

        outputMap = {'NY54':'NewYork',
                    'CHCG':'Chicago',
                    'CMBR':'Cambridge',
                    'CLEV':'Cleveland',
                    'RLGH':'Raleigh',
                    'PHLA':'Philadelphia',
                    'NSVL':'Nashville',
                    'STLS':'St.Louis',
                    'NWOR':'NewOrleans',
                    'HSTN':'Houston',
                    'SNAN':'SanAntonio',
                    'DLLS':'Dallas',
                    'ORLD':'Orlando',
                    'DNVR':'Denver',
                    'KSCY':'KansasCity',
                    'SNFN':'SanFrancisco',
                    'SCRM':'Sacramento',
                    'STTL':'Seattle',
                    'SLKC':'SaltLakeCity',
                    'LA03':'LosAngeles',
                    'SNDG':'SanDiego',
                    'PHNX':'Phoenix',
                    'ATLN':'Atlanta',
                    'WASH':'Washington',
                    'PTLD':'Portland'}

        details = request.get_json()
        firstName = details['data']
        firstName = firstName.split(" ")
        cur = mysql.connection.cursor()
        print(firstName)
        if firstName[0] == "Where":
            if firstName[3] == "from":
                label = firstName[4]
                order = firstName[8]
                print(order)
                if order == "1":
                    #/retrive
                    print("in order")
                    cur.execute("SELECT nodes__label FROM ATNT_cleaned WHERE nodes__id IN (SELECT edges__target FROM ATNT_cleaned WHERE edges__source = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}'));".format(city_map[label]))
                    data = cur.fetchall()
                    data = list(data)
                    outputData = []
                    string = "Traffic from " + str(outputMap[city_map[label]]) + " is going to "
                    for x in range(len(data)):
                        data[x] = ''.join(data[x])
                        outputData.append(outputMap[data[x]])

                    for x in range(len(data)):
                        string = string + outputData[x] + ", "

                    return render_template('sample.html',data=string) # render_template('Qery2.html',data=x)
                elif order == "2":
                    #/retrieve2
                    print("in order 2")
                    cur.execute("SELECT nodes__label FROM ATNT_cleaned WHERE nodes__id IN (SELECT edges__target FROM ATNT_cleaned WHERE edges__source IN (SELECT edges__target FROM ATNT_cleaned WHERE edges__source = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}')));".format(city_map[label]))
                    data = cur.fetchall()
                    data = list(data)
                    outputData = []
                    string = "Traffic from targets of " + str(outputMap[city_map[label]]) + " is going to "
                    for x in range(len(data)):
                        data[x] = ''.join(data[x])
                        outputData.append(outputMap[data[x]])

                    for x in range(len(data)):
                        string = string + outputData[x] + ", "
                    return render_template('sample.html',data=string)
            if firstName[3] == "to":
                label = firstName[4]
                order = firstName[8]
                if order == "1":
                    #/retrieve4
                    cur.execute("SELECT nodes__label FROM ATNT_cleaned WHERE nodes__id IN (SELECT edges__source FROM ATNT_cleaned WHERE edges__target = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}'));".format(city_map[label]))
                    data = cur.fetchall()
                    data = list(data)
                    outputData = []
                    string = "Traffic to " + str(outputMap[city_map[label]]) + " is coming from "
                    for x in range(len(data)):
                        data[x] = ''.join(data[x])
                        outputData.append(outputMap[data[x]])

                    for x in range(len(data)):
                        string = string + outputData[x] + ", "
                    return render_template('sample.html',data=string)
                elif order == "2":
                    #/retrieve5
                    cur.execute("SELECT nodes__label FROM ATNT_cleaned WHERE nodes__id IN (SELECT DISTINCT(edges__source) FROM ATNT_cleaned WHERE edges__target IN (SELECT edges__source FROM ATNT_cleaned WHERE edges__target = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}')));".format(city_map[label]))
                    data = cur.fetchall()
                    data = list(data)
                    outputData = []
                    string = "Traffic to sources of " + str(outputMap[city_map[label]]) + " is coming from "
                    for x in range(len(data)):
                        data[x] = ''.join(data[x])
                        outputData.append(outputMap[data[x]])

                    for x in range(len(data)):
                        string = string + outputData[x] + ", "
                    return render_template('sample.html',data=string)
        elif firstName[0] == "How":
            if firstName[2] == "Egresses":
                label = firstName[4]
                #/retrieve3
                cur.execute("SELECT COUNT(edges__target) FROM ATNT_cleaned WHERE edges__source = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}');".format(city_map[label]))
                data = cur.fetchall()
                data = list(data)
                outputData = []
                string = str(outputMap[city_map[label]]) + " has "
                for x in range(len(data)):
                    data[x] = ''.join(str(data[x]))
                    # outputData.append(outputMap[data[x]])
                data = data[0]
                data = data[1:]    
                data = data[:-2]
                string = string + data + " Egresses."
                return render_template('sample.html',data=string)
            elif firstName[2] == "Ingresses":
                label = firstName[4]
                #/retrieve6
                cur.execute("SELECT COUNT(edges__source) FROM ATNT_cleaned WHERE edges__target = (Select nodes__id FROM ATNT_cleaned WHERE nodes__label = '{0}');".format(city_map[label]))
                data = cur.fetchall()
                data = list(data)
                outputData = []
                string = str(outputMap[city_map[label]]) + " has "
                for x in range(len(data)):
                    data[x] = ''.join(str(data[x]))  
                data = data[0]
                data = data[1:]    
                data = data[:-2]
                string = string + data + " Ingresses."
                return render_template('sample.html',data=string)
    return render_template('Qery2.html',title='Home')



if __name__ == '__main__':
    app.run()


