#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import face_recognition


def get_face_similarity(img1, img2):
    """ 计算人脸相似度
    """
    image = face_recognition.load_image_file(img1)
    face_encodings = face_recognition.face_encodings(image, num_jitters=128)
    print(face_encodings)
    if len(face_encodings) > 0:
        unknown_image = face_recognition.load_image_file(img2)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image, num_jitters=128)
        print(unknown_face_encodings)

        if len(unknown_face_encodings) > 0:
            return face_recognition.face_distance(
                face_encodings, 
                unknown_face_encodings[0]
            )

    return 0

def main():
    """ 人脸识别

        1. 接收输入的两张图片地址
        2. 计算两张图片中人脸的相似度
    """
    if len(sys.argv) < 3:
        return 

    img1 = sys.argv[1]
    img2 = sys.argv[2]
    print(img1, img1)

    # TODO: 修改以下内容，按要求实现
    print(get_face_similarity(img1, img1))

if __name__ == '__main__':
    main()