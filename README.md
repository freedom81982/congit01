# 算力租赁后台 Demo

一个可直接运行的 Python 后台 Demo，模拟「算力套餐管理、客户建档、订单启动/停止、按小时计费、运营看板」等核心能力。

## 功能

- 预置 3 种算力套餐（A10/A100/4090）。
- 创建客户。
- 创建租赁订单。
- 启动/停止实例并按小时计费。
- 查看订单列表与运营看板（客户数、运行中实例、营收）。

## 快速启动

```bash
python server.py
```

服务默认监听：`http://127.0.0.1:8000`

## API 示例

### 1) 查询套餐

```bash
curl http://127.0.0.1:8000/api/v1/plans
```

### 2) 创建客户

```bash
curl -X POST http://127.0.0.1:8000/api/v1/customers \
  -H 'Content-Type: application/json' \
  -d '{"name":"张三","email":"zhangsan@example.com"}'
```

### 3) 创建租赁订单

```bash
curl -X POST http://127.0.0.1:8000/api/v1/rentals \
  -H 'Content-Type: application/json' \
  -d '{"customer_id":"cus_xxx","plan_id":"plan-a10"}'
```

### 4) 启动订单

```bash
curl -X POST http://127.0.0.1:8000/api/v1/rentals/ord_xxx/start
```

### 5) 停止并计费（传 hours）

```bash
curl -X POST 'http://127.0.0.1:8000/api/v1/rentals/ord_xxx/stop?hours=2.5'
```

### 6) 查看看板

```bash
curl http://127.0.0.1:8000/api/v1/dashboard
```

## 测试

```bash
python -m unittest discover -s tests -v
```
