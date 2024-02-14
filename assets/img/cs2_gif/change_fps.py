import imageio

def increase_gif_fps(input_gif_path, output_gif_path, new_fps):
    reader = imageio.get_reader(input_gif_path)
    frames = [frame for frame in reader]
    
    writer = imageio.get_writer(output_gif_path, fps=new_fps)
    for frame in frames:
        writer.append_data(frame)
    writer.close()

input_gif_path = 'half_new.gif'
output_gif_path = 'half_new_1.gif'
new_fps = 11

increase_gif_fps(input_gif_path, output_gif_path, new_fps)
