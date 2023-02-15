from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('ms4_1.png'))
print(hash)
otherhash = imagehash.average_hash(Image.open('ms4_5.jpg'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
