from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List
import uuid


@dataclass
class Plan:
    plan_id: str
    name: str
    gpu_model: str
    vcpu: int
    memory_gb: int
    storage_gb: int
    hourly_price: Decimal


@dataclass
class Customer:
    customer_id: str
    name: str
    email: str
    created_at: str


@dataclass
class Rental:
    rental_id: str
    customer_id: str
    plan_id: str
    status: str
    started_at: str | None
    stopped_at: str | None
    billed_hours: Decimal
    amount_due: Decimal


class ComputeRentalService:
    def __init__(self) -> None:
        self.plans: Dict[str, Plan] = {
            "plan-a10": Plan("plan-a10", "A10 入门", "NVIDIA A10", 8, 32, 200, Decimal("8.50")),
            "plan-a100": Plan("plan-a100", "A100 训练", "NVIDIA A100", 24, 128, 1000, Decimal("42.00")),
            "plan-4090": Plan("plan-4090", "4090 推理", "RTX 4090", 16, 64, 500, Decimal("18.80")),
        }
        self.customers: Dict[str, Customer] = {}
        self.rentals: Dict[str, Rental] = {}

    @staticmethod
    def _now() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def _ts(dt: datetime | None) -> str | None:
        return dt.isoformat() if dt else None

    @staticmethod
    def _money(value: Decimal) -> Decimal:
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def create_customer(self, name: str, email: str) -> Dict:
        customer = Customer(
            customer_id=f"cus_{uuid.uuid4().hex[:10]}",
            name=name,
            email=email,
            created_at=self._ts(self._now()) or "",
        )
        self.customers[customer.customer_id] = customer
        return asdict(customer)

    def list_plans(self) -> List[Dict]:
        rows = []
        for plan in self.plans.values():
            row = asdict(plan)
            row["hourly_price"] = str(plan.hourly_price)
            rows.append(row)
        return rows

    def create_rental(self, customer_id: str, plan_id: str) -> Dict:
        if customer_id not in self.customers:
            raise ValueError("客户不存在")
        if plan_id not in self.plans:
            raise ValueError("套餐不存在")

        rental = Rental(
            rental_id=f"ord_{uuid.uuid4().hex[:10]}",
            customer_id=customer_id,
            plan_id=plan_id,
            status="pending",
            started_at=None,
            stopped_at=None,
            billed_hours=Decimal("0"),
            amount_due=Decimal("0"),
        )
        self.rentals[rental.rental_id] = rental
        return self._serialize_rental(rental)

    def start_rental(self, rental_id: str) -> Dict:
        rental = self._get_rental(rental_id)
        if rental.status not in {"pending", "stopped"}:
            raise ValueError("当前状态不可启动")
        rental.status = "running"
        rental.started_at = self._ts(self._now())
        rental.stopped_at = None
        return self._serialize_rental(rental)

    def stop_rental(self, rental_id: str, hours: str | None = None) -> Dict:
        rental = self._get_rental(rental_id)
        if rental.status != "running":
            raise ValueError("仅运行中的实例可以停止")
        runtime_hours = Decimal(hours) if hours else Decimal("1")
        if runtime_hours <= 0:
            raise ValueError("计费时长必须大于 0")

        plan = self.plans[rental.plan_id]
        rental.status = "stopped"
        rental.stopped_at = self._ts(self._now())
        rental.billed_hours += runtime_hours
        rental.amount_due = self._money(rental.amount_due + runtime_hours * plan.hourly_price)
        return self._serialize_rental(rental)

    def list_rentals(self) -> List[Dict]:
        return [self._serialize_rental(rental) for rental in self.rentals.values()]

    def dashboard(self) -> Dict:
        running = sum(1 for r in self.rentals.values() if r.status == "running")
        stopped = sum(1 for r in self.rentals.values() if r.status == "stopped")
        total_revenue = self._money(sum((r.amount_due for r in self.rentals.values()), start=Decimal("0")))
        return {
            "customers": len(self.customers),
            "orders": len(self.rentals),
            "running_instances": running,
            "stopped_instances": stopped,
            "estimated_revenue": str(total_revenue),
        }

    def _get_rental(self, rental_id: str) -> Rental:
        rental = self.rentals.get(rental_id)
        if not rental:
            raise ValueError("订单不存在")
        return rental

    def _serialize_rental(self, rental: Rental) -> Dict:
        row = asdict(rental)
        row["billed_hours"] = str(self._money(rental.billed_hours))
        row["amount_due"] = str(self._money(rental.amount_due))
        return row
