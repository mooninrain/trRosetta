import os
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("NPZDIR", type=str, help="predicted distograms and anglegrams")
parser.add_argument("GTDIR", type=str, help="groundtruth distograms and anglegrams")
args = parser.parse_args()

output_data = args.NPZDIR
gt_data = args.GTDIR
outputlist = os.listdir(output_data)
gtlist = os.listdir(gt_data)

count = 0
for file in outputlist:
    filename1 = os.path.splitext(file)[1]
    filename0 = os.path.splitext(file)[0]
    if filename1=='.npz' and filename0+'.npy' in gtlist:

print('{} files evaluated'.format(count))