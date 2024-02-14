import imageio

def increase_gif_fps(input_gif_path, output_gif_path, new_fps):
    reader = imageio.get_reader(input_gif_path)
    frames = [frame for frame in reader]
    
    writer = imageio.get_writer(output_gif_path, fps=new_fps)
    for frame in frames:
        writer.append_data(frame)
    writer.close()

input_gif_path = 'run.gif'
output_gif_path = 'run_new.gif'
new_fps = 20

increase_gif_fps(input_gif_path, output_gif_path, new_fps)
