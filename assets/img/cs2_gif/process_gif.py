import imageio

def cut_and_join_gif(input_gif_path, output_gif_path, start_frame, end_frame):
    reader = imageio.get_reader(input_gif_path)
    frames = [frame for frame in reader]

    fps = reader.get_meta_data().get('fps', 9)
    
    new_frames = frames[:start_frame] + frames[end_frame:]
    
    writer = imageio.get_writer(output_gif_path, fps=fps)
    for frame in new_frames:
        writer.append_data(frame)
    writer.close()

input_gif_path = 'half_new.gif'
output_gif_path = 'half_new_1.gif'
start_frame = 56
end_frame = 85

cut_and_join_gif(input_gif_path, output_gif_path, start_frame, end_frame)
