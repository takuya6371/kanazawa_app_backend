    
# coding: utf-8
import itertools
from googletrans import Translator

# 自分の得意な言語で
# Let's チャレンジ！！
score_list = []
result_unique_score_list = [0]

score_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for j in range(1, len(score_list) + 1):
    print(j)
    tmp_patern_list = itertools.combinations(score_list, j)
    for k in tmp_patern_list:
        tmp_score_list = list(k)
        sum_score = sum([int(s) for s in tmp_score_list])
        if not sum_score in result_unique_score_list:
            result_unique_score_list.append(sum_score)

print(len(result_unique_score_list))
result_unique_score_list.sort()
for m in result_unique_score_list:
    print(m)