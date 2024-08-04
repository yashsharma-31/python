#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Imports classifier function for using CNN to classify images 
from classifier import classifier
# from get_pet_labels import get_pet_labels

def classify_images(images_dir, results_dic, model):
    for key,val in results_dic.items():
        img_path = images_dir+key
        image_classification = classifier(img_path, model)
        words = image_classification.lower().strip()
        res = 1 if val[0] in words else 0
        results_dic[key].append(words)
        results_dic[key].append(res)
        
# results_dic = get_pet_labels('pet_images/')
# classify_images('pet_images/', results_dic, "vgg")
# print(results_dic)