#!/usr/bin/env python
#-*- coding: utf-8 -*-

import distance

def get_sentence_similarity(s1, s2):
    """ 计算句子相似度
    """
    return distance.levenshtein(s1, s2)

def main():
    """ 基于句子相似度的闲聊程序

        1. 构建对话库
        2. 接收输入的句子，遍历对话库的问题，计算相似度，得到相似度最高的问题，并返回答案
    """
    s1 = input("请输入问题： ")

    # TODO： 修改以下内容，按要求实现

    # 对话库
    dataset = {}
    
    print(s1)


if __name__ == '__main__':
    main()