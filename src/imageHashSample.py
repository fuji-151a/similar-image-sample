from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('/mnt/c/Users/fuji_/git/similar-image-sample/image/ms4_1.png'))
print(hash)
otherhash = imagehash.average_hash(Image.open('/mnt/c/Users/fuji_/git/similar-image-sample/image/ms4_5.jpg'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)