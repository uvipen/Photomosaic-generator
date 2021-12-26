"""
@author: Thang Nguyen <nhthang1009@gmail.com>
"""
import argparse
import cv2
import numpy as np
import glob
from itertools import product


def get_args():
    parser = argparse.ArgumentParser("Viet Nguyen Photomosaic")
    parser.add_argument("--input", type=str, default="data/input.mp4", help="Path to input video")
    parser.add_argument("--output", type=str, default="data/output.mp4", help="Path to output video")
    parser.add_argument("--pool", type=str, default="image_pool", help="Path to directory containing component images")
    parser.add_argument("--stride", type=int, default=20, help="size of each component image")
    parser.add_argument("--fps", type=int, default=0, help="frame per second")
    parser.add_argument("--overlay_ratio", type=float, default=0.2, help="Overlay width ratio")
    args = parser.parse_args()
    return args


def get_component_images(path, size):
    images = []
    avg_colors = []
    for image_path in glob.glob("{}/*.png".format(path)) + glob.glob("{}/*.jpg".format(path)):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (size, size))
        images.append(image)
        avg_colors.append(np.sum(np.sum(image, axis=0), axis=0) / (size ** 2))
    return images, np.array(avg_colors)


def main(opt):
    cap = cv2.VideoCapture(opt.input)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if opt.fps == 0:
        fps = int(cap.get(cv2.CAP_PROP_FPS))
    else:
        fps = opt.fps
    out = cv2.VideoWriter(opt.output, cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height))
    images, avg_colors = get_component_images(opt.pool, opt.stride)

    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break
        blank_image = np.zeros((height, width, 3), np.uint8)
        for i, j in product(range(int(width / opt.stride)), range(int(height / opt.stride))):
            partial_input_image = frame[j * opt.stride: (j + 1) * opt.stride,
                                  i * opt.stride: (i + 1) * opt.stride, :]
            partial_avg_color = np.sum(np.sum(partial_input_image, axis=0), axis=0) / (opt.stride ** 2)
            distance_matrix = np.linalg.norm(partial_avg_color - avg_colors, axis=1)
            idx = np.argmin(distance_matrix)
            blank_image[j * opt.stride: (j + 1) * opt.stride, i * opt.stride: (i + 1) * opt.stride, :] = images[idx]
        if opt.overlay_ratio:
            overlay = cv2.resize(frame, (int(width * opt.overlay_ratio), int(height * opt.overlay_ratio)))
            blank_image[height-int(height*opt.overlay_ratio):, width-int(width*opt.overlay_ratio):,:] = overlay
        out.write(blank_image)
    cap.release()
    out.release()


if __name__ == '__main__':
    opt = get_args()
    main(opt)
