import trimesh
import pyrender
import imageio
import numpy as np

mesh = trimesh.load("output/2/mesh.glb")  # 또는 경로 지정
scene = pyrender.Scene()
mesh_node = scene.add(pyrender.Mesh.from_trimesh(mesh))

camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
camera_pose = np.eye(4)
camera_node = scene.add(camera, pose=camera_pose)

r = pyrender.OffscreenRenderer(viewport_width=512, viewport_height=512)
frames = []

for angle in np.linspace(0, 2 * np.pi, 36):
    rotation = trimesh.transformations.rotation_matrix(angle, [0, 1, 0])
    camera_pose[:3, :3] = rotation[:3, :3]
    scene.set_pose(camera_node, pose=camera_pose)
    color, _ = r.render(scene)
    frames.append(color)

imageio.mimsave("./mesh_preview.gif", frames, fps=10)