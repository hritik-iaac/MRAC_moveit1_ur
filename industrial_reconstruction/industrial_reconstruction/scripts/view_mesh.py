import open3d as o3d

if __name__ == "__main__":
    mesh = o3d.io.read_triangle_mesh("/home/hritik/ply_files/path2.ply")
    o3d.visualization.draw_geometries([mesh])