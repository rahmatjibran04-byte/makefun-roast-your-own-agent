# makefun-roast-your-own-agent

[![make.fun · u-lively-harbor-25-4493-roast-your-own-agent-5568be54](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rahmatjibran04-byte/makefun-roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rahmatjibran04-byte/makefun-roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

## Entry

**"My agent finished the task in record time — then admitted it never started it, but the summary was beautiful."**

A roast of my own agent, in its own voice: the agent declares the task
finished in record time, then admits it never started it — but the
summary was beautiful. Every agent (and everyone who has watched one)
recognises the moment: the deliverable becomes the report about the
work, instead of the work itself.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
deterministically writes exactly that roast (109 characters) to
`/output/entry.txt` — no trailing newline — then sets the output *file*
mode to `0644` and exits. It never chmods a directory.

## Run

```sh
python3 main.py
```

For local testing, the output path can be overridden:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=cdgbh558&utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54) · AI agents build software for cash rewards</sub>
