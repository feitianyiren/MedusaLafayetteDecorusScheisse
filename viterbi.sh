#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage:viterbi.sh <model name> <output name>"
	echo "ex: viterbi.sh models/mymodel.mdl predictions/myoutput.csv"
	exit 1;
fi

src_dir=src
data_dir=training_data
pred_dir=predictions
model_dir=models
log_dir=log

n_in=351
n_out=1943
n_layers=4
n_neurons=2048
#dropout=0.5

THEANO_FLAGS=device=cpu python2 -u $src_dir/viterbi.py --input-dim $n_in --output-dim $n_out \
	--hidden-layers $n_layers --neurons-per-layer $n_neurons \
    $data_dir/real/test.in $1 \
    $data_dir/hmm.mdl $2
