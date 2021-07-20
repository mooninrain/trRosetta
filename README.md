# *trRosetta*
This package is a part of ***trRosetta*** protein structure prediction protocol developed in: [Improved protein structure prediction using predicted inter-residue orientations](https://www.pnas.org/content/117/3/1496). It includes tools to predict protein inter-residue geometries from a multiple sequence alignment or a single sequence.


Contact: Ivan Anishchenko, aivan@uw.edu

## Updates

[***trRosetta2***](https://github.com/RosettaCommons/trRosetta2) is now available (May 20, 2021)


## Requirements
```tensorflow``` (tested on versions ```1.13``` and ```1.14```)

## Download

```
# download package
git clone https://github.com/mooninrain/trRosetta
cd trRosetta

# download pre-trained network
wget https://files.ipd.uw.edu/pub/trRosetta/model2019_07.tar.bz2
tar xf model2019_07.tar.bz2
```

## Usage
```
python ./network/predict.py -m ./model2019_07 7 example/T1001.a3m example/T1001.npz example/T1001.npy

```
or
```
python ./network/predict_many.py -m ./model2019_07 7 example2/input example2/output example2/gt
```

## Links

* [structure modeling scripts](http://yanglab.nankai.edu.cn/trRosetta/download/) (require [PyRosetta](http://www.pyrosetta.org/))

* [***trRosetta*** server](http://yanglab.nankai.edu.cn/trRosetta/)

* [training set](https://files.ipd.uw.edu/pub/trRosetta/training_set.tar.gz)


## References
J Yang, I Anishchenko, H Park, Z Peng, S Ovchinnikov, D Baker. Improved protein structure prediction using predicted inter-residue orientations. (2020) [PNAS. 117(3): 1496-1503](https://www.pnas.org/content/117/3/1496)
