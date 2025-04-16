#!/usr/bin/env python

counter = 0
eval_sum = 0.0

with open("pz_blastx_yeast_top1.txt", "r") as blast_handle:
    for line in blast_handle:
        line_stripped = line.strip()
        line_list = line_stripped.split("\t")
        eval_str = line_list[10]

        eval_sum = eval_sum + float(eval_str)
        counter = counter + 1

mean = eval_sum/counter
print(f"Mean is: {mean}")