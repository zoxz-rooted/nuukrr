<p align="center">
  <pre>
    ███╗   ██╗██╗   ██╗██╗   ██╗██╗  ██╗██████╗ ███████╗
    ████╗  ██║██║   ██║██║   ██║██║ ██╔╝██╔══██╗██╔════╝
    ██╔██╗ ██║██║   ██║██║   ██║█████╔╝ ██████╔╝█████╗  
    ██║╚██╗██║██║   ██║██║   ██║██╔═██╗ ██╔══██╗██╔══╝  
    ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██╗██║  ██║███████╗
    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                        
         ███╗   ██╗██╗   ██╗██╗   ██╗██╗  ██╗██████╗ ███████╗
         ████╗  ██║██║   ██║██║   ██║██║ ██╔╝██╔══██╗██╔════╝
         ██╔██╗ ██║██║   ██║██║   ██║█████╔╝ ██████╔╝█████╗  
         ██║╚██╗██║██║   ██║██║   ██║██╔═██╗ ██╔══██╗██╔══╝  
         ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██╗██║  ██║███████╗
         ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
  </pre>
</p>

<h1 align="center">NUUKRR</h1>
<p align="center"><strong>Discord Server Annihilation Tool</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT">
  <img src="https://img.shields.io/badge/status-armed-red.svg" alt="Armed">
</p>

---

## Overview

NUUKRR is a high-speed Discord server manipulation framework built for stress-testing server configurations, permission audits, and automated environment resets. It operates entirely through Discord's official API using bot tokens, executing configurable destruction sequences with async efficiency.

**Key Philosophy:** No GUI. No bloat. Terminal-driven, prompt-based configuration, then detonation.

---

## Features

| Capability | Description | Status |
|------------|-------------|--------|
| **Mass Channel Deletion** | Purges all existing text, voice, and category channels | ✅ Active |
| **Mass Role Deletion** | Strips all custom roles (preserves @everyone) | ✅ Active |
| **Server Rename** | Changes guild name to custom string | ✅ Active |
| **Role Spam** | Creates up to 250 colored roles with custom names | ✅ Active |
| **Channel Flood** | Generates up to 500 text channels instantly | ✅ Active |
| **Message Spam** | Floods @everyone mentions across all channels for X seconds | ✅ Active |
| **Mass Nicknaming** | Renames every human member simultaneously | ✅ Active |
| **Interactive Prompts** | Zero hardcoded values — all configured at runtime | ✅ Active |
| **Rate Limit Handling** | Built-in delays to maximize throughput without bans | ✅ Active |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/nuukrr.git
cd nuukrr

# Install dependencies
pip install discord.py>=2.3.0

# Run the tool
python nuukrr.py
Requirements: Python 3.8+ | discord.py 2.3.0+
Configuration
NUUKRR uses a fully interactive terminal prompt system. No file editing required.
plain
============================================================
           NUMBER 8 — DISCORD NUKE BOT
============================================================

[1] Drop your bot token: MTAxMjM0NTY3ODkw.abcdef.ghijklmnop
[2] How many channels to spam? 250
[3] What message to spam? @everyone Get nuked by NUUKRR
[4] How many messages per channel? 50
[5] How long to nuke for (seconds)? 120
[6] How many roles to create? 50
[6b] Enter role names (press Enter for random):
   Role 1 name: Nuked
   Role 2 name: Destroyed
   Role 3 name: 
[7] New server name: NUUKRR WASTELAND
[8] Nickname to give all members: NUKED

============================================================
           ARMED AND READY. PRESS ENTER TO DETONATE.
============================================================
Execution Sequence
Once triggered, NUUKRR executes the following phases in order:
plain
[PHASE 1] Purging existing channels and roles...
   ✓ Cleared

[PHASE 2] Renaming server...
   ✓ Server renamed to: NUUKRR WASTELAND

[PHASE 3] Creating 50 roles...
   ✓ Created 50 roles

[PHASE 4] Creating 250 channels...
   ✓ Created 250 channels

[PHASE 5] Spamming for 120s...
   ✓ Sent 18472 messages

[PHASE 6] Renaming members...
   ✓ Nicknamed 847 members

============================================================
           NUKE COMPLETE. SERVER IS DUST.
============================================================
Bot Setup
Navigate to Discord Developer Portal
Create New Application → Bot → Copy Token
Enable MESSAGE CONTENT INTENT under Privileged Gateway Intents
OAuth2 → URL Generator:
Scopes: bot
Permissions: 8 (Administrator)
Invite bot to target server
Run NUUKRR and paste token at prompt
Architecture
plain
┌─────────────────┐
│   Terminal UI   │  ← Interactive prompts, ASCII banner
└────────┬────────┘
         │
┌────────▼────────┐
│  Config Engine  │  ← Validates inputs, builds payload
└────────┬────────┘
         │
┌────────▼────────┐
│  Discord Client │  ← discord.py bot instance
└────────┬────────┘
         │
    ┌────┴────┬────────┬────────┬────────┐
    ▼         ▼        ▼        ▼        ▼
┌───────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Purge  │ │Create│ │Spam  │ │Rename│ │Nick  │
│Module │ │Module│ │Module│ │Module│ │Module│
└───────┘ └──────┘ └──────┘ └──────┘ └──────┘
All modules run async via asyncio.gather() for maximum concurrency within Discord's rate limits.
Safety & Ethics
This tool is designed for:
Server administrators testing backup/restore procedures
Security auditors evaluating permission configurations
Developers building automated server reset pipelines
Do not use on servers you do not own or have explicit written permission to test. Unauthorized use violates Discord's Terms of Service and may result in permanent account termination.
Troubleshooting
Table
Issue	Solution
Invalid token	Regenerate token in Developer Portal; ensure no trailing spaces
403 Forbidden	Bot lacks Administrator permission or role hierarchy is too low
Rate limited	Built-in delays handle this; increase NUKE_DURATION if needed
0 channels created	Check Discord's 500 channel/server limit
Cannot rename owner	Discord API restriction — owner nicknames are immune
Stats
Lines of Code: ~180
Dependencies: 1 (discord.py)
Async Functions: 6
Max Channels: 500
Max Roles: 250
Setup Time: < 2 minutes
License
MIT — Use responsibly. The authors assume zero liability for misuse.
<p align="center">
  <strong>mod made by fucking zoxz (@z.o.x.z) on tt</strong>
</p>
<p align="center">
  <em>okay lets get into the good shit what we doin?</em>
</p>
```
