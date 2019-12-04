#coding:utf-8
import numpy as np

class ApertureContourException(Exception):
    pass

def is_valid_aperture(aperture):
    if not isinstance(aperture, np.ndarray):
        raise ApertureContourException("aperture must be a numpy.ndarray class")
    if aperture.dtype not in (np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64, np.bool):
        raise ApertureContourException("data type of aperture must be a bool or int")
    if not aperture.ndim == 2:
        raise ApertureContourException("aperture must be 2 dimensional data")
    return aperture


# Try all four directions to check if there is a direction to proceed
def go_point(point, points):
    directions = [(0.5, 0), (0, 0.5), (-0.5, 0), (0, -0.5)]
    #Try each directions
    for direction in directions:
        point_cand = point + direction
        is_point = np.all(points == point_cand, axis=1)
        #if proceed
        if np.sum(is_point) != 0:
            #delete previous points
            indexes = np.where(is_point)
            points = np.delete(points, indexes[0][0], 0)
            return point_cand, points
    #If can't go anywhere, return None
    else:
        return None, points

def make_contours(aperture):
    aperture = is_valid_aperture(aperture)
    # the coordinates of each point of the aperture
    h, w = np.where(aperture != 0)
    pixs = np.vstack((w, h)).T
    # the edge and side points of each coordinates
    TR = pixs + np.array([-0.5, -0.5])
    TL = pixs + np.array([0.5, -0.5])
    BR = pixs + np.array([-0.5, 0.5])
    BL = pixs + np.array([0.5, 0.5])
    R = pixs + np.array([-0.5, 0])
    L = pixs + np.array([0.5, 0])
    T = pixs + np.array([0, -0.5])
    B = pixs + np.array([0, 0.5])
    points_edge = np.vstack((TR, TL, BR, BL))
    points_side = np.vstack((T, B, R, L))
    # remove duplicate
    points_edge_unique = np.unique(points_edge, axis=0)
    points_side_unique = np.unique(points_side, axis=0)
    # removed points which are not part of the aperture contour
    points_edge_all = np.array([point for point in points_edge_unique if np.sum(np.all(points_edge == point, axis=1)) != 4])
    points_side_all = np.array([point for point in points_side_unique if np.sum(np.all(points_side == point, axis=1)) != 2])
    # the crossing point shares the edge of two pixels, so it counts twice
    points_cross_cand = [point for point in points_edge_all if np.sum(np.all(points_edge == point, axis=1)) == 2]
    # the crossing point has 4 side points
    points_cross_all = np.array([point for point in points_cross_cand if np.sum(np.all(np.abs(points_side_all - point) <= 0.5, axis=1)) == 4])
    # stack all points
    if points_cross_all.shape[0] == 0:
        points_all = np.vstack((points_edge_all, points_side_all))
    else:
        points_all = np.vstack((points_edge_all, points_side_all, points_cross_all))
    # line up points which consist contour
    lines = []
    # Since the contours are not limited to one, check all separated contours
    while points_all.shape[0] != 0:
        point = points_all[0]
        contour = []
        # draw one contour
        while point is not None:
            contour.append(point)
            point, points_all = go_point(point, points_all)
        #Extract edge points
        contour_arr = np.array(contour)
        diffs = np.diff(contour_arr, 2, axis=0)
        diffs = np.vstack((np.zeros(2), diffs, np.zeros(2)))
        contour_point = np.vstack((contour[0], contour_arr[np.all(diffs != 0, axis=1)], contour[0]))
        lines.append(contour_point)
    return lines

def draw_contours(canvas, aperture, **kwargs):
    points_list = make_contours(aperture)
    for points in points_list:
        for i in range(len(points) - 1):
            canvas.plot((points[i][0], points[i+1][0]), (points[i][1], points[i+1][1]),  "-", **kwargs)
    return canvas
