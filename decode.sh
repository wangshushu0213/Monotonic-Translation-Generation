set -e
MODEL=PATH_TO_MODEL
DATA=PATH_TO_DATA
PYTHON=PATH_TO_PYTHON
BEAMSIZE=5

function kd(){
OUTPUT=PATH_TO_OUTPUT
CUDA_VISIBLE_DEVICES=0 $PYTHON fairseq_cli/generate.py $DATA  \
    --gen-subset test --no-progress-bar \
    --path $MODEL --remove-bpe \
    --max-tokens 8000  --beam $BEAMSIZE  \
    --fp16  > $OUTPUT
}

function mono_kd(){
k=7
OUTPUT=PATH_TO_OUTPUT
CUDA_VISIBLE_DEVICES=0 $PYTHON fairseq_cli/generate.py $DATA  \
    --gen-subset test --no-progress-bar \
    --path $MODEL --remove-bpe \
    --max-tokens 8000  --beam $BEAMSIZE  \
     --fp16 --generator-class monotonic  --latency $k > $OUTPUT
}
