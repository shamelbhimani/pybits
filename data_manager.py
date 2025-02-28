"""
Some docstring to be filled out later
"""

import hashlib
import json


class MemoryManager:
    """
    Handles pseudo-memory storage and ID generation for datasets.
    """
    _memory = {}

    @staticmethod
    def generate_id(data: list) -> str:
        """Generates a unique SHA-256 hash ID for a dataset.

        Parameters:
            data: list
                A list of numerical values.

        Returns:
            str
            A unique SHA-256 hash ID for the dataset.
        """
        standardized_data = tuple(sorted(data))
        data_string = json.dumps(standardized_data)

        # Generate SHA-256 Hash
        hash_object = hashlib.sha256(data_string.encode())
        unique_id = hash_object.hexdigest()

        return unique_id

    @classmethod
    def store_statistics(cls, data: list, stats: dict) -> str:
        """
        Stores computed information for a given dataset a with a given unique_id x.
        If the dataset already exists, it returns the existing id.

        Parameters:
            data: list
                The dataset for which statistics are computed
            stats: dict
                The computer statistics to store

        Returns
        str
            The unique ID associated with the datset
        """
        unique_id = cls.generate_id(data)

        if unique_id not in cls._memory:
            cls._memory[unique_id] = stats

        return unique_id

    @classmethod
    def retrieve_statistics(cls, unique_id: str) -> dict:
        """

        :param cls:
        :param unique_id:
        :return:
        """
        return cls._memory.get(unique_id, {})
