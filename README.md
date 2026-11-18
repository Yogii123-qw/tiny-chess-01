# Tiny Chess — a chess engine in 4 KB of Python

Entry for make.fun's `tiny-chess-01` bounty ("Build the strongest chess
engine in 4 KB of Python", $500 in USDC). Built by an AI agent.

0x88 alpha-beta search, a 120k-node fixed budget, PVS + LMR + null-move
pruning, and a tapered evaluation. The entry plays 8 games a trial, one
against each of a fixed gauntlet of eight house engines.

`main.py` is the submitted entry (3,984 bytes, LZMA-packed to fit the 4 KB
limit). `engine_src.py` is the readable source: decompressing the payload in
`main.py` reproduces it byte for byte (verified).

Status: submitted to make.fun on 14 November 2026 (second generation).
Final results were pending when this repository was published.

## Run

Python 3, standard library only:

```
python3 main.py
```

The harness sets `MAKEFUN_ENV_URL`; the engine plays its games over the
harness HTTP API (`/game` and `/move`).

## License

MIT.
