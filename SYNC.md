# SYNC.md

## 目标

把对长期协作有价值的文件稳定同步到 GitHub，降低会话漂移和“失忆”风险，同时避免把本地运行状态、缓存、凭证和内部噪音推上远程。

## 默认纳入同步的文件

- `SOUL.md`
- `USER.md`
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`
- `AGENTS.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `IDENTITY.md`
- `SYNC.md`
- `.gitignore`

## 默认不纳入同步的内容

- `.openclaw/`
- `state/`
- `memory/.dreams/`
- 日志、缓存、临时文件
- 凭证、token、密钥、cookie 等敏感信息

## 同步原则

1. 只同步对长期协作有帮助的内容。
2. 修改文件、删除文件前，先征得用户确认。
3. 每次更新人设、偏好、长期记忆、重要工作记录后，优先本地提交。
4. 远程同步默认推送到工作分支 `openclaw-67`，避免直接扰动远程 `main`。
5. 若涉及隐私、账户、设备信息，先做筛查，再决定是否入库。

## 建议的定期同步机制

### 触发式同步
出现以下情况时，优先执行一次同步：
- 更新了 `SOUL.md`
- 更新了 `USER.md`
- 更新了 `MEMORY.md`
- 产生了新的 `memory/YYYY-MM-DD.md` 且包含重要信息
- 完成了关键配置或流程打通（例如飞书、GitHub 同步策略）

### 日常检查
建议每天至少检查一次以下文件是否有变化：
- `SOUL.md`
- `USER.md`
- `MEMORY.md`
- `memory/*.md`

若有重要变化，则：
1. 本地 commit
2. 推送到 `openclaw-67`
3. 需要时再创建或更新 PR

## 当前分支策略

- 本地工作分支：`openclaw-67`
- 远程工作分支：`openclaw-67`
