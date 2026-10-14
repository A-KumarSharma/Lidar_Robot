import math 

def sector_min(scan, start_deg, end_deg):

    best = math.inf
    for i , r in enumerate(scan.ranges):
        angle = math.degrees(scan.angle_min+ i* scan.angle_increment)
        if start_deg <= angle <= end_deg and math.isfinite(r) \
                and scan.range_min <= r <= scan.range_max:
            best = min(best,r)
    return best

