#!/bin/bash -eu
FILE_PATH='public/count.csv'
day=`date`
old_num=`tail -n 1 ${FILE_PATH} | awk -F ',' '{print $1}'`
new_num=`expr ${old_num} "*" 2`
echo "${new_num}, ${day}" >> ${FILE_PATH}
