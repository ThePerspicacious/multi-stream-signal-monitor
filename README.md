# Multi-Stream Signal Monitor

I built this while running a live signal operation across multiple Telegram channels. 
Standard monitoring scripts kept failing on edge cases I kept hitting in production — 
so I designed one that handled all of them.

Most monitoring tools break when the signal gets noisy.
This one was built specifically for that.
Built to run 24/7 in production — not a script you babysit.

---

## The Problem It Solves

Imagine you're watching 3 live data streams simultaneously.
Each stream is sending messages in real time.
Some messages contain a signal you care about.
Some don't.
Some signals are duplicates.
Some signals are *almost* legitimate — sent by anonymous users trying to piggyback on real ones.

A basic script handles the easy case.
This handles all the cases.

---

## What It Actually Does

- Monitors **3 concurrent Telegram streams** simultaneously using async event loops
- Extracts and validates signals from noisy, unstructured message data using regex pattern matching
- Maintains a **persistent deduplication layer** across sessions — if the process restarts, it doesn't reprocess old signals
- Implements a **5-message context window** to validate anonymous-source signals against a known-good anchor message
- Routes validated signals to **multiple target destinations** based on signal type (Solana vs TRON chain detection)
- Recovers automatically from disconnections — no manual restart needed
- Runs headlessly, deployed on a remote Linux server 24/7

---

## The Part That Was Non-Obvious

The anonymous user edge case.

The system needed to distinguish between:
- A legitimate signal posted by a verified source
- The same signal posted by an anonymous user *after* a legitimate message (valid — they're responding to it)
- The same signal posted by an anonymous user *without* a preceding legitimate message (invalid — likely a copy attempt)

The solution: when an anonymous signal arrives, the script scans the last 5 messages of the stream to check whether a legitimate anchor message exists within that window. If yes — forward. If no — ignore. The anchor itself gets tracked so it can't be reused.

That's not a standard pattern. That's problem-specific logic built from scratch.

---

## Architecture

```
3 Live Telegram Streams
        │
        ▼
  Async Event Loop (Telethon)
        │
        ▼
  Signal Extractor (Regex)
  ├── Solana address pattern
  └── TRON address pattern
        │
        ▼
  Deduplication Check (JSON persistent store)
        │
   ┌────┴────┐
   │         │
Anonymous  Verified
Source     Source
   │         │
5-msg      Direct
window     forward
check         │
   │         │
   └────┬────┘
        ▼
  Multi-Target Router
  ├── Target A (Solana)
  ├── Target B (formatted broadcast)
  └── Target C (TRON)
        │
        ▼
  Persistent State Save
```
---

## Tech Stack

- Python 3
- Telethon (async Telegram client)
- asyncio
- regex
- JSON (persistent state)

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/ThePerspicacious/multi-stream-signal-monitor
cd multi-stream-signal-monitor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure credentials**
```bash
cp config.example.py config.py
# Edit config.py with your values
```

**4. Run**
```bash
python monitor.py
```

To run headlessly on a server:
```bash
tmux new -s monitor
python monitor.py
# Ctrl+B then D to detach
```

---

## Deployment

Deployed on an AWS EC2 Linux instance. Runs detached via tmux, with automatic reconnection on network failures.
i.e.
Hosted on an AWS EC2 instance (Ubuntu Linux) , ( Or You can use EC2 Windows/Mac instance too ).

- Connected via SSH, set up the environment manually.
- Runs detached using tmux — stays alive after terminal closes.
- Automatic reconnection handles network drops without intervention.
- No process manager needed — the reconnection loop inside the script handles restarts on its own.

---

## What I Learned Building This

- Async event-driven architecture behaves differently from sequential scripts — timing and state management require deliberate design.
- Deduplication across sessions is a different problem from deduplication within a session.
- Real-world data streams are noisy — pattern matching needs to be specific enough to avoid false positives and general enough to catch valid signals.
- Reconnection logic is not optional in production — networks fail.
- The edge in any automation system isn't the code — it's the problem-specific logic nobody else thought to build.
---

*Built by Theperspicacious( S.M ) — [github.com/ThePerspicacious](https://github.com/ThePerspicacious)*
