import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# 加载地图图片
def load_map_image(image_path):
    return mpimg.imread(image_path)

# 定义颜色映射：70dB -> 深红色，49dB -> 浅红色
def db_to_color(db):
    # 将分贝值线性映射到 0-1 的范围
    min_db, max_db = 49, 80
    normalized_value = (db - min_db) / (max_db - min_db)
    normalized_value = np.clip(normalized_value, 0, 1)  # 确保值在 [0, 1] 范围内
    # RGB 颜色：深红色 (0.5, 0, 0) 对应 70 dB，浅红色 (1, 0.7, 0.7) 对应 49 dB
    r = 1 - 0.5 * normalized_value
    g = 0.7 - 0.7 * normalized_value
    b = 0.7 - 0.7 * normalized_value
    return (r, g, b)

# 绘制地图并标注点
def plot_sound_map(image_path, points):
    # 加载地图图片
    map_image = load_map_image(image_path)
    height, width = map_image.shape[:2]  # 获取地图的高度和宽度

    # 创建绘图
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(map_image, extent=[0, width, 0, height])  # 显示地图图片

    for point in points:
        x, y, db = point  # 获取点的坐标和分贝值
        color = db_to_color(db)  # 根据分贝值计算颜色
        ax.scatter(x, y, color=color, s=100, edgecolor='black')  # 在地图上绘制点

    # 添加颜色条
    norm = Normalize(vmin=49, vmax=80)  # 定义归一化范围
    sm = ScalarMappable(cmap='Reds_r', norm=norm)  # 使用 'Reds_r'（反转的红色渐变）
    sm.set_array([])  # 必须调用 set_array，即使为空
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', label="Sound Level (dB)")
    cbar.set_label("Sound Level (dB)", fontsize=12)

    # 设置图形属性
    ax.set_title("Average Sound Pressure Level Map", fontsize=14)
    ax.set_xlabel("X Coordinate", fontsize=10)
    ax.set_ylabel("Y Coordinate", fontsize=10)

    plt.show()

# 示例输入：观测点坐标和分贝值
points = [
    (460, 319, 58.2),  # (x, y, dB)
    (346, 367, 59),
    (405, 466, 62.8),
    (521, 420, 63.9),
    (619, 390, 63.4),
    (672, 278, 51.5),
    (803, 241, 49.8),
    (812, 411, 57.5),
    (1020, 283, 59.9),
    (1192, 402, 52.3),
    (937, 342, 62.5),
    (785, 82, 61),
    (352, 545, 67.7),
    (140, 566, 69.9),
    (969, 503, 55.8)
]

# 地图图片路径
image_path = "map.png"

# 绘制声音地图
plot_sound_map(image_path, points)