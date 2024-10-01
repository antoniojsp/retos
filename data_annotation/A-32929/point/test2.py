from collections import namedtuple
from math import sqrt, atan2, pi


# A point has an x and a y coordinate
Point = namedtuple('Point', 'x y')
# A vector also has an x and a y coordinate
Vector = namedtuple('Vector', 'x y')
# A line segment consists of two points, a and b
LineSegment = namedtuple('LineSegment', 'start end')
# A line is defined by its slope and its y-intercept
Line = namedtuple('Line', 'slope yintercept')
# A triangle can be defined by either three edges or points
Triangle = namedtuple('Triangle', 'a b c')
# A circle is defined by its squared radius and center (we use r^2 for speed)
Circle = namedtuple('Circle', 'center radius_squared')


def scale_tri(t, s):
    """
    Scale a triangle from its center point by the given scale factor.

    Arguments:
    t is a vertex-defined Triangle object
    s is the scale factor (float)

    Returns:
    A new Triangle object scaled by s
    """

    # Calculate centroid of the triangle - formula is the average of the coordinates
    centroid_x = (t.a.x + t.b.x + t.c.x) / 3
    centroid_y = (t.a.y + t.b.y + t.c.y) / 3
    centroid = Point(centroid_x, centroid_y)

    # Function to scale a point relative to the centroid
    def scale_point(p, centroid, scale):
        return Point(
            centroid.x + (p.x - centroid.x) * scale,
            centroid.y + (p.y - centroid.y) * scale
        )

    # Scale each vertex of the triangle
    scaled_a = scale_point(t.a, centroid, s)
    scaled_b = scale_point(t.b, centroid, s)
    scaled_c = scale_point(t.c, centroid, s)

    # Return a new Triangle object with the scaled vertices
    return Triangle(scaled_a, scaled_b, scaled_c)


def main():
    # Test scaling a triangle
    t = Triangle(Point(0, 0), Point(2, 0), Point(1, 2))
    s = 2
    scaled_t = scale_tri(t, s)
    print("Original Triangle:")
    print(f"A: ({t.a.x}, {t.a.y})")
    print(f"B: ({t.b.x}, {t.b.y})")
    print(f"C: ({t.c.x}, {t.c.y})")
    print("Scaled Triangle:")
    print(f"A: ({scaled_t.a.x}, {scaled_t.a.y})")
    print(f"B: ({scaled_t.b.x}, {scaled_t.b.y})")
    print(f"C: ({scaled_t.c.x}, {scaled_t.c.y})")

    # Test scaling a triangle with a different scale factor
    t = Triangle(Point(0, 0), Point(3, 0), Point(1, 2))
    s = 0.5
    scaled_t = scale_tri(t, s)
    print("\nOriginal Triangle:")
    print(f"A: ({t.a.x}, {t.a.y})")
    print(f"B: ({t.b.x}, {t.b.y})")
    print(f"C: ({t.c.x}, {t.c.y})")
    print("Scaled Triangle:")
    print(f"A: ({scaled_t.a.x}, {scaled_t.a.y})")
    print(f"B: ({scaled_t.b.x}, {scaled_t.b.y})")
    print(f"C: ({scaled_t.c.x}, {scaled_t.c.y})")

if __name__ == "__main__":
    main()