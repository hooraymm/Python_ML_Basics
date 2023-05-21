from camera import VideoCamera from network import Network
import numpy as np
import time
import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="camera", help="--input [image_path]")
args = parser.parse_args()
input_image_path = args.input

model_path ="/home/ubuntu/app_example/models/cyclegan.Ine"
cam_id = 0

def gen(camera):
    icv3 = Network(model_path)
    start = time.time()
    if input_image_path == 'camera' :
        count = 0
        while count < 20:
            orig_img = camera.get_frame()
            count = count + 1
        start time.time()
        orig_img = camera.get_frame()
        crop_img icv3.crop_image(orig_img) input_img = icv3.resize_img(crop_img)
        out_img = icv3.inference(input_img)
        frame_Ine = icv3.post_draw(crop_img, out_img)
    else:
        orig_img = icv3.open_image(input_image_path) crop_img = icv3.crop_image(orig_img)
        input_img = icv3.resize_img_rgb(crop_img)
        out_img = icv3.inference(input_img)
        frame_Ine = icv3.post_draw_rgb(crop_img, out_img)

    end = time.time()
    print("Total", end - start)
if __name__ == '__main__':
    gen(VideoCamera(cam_id))

