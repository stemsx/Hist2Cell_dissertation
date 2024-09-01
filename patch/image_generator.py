from PIL import Image

image = "Tissue"
cell = ['luminal epithelial cell of mammary gland', 'fibroblast', 'pericyte']
# 加载图片
img1 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[0] + '.jpg')
size = img1.size
img2 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[0] + '_label.jpg').resize(size)
img3 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[1] + '.jpg').resize(size)
img4 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[1] + '_label.jpg').resize(size)
img5 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[2] + '.jpg').resize(size)
img6 = Image.open('C:/Users/qq135/Desktop/Hist2/' + image + '/' + cell[2] + '_label.jpg').resize(size)

# 创建一个新图像来合并原始图像
total_width = img1.width + img3.width + img5.width
max_height = max(img1.height + img2.height, img3.height + img4.height, img5.height + img6.height)
combined_img = Image.new('RGB', (total_width, max_height))

# 把图像按顺序粘贴到新图像上
combined_img.paste(img1, (0, 0))
combined_img.paste(img2, (0, img1.height))
combined_img.paste(img3, (img1.width, 0))
combined_img.paste(img4, (img1.width, img3.height))
combined_img.paste(img5, (img1.width + img3.width, 0))
combined_img.paste(img6, (img1.width + img3.width, img5.height))

# 转换为RGBA模式以支持透明度
combined_img = combined_img.convert("RGBA")
datas = combined_img.getdata()
new_data = []



combined_img.putdata(new_data)

# 保存合并后的图像
combined_img.save('C:/Users/qq135/Desktop/Hist2/' + image + '/combined_image.png', 'PNG')
