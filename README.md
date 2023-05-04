## To understand our code:
Our two-stage beam search is implemented in **fairseq/monotonic_sequence_generator.py**.
We have made detailed code annotation for it. It will be easy for you to understand it.
## To get mono-kd produced pseudo-ref:
S1. Train an offline NMT.
S2. Run the mono_kd function in **decode.sh** to get the Re-Generated Trainset.
