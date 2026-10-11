#!/bin/sh
# Referee N1, check of error E-2: re-runs of the R3 referee's Model N scripts (r3/refwork), showing that error carrying (EC)
# leaves a tau_gen-independent capacity deficit unless BOTH types are converted.
# Recorded outputs (2026-10-11):
#  onetype_A.py 0.03 1.0 6 0.35355 0.5 1.0  -> supf=0.4583, P_f'(2^-8)=0.5000, R=1.0910 at tau=2^-8 (same for g=8)
#  onetype_A.py 0.03 1.0 6 0.35355 0.25 1.0 -> supf=0.3456, R=1.4468 at tau=2^-8
#  twotype_A.py 0.03 1.0 4 0.1 1.0          -> R=1.8729 at tau=2^-8 (bottom value B S^2/n_conv exceeds sup P_f)
#  coupled_full.py 1.0 0.1 1.0 6 1           -> one shift:  R=1.0901 at tau~4.5 (boundary-layer room deficit)
#  coupled_full.py 1.0 0.1 1.0 6 2           -> two shifts: R=0.9998
D=/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r3/refwork
cd "$D" || exit 1
python3 onetype_A.py 0.03 1.0 6 0.35355 0.5 1.0 | tail -1
python3 onetype_A.py 0.03 1.0 8 0.35355 0.5 1.0 | tail -1
python3 onetype_A.py 0.03 1.0 6 0.35355 0.25 1.0 | tail -1
python3 twotype_A.py 0.03 1.0 4 0.1 1.0 | tail -1
python3 coupled_full.py 1.0 0.1 1.0 6 1 | tail -1
python3 coupled_full.py 1.0 0.1 1.0 6 2 | tail -1
