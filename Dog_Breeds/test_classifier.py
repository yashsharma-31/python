#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from classifier import classifier 

test_image="pet_images/Collie_03797.jpg" 
model = "vgg"
image_classification = classifier(test_image, model)

# prints result from running classifier() function
print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
      model, "was classified as a:", image_classification)
