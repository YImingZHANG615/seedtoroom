from PIL import Image, ImageDraw, ImageFont
import os

# 创建一个1200x630像素的画布
width, height = 1200, 630
image = Image.new('RGB', (width, height), color='#2C3E50')  # 深蓝灰色背景

# 加载字体
font_path = os.path.join(os.getenv('WINDIR'), 'Fonts', 'msyh.ttc')  # 微软雅黑
title_font = ImageFont.truetype(font_path, 80)
subtitle_font = ImageFont.truetype(font_path, 50)

# 创建绘图对象
draw = ImageDraw.Draw(image)

# 绘制标题
title = "医院智能规划系统"
subtitle = "种子到房间配置表"

# 计算文字居中位置
title_bbox = draw.textbbox((0, 0), title, font=title_font)
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)

title_x = (width - (title_bbox[2] - title_bbox[0])) / 2
title_y = height / 2 - 100
subtitle_x = (width - (subtitle_bbox[2] - subtitle_bbox[0])) / 2
subtitle_y = height / 2 + 50

# 绘制文字
draw.text((title_x, title_y), title, font=title_font, fill='white')
draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill='#BDC3C7')  # 浅灰色副标题

# 保存图片
output_path = r'c:\Users\ZYM\Desktop\文本\docs\cover.jpg'
image.save(output_path, quality=95)
print(f"封面图已保存到 {output_path}")
