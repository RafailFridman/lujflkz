import os
from PIL import Image
import torchvision.transforms as T

base_dir = 'wild'
# base_cmd = 'bsub -q waic-short -R affinity[thread*2] -R "select[hname!=hgn01]" -R"select[hname!=ibdgxa01]" -gpu num=1:j_exclusive=yes:gmem=30G "module load miniconda/4.7.12; . activate; conda activate /home/labs/waic/narekt/.conda/envs/vqgan;'
base_cmd = 'bsub -q waic-short -R affinity[thread*2] -gpu num=1:j_exclusive=yes:gmem=10G "source /etc/profile.d/modules.sh;module load anaconda/3.7.3; source activate omerpy3.8; '
file = 'styler.sh'

def get_all_dirs(dir):
    return [os.path.join(dir, d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]


def get_all_edit_prompts(dir):
    return [f for f in os.listdir(dir) if os.path.isdir(os.path.join(dir, f)) and not f.endswith('.DS_Store')]


def get_image_path(dir):
    image_path = [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')]
    assert len(image_path) == 1
    return image_path[0]


image_dirs = get_all_dirs(base_dir)
command = ''
for image_dir in image_dirs:
    src_image_path = get_image_path(image_dir)
    img = Image.open(src_image_path)
    w, h = img.size
    if min(w, h) > 512:
        img = T.Resize(512)(img)
        w, h = img.size
    for edit_prompt in get_all_edit_prompts(image_dir):
        save_name = "_".join(edit_prompt.split())
        output_path = os.path.join(image_dir, edit_prompt, 'vqgan.png')
        os.rename(output_path, os.path.join(image_dir, edit_prompt, 'styler.png'))
