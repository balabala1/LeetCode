# A Weighted GCN with Logical Adjacency Matrix for Relation Extraction(ECAI 2020)
PyTorch implementation of Deep Learning approach for relation extraction task(SemEval 2010 Task 8 and TACRED) via a Weighted Graph Convolutional Neural Networks with Entity-Attention (EA-WGCN).<\br>
This paper proposes a novel weighted graph convolutional network by constructing a logical adjacency matrix which effectively solves the feature fusion of multi-hop relation without additional layers and parameters for relation extraction task. Experimental results show that our model can take better advantage of the structural information in the dependency tree and produce better results than previous models. <\br>
You can find the paper here(http://ecai2020.eu/papers/957_paper.pdf) <\br>
The figure below shows the overall architecture of the model: 
#Requirements
Python 3 (tested on 3.7.3)
PyTorch (tested on 1.1.0)
tqdm, pickle
# Usage
## Preparation
We evaluate the performance of our model on TACRED and SemEval 2010 Task 8 datasets. This code needs to use the TACRED dataset(LDC license required). If you get the TACRED dataset, please put the JSON files under the directory dataset/tacred. In this repository, we provide only sample data from TACRED dataset. If you want to change the data set, you can go here(http://semeval2.fbk.eu/semeval2.php) to get the SemEval 2010 Task 8 datasets. But you need to do your own data preprocessing.<\br>

First, since the pre-training GLoVe vectors is applied, you need to download from the Stanford NLP group website (https://nlp.stanford.edu/projects/glove/) and unzip it to the directory 
dataset/glove. <\br>
Then prepare vocabulary and initial word vectors with: <\br>

python3 prepare_vocab.py dataset/tacred dataset/vocab dataset/glove
The vocabulary and word vectors can be saved under this directory dataset/vocab.

## Training
To train a EA-WGCN model, run:
python3 train.py 
Model checkpoints and logs will be saved to ./saved_models. For details on the use of other parameters, please refer to train.py.
## Evaluation
To run evaluation on the test set, run:
python3 evaluate.py --model_dir saved_models/best_model 

## Ensemble
To run an ensemble model, run:
python3 ensemble.py

#Citation
@inproceedings{????,
 author = { Li Zhou and Tingyu Wang and Hong Qu and Li Huang and Yuguo Liu },
 booktitle = {Proc. of ECAI},
 title = { A Weighted GCN with Logical Adjacency Matrix for Relation Extraction },
 year = {2020}
}
