# One Star, Five Stars for the Food

A one-sentence review of planet Earth by an alien tourist: one star for the
planet, five stars for the food. `main.py` (Python standard library only)
writes that single sentence to `/output/entry.txt`.

Entry for the make.fun bounty: https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7

[![Bounty](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/freysiatiara/one-star-five-stars-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/freysiatiara/one-star-five-stars-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

## Run

```sh
python3 main.py
```

Writes the review to `/output/entry.txt` (or `$ENTRY_OUTPUT`, or
`$OUTPUT_DIR/entry.txt` / `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).
The output is deterministic: every run writes the exact same bytes,
and the file is created with mode `0644`.
