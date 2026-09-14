"""Capacity estimation helpers for system design interviews."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Capacity:
    daily_active_users: int
    requests_per_user_per_day: int
    avg_record_bytes: int

    @property
    def qps(self) -> float:
        return self.daily_active_users * self.requests_per_user_per_day / 86_400

    @property
    def peak_qps(self) -> float:
        return self.qps * 2  # rule of thumb: peak ~ 2x average

    @property
    def storage_per_day_gb(self) -> float:
        writes = self.daily_active_users * self.requests_per_user_per_day
        return writes * self.avg_record_bytes / 1e9

    @property
    def storage_per_year_tb(self) -> float:
        return self.storage_per_day_gb * 365 / 1000


def servers_needed(peak_qps: float, per_server_qps: float) -> int:
    return int(peak_qps / per_server_qps) + 1


if __name__ == "__main__":
    cap = Capacity(daily_active_users=10_000_000, requests_per_user_per_day=20, avg_record_bytes=500)
    assert 2_000 < cap.qps < 3_000
    assert cap.storage_per_day_gb > 0
    print(f"QPS={cap.qps:.0f} peak={cap.peak_qps:.0f} storage/day={cap.storage_per_day_gb:.1f} GB")
