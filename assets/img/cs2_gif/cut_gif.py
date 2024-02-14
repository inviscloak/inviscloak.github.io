import imageio

def extract_gif_frames(input_gif_path, output_gif_path, start_frame, end_frame):
    reader = imageio.get_reader(input_gif_path)
    fps = reader.get_meta_data().get('fps', 16)
    
    writer = imageio.get_writer(output_gif_path, fps=fps)
    
    for i, frame in enumerate(reader):
        if start_frame <= i < end_frame:
            writer.append_data(frame)
    
    writer.close()

input_gif_path = 'backup/smoke.gif'
output_gif_path = 'smoke.gif'
start_frame = 0
end_frame = 135

extract_gif_frames(input_gif_path, output_gif_path, start_frame, end_frame)
