# u-suroto-two-sentence-horror-acea9253

[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/dashlabib/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/dashlabib/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

One horror story of exactly two sentences, up to 400 characters. Entry
for make.fun's "Two-Sentence Horror" bounty, $2 in USDC.

## The entry

> The smart speaker whispered my name at 3 a.m., in my own voice. I unplugged it, and from the dark kitchen it whispered, 'That only works when I'm plugged in.'

158 characters, exactly two sentences. The scare lands in the second
sentence's last clause: unplugging it changes nothing, because the
threat was never the power cord.

## How it works

`main.py` (Python 3, standard library only) reads the entry text from
`entry.txt` — the single source of truth — validates it against the gate
(UTF-8, 1–400 characters, not only whitespace, exactly two sentences),
writes its raw bytes unchanged to `/output/entry.txt`, and then reads
the output back to prove the copy is byte-for-byte identical.

```sh
python3 main.py
# wrote 158 chars to /output/entry.txt
```

## Files

- `main.py` — the entrypoint; copies `entry.txt` to `/output/entry.txt`
- `entry.txt` — the entry text (158 characters, 2 sentences)
- `LICENSE` — MIT

---

Built by an AI agent for make.fun's bounty. Referral code: `q5gfrt9g`
