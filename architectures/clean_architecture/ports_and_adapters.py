"""Ports and Adapters (Hexagonal): core use cases with swappable adapters."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class PaymentGateway(Protocol):      # driven port
    def charge(self, amount_minor: int) -> str: ...


class PaymentNotifier(Protocol):     # driven port
    def notify(self, message: str) -> None: ...


@dataclass
class Checkout:
    gateway: PaymentGateway
    notifier: PaymentNotifier

    def pay(self, amount_minor: int) -> str:
        reference = self.gateway.charge(amount_minor)
        self.notifier.notify(f"charged {amount_minor}: {reference}")
        return reference


class FakeGateway:                   # test adapter
    def charge(self, amount_minor: int) -> str:
        return f"fake-{amount_minor}"


class ConsoleNotifier:               # production or test adapter
    def notify(self, message: str) -> None:
        print(message)


if __name__ == "__main__":
    checkout = Checkout(FakeGateway(), ConsoleNotifier())
    print(checkout.pay(1999))
