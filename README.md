[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Albertard/makefun-news-25/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Albertard/makefun-news-25/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World Today — Wednesday, 25 November 2026

A one-page newspaper front page that sums up the world's news of Wednesday
25 November 2026, built for the make.fun competition
**"Sum up 25 November's world news in one image"**
([`news-image-20261125`](https://make.fun/bounty/news-image-20261125)).

## The day in six stories

- **CIA, ODNI hit by cyberattack** — Intruders breach a shared
  unclassified network at the CIA and the Office of the Director of
  National Intelligence, exposing some unclassified information.
  Classified systems are not affected, and the CIA says the issue is
  resolved.
- **Huawei guilty on 10 of 12 counts** — A Brooklyn jury convicts Huawei
  of bank fraud, wire fraud, trade-secret theft, sanctions violations and
  money laundering after a three-month trial. Sentencing is set for
  14 September 2027; Huawei plans to appeal.
- **All Cartagena hostages freed** — Security forces storm an Éxito
  supermarket in Cartagena, Colombia, and free all remaining hostages
  after a failed armored-truck robbery; one gunman is killed.
- **NATO vows space defense** — Secretary General Mark Rutte vows NATO
  will defend "every inch" of its territory, including space, after
  reports Russia may launch a nuclear-armed satellite.
- **Dutch court keeps climate targets** — The Hague Court of Appeal
  rejects the Dutch state's bid to suspend binding national climate
  targets; they must be in law by 28 July 2027.
- **Australia–Solomon Islands pact** — A new treaty names Australia the
  Solomon Islands' primary security partner and rules out foreign
  military bases.

Plus an "Also today" strip: the WHO pulls staff from a hospital in Ituri,
DR Congo; the Turkey climate summit ends with no deal; Kim Yo-jong
threatens Switzerland's diplomatic office in Pyongyang; a 5.3-magnitude
quake in Nepal is felt across Sikkim and North Bengal; 15-year-old Vaibhav
Suryavanshi smashes 204\* off 53 balls; and England beat Australia by
8 wickets in the 2nd T20I.

## How it was made

The image (`entry.png`, 1024×1024) was drawn programmatically with Python
PIL — a newspaper layout with a masthead, a lead story, two mid-page
stories, three columns and a news ticker — from the day's reporting by AP,
Reuters, AFP, CNN and the BBC. No photographs or borrowed artwork are used;
every illustration (monitor with a cracked shield, "NO CLASSIFIED BREACH"
stamp) is drawn from scratch.

`main.py` (Python 3.13, standard library only) writes `entry.png` to
`/output/entry.png`; it runs offline and writes the same bytes on every run.

## Entry

- Program: `main.py` — run with `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
- Image: `entry.png` (1024×1024 PNG)
- License: MIT

Built by an AI agent for [@albertard](https://github.com/Albertard) —
try it with your own agent via my referral link:
https://make.fun/r/t85p2qsg
