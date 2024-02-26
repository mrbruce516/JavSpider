#!/bin/bash
# IFS避免识别空格，方便写入数组 
IFS=$'\n'
dir_arrs=( `ls -l|grep ^d|awk '{print $8}'` )
IFS=$OIFS

# 清理垃圾广告
for i in ${dir_arrs[@]}
do
    cd "$i"
    IFS=$'\n'
    obj_arrs=( `find . ! -name '.' -and ! -name 'clean.sh' -and ! -regex '.*\([A-Z]+-[0-9]+\)\(.*\)'` )
    IFS=$OIFS
    for obj in ${obj_arrs[@]}
    do
        rm -rf $obj
    done
    cd ..
done

# 放到jellyfin目录
pwd
for i in ${dir_arrs[@]}
do
    mv $i /data/jellyfin/media/ero/AV
done