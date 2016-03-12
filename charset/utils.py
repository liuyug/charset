# encoding: utf-8

import webcolors


def get_colors(step):
    o_colors = [k for k, v in webcolors.css3_names_to_hex.items() if k not in ['black', 'white']]
    o_colors.sort()
    colors_max = len(o_colors)
    miss = step - colors_max
    colors = []
    if miss > 0:
        colors = o_colors
        colors += o_colors[:miss]
    else:
        colors = [o_colors[x] for x in range(0, colors_max, int(colors_max / step))]
    return colors
