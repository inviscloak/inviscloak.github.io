import imageio

def cut_and_join_gif(input_gif_path, output_gif_path, start_frame, end_frame):
    reader = imageio.get_reader(input_gif_path)
    frames = [frame for frame in reader]

    fps = reader.get_meta_data().get('fps', 18)
    
    new_frames = frames[:start_frame] + frames[end_frame:]
    
    writer = imageio.get_writer(output_gif_path, fps=fps)
    for frame in new_frames:
        writer.append_data(frame)
    writer.close()

input_gif_path = 'smoke.gif'
output_gif_path = 'smoke_1.gif'
start_frame = 42
end_frame = 160

cut_and_join_gif(input_gif_path, output_gif_path, start_frame, end_frame)
