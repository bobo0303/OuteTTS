import os  
import subprocess  
  
def convert_m4a_to_wav(source_folder, target_folder):  
    if not os.path.exists(target_folder):  
        os.makedirs(target_folder)  
  
    for filename in os.listdir(source_folder):  
        if filename.endswith(".m4a"):  
            m4a_path = os.path.join(source_folder, filename)  
            wav_path = os.path.join(target_folder, os.path.splitext(filename)[0] + ".wav")  
              
            command = ['ffmpeg', '-i', m4a_path, wav_path]  
            subprocess.run(command, check=True)  
            print(f"已將 {filename} 轉換為 {os.path.basename(wav_path)}")  
  
source_folder = 'pre_audio/'  
target_folder = 'pre_audio/'  
  
convert_m4a_to_wav(source_folder, target_folder) 
  
for filename in os.listdir(source_folder):  
    if filename.startswith("hey_echo (") and filename.endswith(").wav"):  
        # 構建新的檔名  
        new_filename = filename.replace(" (", "_").replace(")", "")  
        # 獲取完整的舊檔案路徑和新檔案路徑  
        old_file = os.path.join(source_folder, filename)  
        new_file = os.path.join(source_folder, new_filename)  
        # 重命名檔案  
        os.rename(old_file, new_file)  