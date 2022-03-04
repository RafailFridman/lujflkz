import os
from PIL import Image
import torchvision.transforms as T
import shutil, os

base_dir = 'wild'


def get_all_dirs(dir):
    return [os.path.join(dir, d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]


def get_all_edit_prompts(dir):
    return [f for f in os.listdir(dir) if os.path.isdir(os.path.join(dir, f)) and not f.endswith('.DS_Store')]


def get_image_path(dir):
    image_path = [os.path.join(dir, f) for f in os.listdir(dir) if
                  f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
    assert len(image_path) == 1
    return image_path[0]

for i in range(82):
    shutil.copy(f'imou_highres/{i}.jpg', f'imou/{i}.jpg')
    shutil.copy(f'imsty_highres/{i}.jpg', f'imsty/{i}.jpg')
    shutil.copy(f'src_imgs_highres/{i}.jpg', f'src_imgs/{i}.jpg')
    shutil.copy(f'imvq_highres/{i}.jpg', f'imvq/{i}.jpg')

# i = 0
# image_dirs = get_all_dirs(base_dir)
# command = ''
# for image_dir in image_dirs:
#     src_image_path = get_image_path(image_dir)
#     # img = Image.open(src_image_path)
#     # w, h = img.size
#     # if min(w, h) > 512:
#     #     img = T.Resize(512)(img)
#     #     w, h = img.size
#     for edit_prompt in get_all_edit_prompts(image_dir):
#         shutil.copy(src_image_path, os.path.join('src_imgs', f'{i}.jpg'))
#         command += edit_prompt + '\n'
#         # dir = os.path.join(image_dir, edit_prompt)
#         # ours = [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and os.path.join(dir, f).endswith('png') and 'vqgan' not in f and 'styler' not in f][0]
#         # print(dir)
#         # exit()
#         # os.rename(ours, os.path.join(dir, f'ours.png'))
#         # print(files)
#         # exit()
#         # print(dir)
#         # exit()
#         # vqgan = os.path.join(dir, 'vqgan.png')
#         # styler = os.path.join(dir, 'styler.png')
#         # ours = os.path.join(dir, 'ours.png')
#         # shutil.copy(vqgan, os.path.join('imvq', f'{i}.jpg'))
#         # shutil.copy(styler, os.path.join('imsty', f'{i}.jpg'))
#         # shutil.copy(ours, os.path.join('imou', f'{i}.jpg'))
#         # os.rename(vqgan, os.path.join('imvq', f'{i}.jpg'))
#         # os.rename(styler, os.path.join('imsty', f'{i}.jpg'))
#         # os.rename(ours, os.path.join('imou', f'{i}.jpg'))
#         i += 1
#         # save_name = "_".join(edit_prompt.split())
#         # output_path = os.path.join(image_dir, edit_prompt, 'vqgan.png')
#         # os.rename(output_path, os.path.join(image_dir, edit_prompt, 'styler.png'))
# print(i+1)
# # with open('captions_imgs.txt', 'w') as f:
# #     f.write(command)