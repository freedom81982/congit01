# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Web Backends

- 顺客云后台 → https://bss.aywcloud.com/login?redirect=/index
  - 默认优先用 OpenClaw 受控 Chrome 打开与操作
  - 用途：查看今日收入、订单与运营数据

## Image Generation

- ComfyUI 局域网后端 → http://192.168.210.3:8000
  - 当前已确认可从这台 Mac 访问 `/` 与 `/system_stats`
  - 用途：后续供 `portrait-gen` 走人物图、头像、形象照生成
  - 备注：若再次连不上，先检查目标电脑 IP 是否变化、防火墙、以及桌面客户端是否仍监听局域网
