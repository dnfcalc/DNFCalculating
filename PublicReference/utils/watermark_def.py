# 水印附近背景色-排行榜界面
watermark_surrounding_backgroud_color_ranking = (21, 39, 65)
# 水印附近背景色-详情界面
watermark_surrounding_backgroud_color_detail = (27, 14, 6)
# 水印与背景色的偏差值
watermark_delta = -5
# 考虑到图片压缩，水印色彩允许的上下偏移值
watermark_tolerance_value = 1
# 替换为显著颜色
reverse_color = (255, 255, 255)


def make_watermark_qt_color_string(
        watermark_surrounding_backgroud_color: tuple):
    color_str = ', '.join((str(rgb + watermark_delta)
                           for rgb in watermark_surrounding_backgroud_color))
    return f"color:rgb({color_str})"
