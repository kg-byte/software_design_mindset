from functools import partial
from typing import Callable

CONVERSION_RATES = {
    "USD": 1.0,
    "EUR": 0.9,
    "JPY": 1.2,
    "GBP": 0.8,
    "CHF": 1.1,
    "AUD": 1.3,
    "CAD": 1.5,
}


def convert_to_currency(
    value: int, currency: str, conversion_rates: dict[str, int]
) -> int:
    return value * conversion_rates[currency]


def multi_convert_currencies(
    value: int,
    currencies: list[str],
    conversion_functions: dict[str, Callable[[int], int]],
) -> dict[str, int]:
    return {currency: conversion_functions[currency](value) for currency in currencies}


def main():
    dollar_amount = 50_00
    print(f"Converting ${dollar_amount/100:.2f} USD to EUR:")
    eur_amount = convert_to_currency(dollar_amount, "EUR", CONVERSION_RATES)
    print(f"{eur_amount/100:.2f} EUR")
    conversion_functions = {
        currency: partial(
            convert_to_currency, currency=currency, conversion_rates=CONVERSION_RATES
        )
        for currency in CONVERSION_RATES
    }
    print(f"Converting ${dollar_amount/100:.2f} USD to EUR and JPY:")
    currencies = ["EUR", "JPY"]
    amounts = multi_convert_currencies(dollar_amount, currencies, conversion_functions)
    for currency, amount in amounts.items():
        print(f"{amount/100:.2f} {currency}")


if __name__ == "__main__":
    main()
