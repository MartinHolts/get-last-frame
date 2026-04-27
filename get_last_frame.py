import cv2
import sys
import os

# Get the directory where the .exe is sitting
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

# List of video types to look for
video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv')
processed_count = 0

# Loop through all files in the folder
for filename in os.listdir(current_dir):
    if filename.lower().endswith(video_extensions):
        video_path = os.path.join(current_dir, filename)
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            continue
        
        # Get last frame
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames > 0:
            cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
            success, frame = cap.read()
            
            if success:
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(current_dir, f"{base_name}_last_frame.jpg")
                cv2.imwrite(output_path, frame)
                processed_count += 1
                
        cap.release()
