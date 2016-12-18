#-*- coding:utf-8 -*-
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance, ImageFont, ImageMath
import os

path = os.path.dirname(__file__)

image1 = Image.open(path+'/../image/Koala.jpg')
image2 = Image.open(path+'/../image/Lighthouse.jpg')

#图片保存
def image_save(image, name):
    image.save(name)

#图片大小
def image_size(image):
    w, h = image.size
    return w, h

print(image_size(image1))
#图片裁剪
def image_crop(image, p1, p2, p3, p4):
    box = (p1, p2, p3, p4)
    image = image.crop(box)
    image.show()
    return image

#图片压缩
def image_thumbnail(image, s1, s2):
    image.thumbnail((s1, s2), Image.ANTIALIAS)
    image.show()
    return image

#image = image_thumbnail(image1, 400, 500)
#image_save(image, 'thumbnail.jpg')
#图片旋转
def image_rotate(image, rotate):
    image = image.rotate(rotate)
    image.show()
    return image

#图片黑白转换
def image_convert(image):
    image = image.convert('L')
    image.show()
    return image

#图片过滤
def image_filter(image):
    image = image.filter(ImageFilter.DETAIL)
    image.show()
    return image

#图片写字
def image_draw(image, p1, p2, text, font):
    draw = ImageDraw.Draw(image)
    draw.text((p1, p2), text, font=font)
    image.show()
    return image

# w, h = image_size(image2)
# font = ImageFont.truetype(path +'/../fonts/simsun.ttc', 24)
# image = image_draw(image2, w - 150, 30, u'你好', font)
# image_save(image, 'draw.jpg')

#图片拼接
def image_resize(image1, image2):
    images = (image1, image2)
    w1, h1 = image1.size
    w2, h2 = image2.size
    h = h1 if h1 > h2 else h2
    target = Image.new('RGB',(w1+w2, h))
    left = 0
    right = w1
    for image in images:
        temp = image.resize((w1, h1), Image.ANTIALIAS)
        target.paste(temp, (left, 0, right, h))
        left += w2
        right += w2
    target.show()
    return target

# image = image_resize(image1, image2)
# image_save(image, 'resize_image.jpg')

#图片虚化
def image_convert_p(image):
    image = image.convert('P')
    image.show()
    return image

# image = image_convert_p(image1)
# image_save(image, 'p.jpg')

#图片怀旧转换
def image_convert_LA(image):
    image = image.convert('LA')
    image.show()
    return image

# image = image_convert_LA(image1)
# image_save(image, 'la.jpg')

#图片锐化
def image_sharp(image, degree):
    enhancer = ImageEnhance.Sharpness(image)
    enhancer.enhance(degree).show()
    return enhancer

# image = image_sharp(image1, 50)
# image_save(image, 'sharp.jpg')

#图片色彩增强
def image_color(image, degree):
    enhancer = ImageEnhance.Color(image)
    enhancer.enhance(degree).show()
    return enhancer

#图片亮度增强
def image_bright(image, degree):
    enhancer = ImageEnhance.Brightness(image)
    enhancer.enhance(degree).show()
    return enhancer

#图片曝光
def image_blur(image):
    image = image.filter(ImageFilter.BLUR)
    image.show()
    return image

#图片最小化过滤
def image_min_filter(image):
    image = image.filter(ImageFilter.MaxFilter)
    image.show()
    return image

#图片转换黑白线条
def image_filter_bw(image):
    image = image.filter(ImageFilter.CONTOUR)
    image.show()
    return image

# image = image_filter_bw(image1)
# image_save(image, 'bw.jpg')
#图片浮雕
def image_emboss(image):
    image = image.filter(ImageFilter.EMBOSS)
    image.show()
    return image

#图片
def image_edges(image):
    image = image.filter(ImageFilter.FIND_EDGES)
    image.show()
    return image
# image = image_edges(image1)
# image_save(image, 'edges.jpg')

#图片旋转
def image_rotate(image, theta):
    image = image.rotate(theta)
    image.show()
    return image

#图片翻转
def image_transpose(image):
    image = image.transpose(Image.ROTATE_90)
    image.show()
# image_transpose(image1)