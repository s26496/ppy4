import math


def panel_calc(floor_length, floor_width, panel_length, panel_width, panels_in_package):
    room_area = (floor_length*floor_width)*1.1
    panel_area = panel_length*panel_width
    panels_required = math.ceil(room_area/panel_area)
    packages_required = math.ceil(panels_required/panels_in_package)

    return packages_required





