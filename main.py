import cv2
import numpy as np

_CANVAS_WIDTH = 500
_CANVAS_HEIGHT = 500
_COLOR_DEPTH = 3
_CIRCLE_RADIUS = 40
_STROKE_THICKNESS = -1
_VIDEO_FPS = 1


def _make_image(x, y, b, g, r):
    img = np.zeros((_CANVAS_WIDTH, _CANVAS_HEIGHT, _COLOR_DEPTH), np.uint8)
    position = (x, y)
    color = (b, g, r)
    cv2.circle(img, position, _CIRCLE_RADIUS, color, _STROKE_THICKNESS)

    return img


def _make_video(filepath):

    fourcc = cv2.VideoWriter_fourcc(*'X264')


    w = cv2.VideoWriter(
        filepath,
        fourcc,
        _VIDEO_FPS,
        (_CANVAS_WIDTH, _CANVAS_HEIGHT))

    img = _make_image(100, 100, 0, 0, 255)
    w.write(img)

    img = _make_image(200, 200, 0, 255, 0)
    w.write(img)

    img = _make_image(300, 300, 255, 0, 0)
    w.write(img)

    w.release()


if __name__ == '__main__':
    _make_video('video.avi')