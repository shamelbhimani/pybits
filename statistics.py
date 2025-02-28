"""
Statistics and Probability Utilities
====================================

This module provides a collection of statistical and probability functions
that aid in understanding and applying fundamental statistical concepts.
It is designed to be used as an importable package, leveraging a hybrid
of object-oriented and functional programming.

Key Features:
- Descriptive statistics (mean, variance, standard deviation, etc.)
- Probability distributions (normal, binomial, Poisson, etc.)
- Hypothesis testing (t-tests, chi-square tests, etc.)
- Regression analysis (simple and multiple linear regression)
- Causal inference methods inspired by *Causal Inference: The Mixtape*

This module follows PEP 8 formatting and includes:
- Static analysis using PythonTA (`python_ta`)
- Runtime contract checks using `contracts`
- Strict type hints for improved readability

MIT License
-----------
Copyright (c) 2025 Shamel Bhimani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import List, Union
import logging
import pytest
import warnings
import python_ta
from abc import ABC, abstractmethod
from data_manager import MemoryManager


class Statistics:
    """
    A class for performing basic statistical calculations.

    This class provides methods for computing measures of central tendency and
    dispersion, formatted using f-strings for readability.
    """

    def __init__(self, data: list[Union[int, float]]):
        """
        Initializes the Statistics object with a dataset.

        Parameters:
            data: list[Union[int, float]]
                A list of numerical values

        Raises:
            ValueError
                If the list is empty.
        """
        if not data:
            raise ValueError("List cannot be empty")

        self.data = data
        self.results = {}

    def __str__(self) -> str:
        """
        Returns a string representation of the computed statistics.

        Returns:
            str
                A formatted string displaying the statistical results
        """
        if not self.results:
            return "No computed statistics."

        return "\n".join([f"{key}: {value:.2f}"
                         f"" for key, value in self.results.items()])

    def sample_mean(self) -> float:
        """Calculates the mean or average of a given list of integers or floats.

        Returns:
            str
                The sample mean formatted as an f-string.
        """
        # Error Handling: Checks if the list is empty and raises a ValueError.
        mean = sum(self.data) / len(self.data)

        return mean


if __name__ == "__main__":
    a = Statistics([1, 2, 3])
    a.sample_mean()
