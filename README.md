## To understand our code:
Our two-stage beam search is implemented in **fairseq/monotonic_sequence_generator.py**.
We have provided comprehensive code annotations to facilitate your understanding of the implementation.
## To get mono-kd produced pseudo-ref:
S1. Train an offline NMT.
S2. Run the mono_kd function in **decode.sh** to get the Re-Generated Trainset.
