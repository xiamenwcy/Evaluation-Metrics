# -*- coding: utf-8 -*-

"""
@date: 2020/5/25 下午3:46
@file: test_map_voc.py
@author: zj
@description: 
"""

from metrics.map import voc_evaluation

if __name__ == '__main__':
    ground_truth_dir = './input/ground-truth'
    detection_result_dir = './input/detection-results'
    tmp_json_dir = './.tmp_files'

    metrics = voc_evaluation(ground_truth_dir, detection_result_dir, tmp_json_dir)

    for key, item in metrics.items():
        print('{} = {:.3f}%'.format(key, item * 100))
