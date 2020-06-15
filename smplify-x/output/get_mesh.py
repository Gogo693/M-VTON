import os
from openmesh import *
import trimesh
import renderer as rd


my_renderer = rd.SMPLRenderer()

mesh = trimesh.load("./meshes/000001_0/000.obj")

proj_sil = my_renderer.silhouette(verts = mesh.points())

print(type(proj_sil))