import os
import sounddevice as sd
from scipy.io.wavfile import write
import time

# 配置参数
output_folder = "5106/recordings"  # 保存录音文件的文件夹
sample_rate = 44100          # 录音采样率 (Hz)
duration = 1 * 60           # 每次录音时长 (秒)
interval = 14 * 60           # 每次录音之间的间隔 (秒)

# 创建保存文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 初始化计数器
counter = 1

print("开始录音程序...")

try:
    while True:
        # 生成文件名
        file_name = os.path.join(output_folder, f"recording_{counter:04d}.wav")
        
        print(f"正在录制 {file_name} ...")
        
        # 录制音频
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
        sd.wait()  # 等待录音完成
        
        # 保存为 WAV 文件
        write(file_name, sample_rate, recording)
        print(f"已保存 {file_name}")
        
        # 更新计数器
        counter += 1
        
        # 等待下一次录音
        print(f"等待 {interval // 60} 分钟后开始下一次录音...")
        time.sleep(interval)

except KeyboardInterrupt:
    print("录音程序已停止。")