import argparse

def get_args():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("gpu", type=str)
    parser.add_argument("ALN", type=str, help="input multiple sequence alignment in A3M/FASTA format")
    parser.add_argument("NPZ", type=str, help="predicted distograms and anglegrams")
    parser.add_argument("GT", type=str, help="groundtruth distograms and anglegrams")
    parser.add_argument('-m', type=str, required=True, dest='MDIR', help='folder with the pre-trained network')

    args = parser.parse_args()

    return args


def get_args_many():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("gpu", type=str)
    parser.add_argument("ALNDIR", type=str, help="folder with input multiple sequence alignments in A3M/FASTA format")
    parser.add_argument("NPZDIR", type=str, help="folder to save predicted distograms and anglegrams")
    parser.add_argument("GTDIR", type=str, help="groundtruth distograms and anglegrams")
    parser.add_argument('-m', type=str, required=True, dest='MDIR', help='folder with the pre-trained network')
                
    args = parser.parse_args()
                    
    return args