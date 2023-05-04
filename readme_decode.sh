set -e
# To understand our code:
# Our two-stage beam search is implemented in fairseq/monotonic_sequence_generator.py
# We have made detailed code annotation for it. It will be easy for you to understand it.
# To get mono-kd produced pseudo-ref:
# S1. Train an offline NMT.
# S2. Run the mono_kd function below to get the Re-Generated Trainset.
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