from PIL import Image
from rembg import remove

mainPic = Image.open('../images/lizard.jpg')
resPic = remove(mainPic)
resPic.save('../images/resPic.png')

