from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('/mnt/c/Users/fuji_/git/similar-image/image/ms4_1.png'))
print(hash)
otherhash = imagehash.average_hash(Image.open('/mnt/c/Users/fuji_/git/similar-image/image/ms4_4.png'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)