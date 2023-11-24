from functools import partial
from typing import Callable

ConversionFunction = Callable[[int], int]
ConversionRates = dict[str, float]

CONVERSION_RATES: ConversionRates = {
    "USD": 1.0,
    "EUR": 0.9,
    "JPY": 119.22,
    "GBP": 0.76,
    "CHF": 0.93,
    "AUD": 1.35,
    "CAD": 1.26,
}


def convert_to_currency(
    value: int, currency: str, conversion_rates: ConversionRates
) -> int:
    return value * conversion_rates[currency]


def multi_convert_currencies(
    value: int,
    currencies: list[str],
    conversion_functions: dict[str, ConversionFunction],
) -> dict[str, int]:
    return {currency: conversion_functions[currency](value) for currency in currencies}


def main():
    dollar_amount = 50_00
    print(f"Converting {dollar_amount/100:.2f} USD to EUR:")
    eur_amount = convert_to_currency(dollar_amount, "EUR", CONVERSION_RATES)
    print(f"{eur_amount/100:.2f} EUR")
    conversion_functions = {
        currency: partial(
            convert_to_currency, currency=currency, conversion_rates=CONVERSION_RATES
        )
        for currency in CONVERSION_RATES
    }
    conversion_functions_lambda = {
        currency: lambda value, rate=rate: value * rate
        for currency, rate in CONVERSION_RATES.items()
    }
    print(f"Converting {dollar_amount/100:.2f} USD to multiple currencies:")
    currencies = ["EUR", "JPY", "GBP", "CHF"]
    amounts = multi_convert_currencies(dollar_amount, currencies, conversion_functions)
    for currency, amount in amounts.items():
        print(f"{amount/100:.2f} {currency}")


if __name__ == "__main__":
    main()
