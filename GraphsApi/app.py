from flask import Flask, request, Response
import pickle

from graph import *
from node import *
from link import *

from increment import *


def save_pkl(name, obj):
    f=open(name, 'wb')
    pickle.dump(obj, f)
    f.close()

def load_pkl(name):
    f=open(name, 'rb')
    obj=pickle.load(f)
    f.close()
    return obj

def find_graph(id):
    for i in range(0, len(graphs)):
    	if graphs[i].id == id:
        	return i
    return -1

#️graphs = []
#️nodes = []
#️links = []


graphs=load_pkl('graphs.pkl')
nodes=load_pkl('nodes.pkl')
links=load_pkl('links.pkl')

f = open('last_ids.txt','r')
a = f.readlines()
next_graph_id = Increment(int(a[0]))
next_node_id = Increment(int(a[1]))
next_link_id = Increment(int(a[2]))
f.close()

app = Flask('graph_api')

@app.route('/save')
def save_data():
    save_pkl('graphs.pkl', graphs)
    save_pkl('nodes.pkl', nodes)
    save_pkl('links.pkl', links)
    f = open('last_ids.txt', 'w')
    f.write(f'{next_graph_id.id}\n{next_node_id.id}\n{next_link_id.id}')
    return 'ok'

@app.route('/graph/add')
def add_new_graph():
    name=request.args.get('name')
    graph=Graph(name,next_graph_id)
    graphs.append(graph)
    return Response(response = '{ "id": ' + str(graph.id) + ' }', status = 200,  mimetype='application/json')

@app.route('/graph/remove')
def remove_existing_graph():
    id = int(request.args.get('id'))
    idx = find_graph(id)
    if idx > -1:
        del graphs[idx]
    else:
        return Response(status = 400,  mimetype='application/json')
    return Response(status = 200,  mimetype='application/json')

@app.route('/graph/update')
def update_existing_graph():
    id = int(request.args.get('id'))
    name = str(request.args.get('name'))
    idx = find_graph(id)
    if idx > -1:
        graphs[idx].name = name
    else:
        return Response(status = 400,  mimetype='application/json')
    return Response(status = 200,  mimetype='application/json')

@app.route('/graph/list')
def list_all_graphs():
    s = '[ '
    for graph in graphs:
        s += graph.get_json() + ','
    s = s[:-1] + ' ]'
    return Response(response=s, status=200, mimetype='application/json')


