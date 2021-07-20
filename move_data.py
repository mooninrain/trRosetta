import os
import shutil

src_input_data = "/data/hdd01/jiaqi/fan/datasets/hhblits_msa_aln"
src_gt_data = "/data/hdd01/jiaqi/fan/datasets/gt_contact_map"
inputlist = os.listdir(src_input_data)
gtlist = os.listdir(src_gt_data)

dst_input_data = "/data/hdd01/jiaqi/ruidong/data/trRosetta/set2/input"
dst_gt_data = "/data/hdd01/jiaqi/ruidong/data/trRosetta/set2/gt"
if not os.path.exists(dst_input_data):
    os.makedirs(dst_input_data)
if not os.path.exists(dst_gt_data):
    os.makedirs(dst_gt_data)

count = 0
for files in inputlist:
    filename1 = os.path.splitext(files)[1]
    filename0 = os.path.splitext(files)[0]
    if filename1=='.a3m' and filename0+'.npy' in gtlist:
        srcpath = os.path.join(src_input_data, files)
        dstpath = os.path.join(dst_input_data, files)
        shutil.copy(srcpath, dstpath)

        srcpath = os.path.join(src_gt_data, filename0+'.npy')
        dstpath = os.path.join(dst_gt_data, filename0+'.npy')
        shutil.copy(srcpath, dstpath)

        count+=1

        if count==10:
            break

print('{} files moved'.format(count))