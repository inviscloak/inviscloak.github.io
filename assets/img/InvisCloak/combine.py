from PIL import Image
import os

def merge_images(folder_path, output_path, rows=4, cols=8, spacing=10):
    for map_name in os.listdir(folder_path):
        map_path = os.path.join(folder_path, map_name)
        if os.path.isdir(map_path):
            images = [Image.open(os.path.join(map_path, img)) for img in os.listdir(map_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
            if len(images) != rows * cols:
                print(f"Skipping {map_name}, as it does not contain exactly {rows*cols} images.")
                continue

            widths, heights = zip(*(i.size for i in images))
            total_width = sum(widths[0:cols]) + spacing * (cols - 1)
            max_height = max(heights) * rows + spacing * (rows - 1)
            
            new_im = Image.new('RGB', (total_width, max_height), (255, 255, 255))
            
            x_offset, y_offset = 0, 0
            for i, im in enumerate(images):
                if i % cols == 0 and i != 0:
                    x_offset = 0
                    y_offset += max(heights) + spacing
                new_im.paste(im, (x_offset, y_offset))
                x_offset += im.size[0] + spacing
                
                if (i + 1) % cols == 0:
                    y_offset += max(heights) - im.size[1]
            output_file = os.path.join(output_path, f"{map_name}.jpg")
            new_im.save(output_file)
            print(f"Image saved to {output_file}")

source_folder = "cs2"
output_folder = "cs2_combine"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

merge_images(source_folder, output_folder)
