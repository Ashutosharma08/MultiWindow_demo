import open3d as o3d
import keyboard
pcd = o3d.io.read_point_cloud('TSY 2/TSY_AC_AA/TreeFiles/1.ply')
pcd.paint_uniform_color([1,0,0])
pcd1 = o3d.io.read_point_cloud('Normal1.ply')
pcd1.paint_uniform_color([0,0,1])

vis1 = o3d.visualization.Visualizer()
vis1.create_window(height=500,width=800)
vis1.add_geometry(pcd)

ctrl1 = vis1.get_view_control()
ctrl1.rotate(0,-500)
vis1.poll_events()
vis1.update_renderer()
# vis1.destroy_window()

vis2 = o3d.visualization.Visualizer()
vis2.create_window(height=500,width=800,left=1000)
vis2.add_geometry(pcd1)
ctrl2 = vis2.get_view_control()
ctrl2.rotate(0,-500)
vis2.poll_events()
vis2.update_renderer()
# vis2.destroy_window()
for i in range(500000):

    # vis1.add_geometry(pcd)
    # vis1.run()
    ctrl1.rotate(10,0)
    vis1.poll_events()
    vis1.update_renderer()

    ctrl2.rotate(10, 0)
    vis2.poll_events()
    vis2.update_renderer()
    if keyboard.is_pressed('q'):
        vis1.destroy_window()
        vis2.destroy_window()
# vis1.destroy_window()

    # for i in range(500000):
    #     vis2.add_geometry(pcd1)
    #     vis2.run()
        # ctrl2.rotate(10,0)
        # vis2.poll_events()
        # vis2.update_renderer()
        # if keyboard.is_pressed('q'):
        #     vis1.destroy_window()
        #     vis2.destroy_window()

# vis2.destroy_window()