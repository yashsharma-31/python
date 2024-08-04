#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

def get_input_args():
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    # Create 3 command line arguments using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='pet_images/', help= 'path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='name of CNN model architecture (vgg, resnet, alexnet)')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='name of file containing dog names')
    
    return parser.parse_args()
