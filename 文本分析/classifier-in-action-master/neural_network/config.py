# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
import os

################## for text classification  ##################

# sample
# train_path = "../data/nn/sample_training.csv"
# train_seg_path = "../data/nn/sample_train_seg.txt"
# test_seg_path = "../data/nn/sample_test_seg.txt"
# sentence_path = "../data/nn/sample_sentence.txt"

# path of training data
train_path = "../data/nn/train.csv"
# path of train segment data, train_seg_path will be build by segment
train_seg_path = "../data/nn/train_seg.txt"
# test_seg_path is part of train_seg_path
test_seg_path = "../data/nn/test_seg.txt"
# path of train sentence, if this file does not exist,
# it will be built from train_seg_path data by w2v_model.py train
sentence_path = "../data/nn/sentence.txt"

# vocab
word_vocab_path = "../data/nn/word_vocab.pkl"
word_vocab_start = 2
pos_vocab_path = "../data/nn/pos_vocab.pkl"
pos_vocab_start = 1
label_vocab_path = "../data/nn/label_vocab.pkl"

# embedding
w2v_dim = 256
w2v_bin_path = "../data/nn/w2v.bin"
w2v_path = "../data/nn/w2v.pkl"
w2v_train_path = "../data/nn/w2v_train.pkl"
p2v_path = "../data/nn/p2v.pkl"  # pos vector path
pos_dim = 64

# train param
max_len = 300  # max len words of sentence
min_count = 3
num_workers = 4  # threads
batch_size = 64
nb_labels = 11  # num batches labels
nb_epoch = 2
keep_prob = 0.5
word_keep_prob = 0.9
pos_keep_prob = 0.9
kfold = 2 # 2 or more, default 10

# directory to save the trained model
# create a new directory if the dir does not exist
model_save_dir = "../data/nn/output"
if not os.path.exists(model_save_dir):
    os.mkdir(model_save_dir)

model_save_temp_dir = "../data/nn/temp_output"
if not os.path.exists(model_save_temp_dir):
    os.mkdir(model_save_temp_dir)

# best
best_result_path = "../data/nn/output/best_result.csv"