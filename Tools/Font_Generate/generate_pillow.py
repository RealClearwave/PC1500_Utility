#coding: utf-8

from PIL import Image, ImageDraw, ImageFont
from typing import Tuple

class PILFont():
    def __init__(self, font_path: str, font_size: int) -> None:
        self.__font = ImageFont.FreeTypeFont(font_path, font_size)
    
    def render_text(self, text: str, offset: Tuple[int, int] = (0, 0)) -> Image:
        ''' 绘制文本图片
            > text: 待绘制文本
            > offset: 偏移量
        '''
        __left, __top, right, bottom = self.__font.getbbox(text)
        img = Image.new("1", (right, bottom), color=255)
        img_draw = ImageDraw.Draw(img)
        img_draw.text(offset, text, fill=0, font=self.__font, spacing=0)
        return img

f = PILFont("guanzhi.ttf", 8)
# 渲染文本
im = f.render_text("春日影")

width, height = im.size

alphabet = '0123456789ABCDEF'

ans = 'DATA "'
for i in range(width):
    fr = (im.getpixel((i, 1))!=255)+(im.getpixel((i, 2))!=255)*2+(im.getpixel((i, 3))!=255)*4+(im.getpixel((i, 4))!=255)*8
    rr = (im.getpixel((i, 5))!=255)+(im.getpixel((i, 6))!=255)*2+(im.getpixel((i, 7))!=255)*4
    #print(im.getpixel((i, 1))!=255)
    ans += alphabet[int(rr)] + alphabet[int(fr)]
    if (i+1) % 28 == 0: ans += '"\nDATA "'
    elif (i+1) % 7 == 0: ans += '","'

ans += '"'
print("DATA",i//7+1)
print(ans)
#im.save("hope.png")
# 渲染单个文字，可用于生成字体
# im = f.render_text("龙", (0, -1))
# im.show()
