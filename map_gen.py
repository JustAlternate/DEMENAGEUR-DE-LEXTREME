#Map generation.py
from msilib.schema import MsiPatchHeaders
from re import M
from math import sqrt
import random
from class_graphe import *

def starting_map():
    Map_graph = Graphe("map")

    Map_graph.ajouterSommet(Sommet(0,[0,0]))
    s=Map_graph.sommets[0]
    Map_graph.ajouterSommet(Sommet(s.nom+1,[s.pos[0],s.pos[1]+50]))
    Map_graph.ajouterArc(Arc(s,Map_graph.sommets[-1]))
    Map_graph.ajouterSommet(Sommet(s.nom+2,[s.pos[0],s.pos[1]-50]))
    Map_graph.ajouterArc(Arc(s,Map_graph.sommets[-1]))
    Map_graph.ajouterSommet(Sommet(s.nom+3,[s.pos[0]-50,s.pos[1]]))
    Map_graph.ajouterArc(Arc(s,Map_graph.sommets[-1]))
    Map_graph.ajouterSommet(Sommet(s.nom+4,[s.pos[0]+50,s.pos[1]]))
    Map_graph.ajouterArc(Arc(s,Map_graph.sommets[-1]))

    return Map_graph

def gen_neighboor(Map_graph,s):

    Voisins=[]
    for arc in Map_graph.arcs:
        if arc.s_origine==s:
            Voisins.append(arc.s_extremite)
        elif arc.s_extremite==s:
            Voisins.append(arc.s_origine)
    
    print(Voisins)

    def s_coord_existe_in_voisins(s,voisins):
        for voisin in voisins:
            if voisin.pos[0]==s.pos[0] and voisin.pos[1]==s.pos[1]:return True
        return False

    Sommets_to_add=[
        Sommet(s.nom+1,[s.pos[0],s.pos[1]+50]),
        Sommet(s.nom+2,[s.pos[0],s.pos[1]-50]),
        Sommet(s.nom+3,[s.pos[0]-50,s.pos[1]]),
        Sommet(s.nom+4,[s.pos[0]+50,s.pos[1]])]

    for sommet in Sommets_to_add:
        if not (s_coord_existe_in_voisins(sommet,Voisins)):
            Map_graph.ajouterSommet(sommet)
            for sommetglob in Map_graph.sommets:
                if sqrt((sommetglob.pos[1]-sommet.pos[1])**2+(sommetglob.pos[0]-sommet.pos[0])**2)==50:
                    Map_graph.ajouterArc(Arc(sommet,sommetglob))