import unittest

from service import ComputeRentalService


class ComputeRentalServiceTest(unittest.TestCase):
    def test_create_and_bill_rental(self) -> None:
        svc = ComputeRentalService()
        customer = svc.create_customer("Alice", "alice@example.com")
        rental = svc.create_rental(customer["customer_id"], "plan-a10")

        svc.start_rental(rental["rental_id"])
        stopped = svc.stop_rental(rental["rental_id"], hours="2.5")

        self.assertEqual(stopped["status"], "stopped")
        self.assertEqual(stopped["billed_hours"], "2.50")
        self.assertEqual(stopped["amount_due"], "21.25")

    def test_dashboard(self) -> None:
        svc = ComputeRentalService()
        customer = svc.create_customer("Bob", "bob@example.com")
        r1 = svc.create_rental(customer["customer_id"], "plan-4090")
        r2 = svc.create_rental(customer["customer_id"], "plan-a100")

        svc.start_rental(r1["rental_id"])
        svc.start_rental(r2["rental_id"])
        svc.stop_rental(r1["rental_id"], hours="1")

        panel = svc.dashboard()
        self.assertEqual(panel["customers"], 1)
        self.assertEqual(panel["orders"], 2)
        self.assertEqual(panel["running_instances"], 1)
        self.assertEqual(panel["stopped_instances"], 1)
        self.assertEqual(panel["estimated_revenue"], "18.80")


if __name__ == "__main__":
    unittest.main()
