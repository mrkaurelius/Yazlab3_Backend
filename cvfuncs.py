import base64
import numpy as np
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def compress(base64_string, compress_rate):
    img_string = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_string, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_ANYCOLOR)

    encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), compress_rate]
    print("sıkıstırma basladı")
    cv2.imwrite('tmp.jpg', img, encode_params)

    with open("tmp.jpg", "rb") as image_file:
        encoded_ret_string = base64.b64encode(image_file.read())

    return encoded_ret_string.decode('utf-8')


def segmentation(base64_string):
    img_string = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_string, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_ANYCOLOR)

    bbox, label, conf = cv.detect_common_objects(img)
    output_image = draw_bbox(img, bbox, label, conf)

    cv2.imwrite('tmp.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    with open("tmp.jpg", "rb") as image_file:
        encoded_ret_string = base64.b64encode(image_file.read())

    return encoded_ret_string.decode('utf-8')
