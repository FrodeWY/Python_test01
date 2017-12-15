import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw


def thumbnail():
    im = Image.open("../resource/3.jpg")
    # im.size返回一个元组，分别是宽和高
    w, h = im.size
    print('origin size w:%s,h:%s' % (w, h))
    # thumbnail函数接受一个元组作为参数，分别对应着缩略图的宽高，
    # 在缩略时，函数会保持图片的宽高比例。如果输入的参数宽高和原图像宽高比不同，则会依据最小对应边进行原比例缩放。
    im.thumbnail((w // 2, h // 2))
    print('resize image size w:%s,h:%s' % (w // 2, h // 2))
    im.save('../resource/thumbnail.png')


# 图像滤波在ImageFilter 模块中，在该模块中，预先定义了很多增强滤波器，可以通过filter( )函数使用，预定义滤波器包括：
#  mageFilter.BLUR为模糊滤波，处理之后的图像会整体变得模糊。
# ImageFilter.CONTOUR为轮廓滤波，将图像中的轮廓信息全部提取出来。
# ImageFilter.DETAIL为细节增强滤波，会使得图像中细节更加明显。
# ImageFilter.EDGE_ENHANCE为边缘增强滤波，突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法。经处理使得边界和边缘在图像上表现为图像灰度的突变,用以提高人眼识别能力。
# ImageFilter.EMBOSS为浮雕滤波，会使图像呈现出浮雕效果。
def filter():
    im = Image.open("../resource/cat.jpg")
    print('filter')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('../resource/filter.jpg', 'jpeg')


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def new_image():
    width = 60 * 4
    height = 60
    # 创建图片
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建trueType字体
    font = ImageFont.truetype('../resource/Arial.ttf', size=36, encoding='utf-8')
    # 创建一个可用来对image进行操作的对象
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    for x in range(5):
        draw.line((0, x * 15, 240, x * 15), fill=rndColor(), width=10)
    for x in range(4):
        draw.text((60 * x + 10, 10), rndChar(), fill=rndColor2(), font=font)
    # ImageFilter模块提供了滤波器相关定义；这些滤波器主要用于Image类的filter()方法
    image = image.filter(ImageFilter.BLUR)
    image.save('../resource/verification_code.jpg')


if __name__ == '__main__':
    # thumbnail()
    # filter()
    new_image()
