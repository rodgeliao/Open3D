# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/Python/Tutorial/Basic/rgbd_tum.py

from open3d import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Read TUM dataset")
    color_raw = read_image("../../TestData/RGBD/other_formats/TUM_color.png")
    depth_raw = read_image("../../TestData/RGBD/other_formats/TUM_depth.png")
    rgbd_image = create_rgbd_image_from_tum_format(color_raw, depth_raw);
    print(rgbd_image)
    plt.subplot(1, 2, 1)
    plt.title('TUM grayscale image')
    plt.imshow(rgbd_image.color)
    plt.subplot(1, 2, 2)
    plt.title('TUM depth image')
    plt.imshow(rgbd_image.depth)
    plt.show()
    pcd = create_point_cloud_from_rgbd_image(rgbd_image, PinholeCameraIntrinsic(
            PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    draw_geometries([pcd])
