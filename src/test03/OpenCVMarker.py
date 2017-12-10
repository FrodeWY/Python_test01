import json
import os
import cv2
import numpy as np
import subprocess

path = 'C:/Users/mac/Desktop/wujing_short.mp4_labeled/'
path2 = 'C:/Users/mac/Desktop/wujing_short.mp4_jsons/'


class Marker:

    def marker_image(self,json_dir_path, image_dir_path, lable):

        pathDir = os.listdir(json_dir_path)
        suffix = '.png'

        for i in range(len(pathDir)):
            if json_dir_path.endswith('/'):
                json_path = json_dir_path + pathDir[i]
            else:
                json_path = json_dir_path + "/" + pathDir[i]
            f = open(json_path, encoding='utf-8')
            jsons = json.load(f)
            for single_json in jsons:
                right = single_json['bottomright']['x']
                bot = single_json['bottomright']['y']
                left = single_json['topleft']['x']
                top = single_json['topleft']['y']
                json_lable = single_json['label']
                mess = json_lable + str(single_json['confidence'])
                if json_lable == lable:
                    file_name = str(pathDir[i]).split(".")[0]
                
                    if image_dir_path.endswith("/"):
                        image_file_path = image_dir_path + file_name + suffix
                    else:
                        image_file_path = image_dir_path + "/" + file_name + suffix
                    if os.path.exists(image_file_path):
                        if type(image_file_path) is not np.ndarray:
                            imgcv = cv2.imread(image_file_path)
                        else:
                            imgcv = image_file_path
                        h, w, _ = imgcv.shape
                        thick = int((h + w) // 300)
                        if (os.path.exists(image_file_path)):
                            cv2.rectangle(imgcv, (left, top), (right, bot), (255, 0, 0), thick)
                            cv2.putText(imgcv, mess, (left, top - 12), 0, 1e-3 * h, (0, 255, 0), thick // 3)
                            cv2.imwrite(image_file_path, imgcv)
                            subprocess.Popen('ffmpeg -i  %d.png video.mp4')

    @staticmethod
    def cut_map(video, path):
        subprocess.Popen('ffmpeg -i ' + video + ' -vframes 25 ' + '%d.png')


path = 'C:/Users/mac/Desktop/wujing_short.mp4_images'
maker = Marker()
# maker.cut_map("C:/Users/mac/Desktop/wujing_short.mp4", path)

maker.marker_image(path2, path, 'wujing')
