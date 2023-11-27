# author: amirhossein khatami
# mail: amirkhatami@gmail.com
# importing libraries
import numpy as np


def nearest_point(point, points):
    """
    Find the nearest point to the given point.

    Args:
        point (list): The given point.
        points (list): The list of points.

    Returns:
        float: The x-coordinate of the nearest point.
    """
    def distance(point, points):
        
        """
        Find the distance of the given point to the points in the list.

        Args:
            point (list): The given point.
            points (list): The list of points.

        Returns:
            list: The list of distances.
        """
        distances = []
        for p in points:
            temp = np.sqrt((p[0] - point[0]) ** 2 + (p[1] - point[1]) ** 2)
            distances.append(temp)
        return distances

    def find_nearest_point(distances):
        """ this function find the nearest point to the given point
        Args:
            distances (list): The list of distances.
        
        Returns:
            float: The x-coordinate of the nearest point.
        """
        np_distances = np.array(distances, dtype=np.float64)
        return points[np.argmin(np_distances)]

    return find_nearest_point(distance(point, points))