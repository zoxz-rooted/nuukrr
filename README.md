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
python nuukrr.py

''ascii ▒███████▒ ▒█████  ▒██   ██▒▒███████▒
▒ ▒ ▒ ▄▀░▒██▒  ██▒▒▒ █ █ ▒░▒ ▒ ▒ ▄▀░
░ ▒ ▄▀▒░ ▒██░  ██▒░░  █   ░░ ▒ ▄▀▒░ 
  ▄▀▒   ░▒██   ██░ ░ █ █ ▒   ▄▀▒   ░
▒███████▒░ ████▓▒░▒██▒ ▒██▒▒███████▒
░▒▒ ▓░▒░▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▒▒ ▓░▒░▒
░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░░   ░▒ ░░░▒ ▒ ░ ▒
░ ░ ░ ░ ░░ ░ ░ ▒   ░    ░  ░ ░ ░ ░ ░
  ░ ░        ░ ░   ░    ░    ░ ░    
░                          ░        
''
