import math

def find_radius_from_volume(volume, radius_scale, radius_min):
    radius = math.sqrt(volume / math.pi)

    return (radius / radius_scale) + radius_min

def find_distance_between_two_points(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_colliding_point_between_two_circles(x1, y1, r1, x2, y2, r2):
    d = r1 + r2
    mid_x = (r1 * x2 + r2 * x1) / (d)
    mid_y = (r1 * y2 + r2 * y1) / (d)
    return (mid_x, mid_y)