import os
from matplotlib import font_manager
from matplotlib import rc

font_path = os.path.join(os.getcwd(), "NanumGothic-Regular.ttf")
fontprop = font_manager.FontProperties(fname=font_path)
