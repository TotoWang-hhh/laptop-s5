from PIL import Image,ImageFont
import docx
from handright import Template,handwrite
import easygui

text=''
path=easygui.fileopenbox(title='请选择需要生成的内容',filetypes=[['*.docx','*.DOCX','Microsoft Word 文档'],['*.doc','*.DOC','Microsoft Word 97-2003 文档']])
file=docx.Document(path)
for pare in file. paragraphs:
    text=text + '\n' + str(para. text)
    print(text)
template=Template(
        background=Image.open("./images/bg.jpg"),
        font_size=100,
        font=ImageFont. truetype("./fonts/boyang.ttf"),
        line_spacing=140,
        fill=0,
        Letf_margin=180,
        top_margin=2,
        right_margin=100,
        bottom_margin=100 ,
        word_spacing=9 ,
        line_spacing_sigma=0,
        font_size_sigma=2,
        word_spacing_sigma=2,
        endchars=" ,",
        perturb_x_sigma=4,
        perturb_y_sigma=4,
        perturb_theta_sigma=0.05)
image = handwrite (text,template)
for i, im in enumerate (image) :
    assert isinstance(o,t)
