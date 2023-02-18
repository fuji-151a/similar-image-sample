# Image Hashを用いた類似画像検出
# image以下のms4_1.pngをベースにそれ以外の画像との類似度を順番に出している
import glob

from PIL import Image
import imagehash

uploaded_file_names = sorted(glob.glob('image/*.???'))
print(uploaded_file_names)
base_image_hash = imagehash.average_hash(Image.open(uploaded_file_names.pop(0)))
title = ["似ている画像", "図形の順番を変えた画像", "図形の順番を変えた画像2", "使っている色が同じ画像", "全く別の画像"]
print('==========似ていない画像の類似度===========')
other_image_hash_list = list(map(lambda x: base_image_hash-x, map(imagehash.average_hash, map(Image.open,uploaded_file_names))))
for i,x in enumerate(other_image_hash_list):
  print(title[i] + ":" + str(x))
