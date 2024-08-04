#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir

def get_pet_labels(image_dir):
    
    file_name_list = listdir(image_dir)
    pet_labels =[]
    for name in file_name_list:
        if name[0]!='.':
            label =''
            for word in name.split('_'):
                word = word.lower()
                if word.isalpha():
                    label+= word+' '
                else:
                    break
            pet_labels.append(label.strip())
    results_dic = {}
    for idx in range(0, len(file_name_list),1):
        if file_name_list[idx] not in results_dic:
            results_dic[file_name_list[idx]] = [pet_labels[idx]]
        else:
            print("** Warning: Key=", file_name_list[idx], 
               "already exists in results_dic with value =", 
               results_dic[file_name_list[idx]])
      
    return results_dic

