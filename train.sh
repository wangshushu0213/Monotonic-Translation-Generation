MODEL=PATH_TO_MODEL
DATA=PATH_TO_DATA
MAX_EPOCH=80
LOG=PATH_TO_LOG
PYTHON=PATH_TO_PYTHON

CUDA_VISIBLE_DEVICES=0,1 $PYTHON -u train.py $DATA  --arch  transformer_wmt_en_de \
  --no-progress-bar --log-interval 3000 \
  --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
  --lr-scheduler inverse_sqrt --warmup-init-lr 1e-07 --warmup-updates 4000 \
  --lr 0.0003  --dropout 0.3 --weight-decay 0.0001 --criterion label_smoothed_cross_entropy --label-smoothing 0.1  \
  --max-tokens 8196 --update-freq 2  \
  --save-dir $MODEL --max-epoch $MAX_EPOCH  --fp16 --save-interval 1 --share-decoder-input-output-embed > $LOG