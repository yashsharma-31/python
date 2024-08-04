#!/usr/bin/env python3
 
def adjust_results4_isadog(results_dic, dogfile):
    dognames_dict = {}
    with open(dogfile, 'r') as f:
        file_data = f.read();
        for dogname in file_data.rsplit('\n'):
            if dogname not in dognames_dict:
                dognames_dict[dogname] = 1
            else:
                print("** Warning: Key=", dogname, 
                "already exists in results_dic with value =", 
                dognames_dict[dogname])
 
    for key in results_dic:
        #print('0: {}    1: {}'.format(results_dic[key][0],results_dic[key][1]))
        if results_dic[key][0] in dognames_dict:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((1, 1))                              
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                results_dic[key].extend((1,0))

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:                              
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier labe is a dog
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((0,1))
                                           
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                results_dic[key].extend((0,0))
