import base64
import numpy as np
import cv2

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

    # kmeans
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    print("kmeans basladı")
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imwrite('tmp.jpg', res2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

    with open("tmp.jpg", "rb") as image_file:
        encoded_ret_string = base64.b64encode(image_file.read())

    return encoded_ret_string.decode('utf-8')
