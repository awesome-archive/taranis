# Copyright (C) 2019 Pierre Letessier
# This source code is licensed under the BSD 3 license found in the
# LICENSE file in the root directory of this source tree.
"""
AbstractDatabaseRepository
"""
from utils.singleton import Singleton


class AbstractDatabaseRepository(metaclass=Singleton):
    # instance = None
    #
    # def __new__(cls, *args, **kargs):
    #     if cls.instance is None:
    #         cls.instance = object.__new__(cls, *args, **kargs)
    #     return cls.instance

    # @abstractmethod
    def get_all_databases(self) -> list:
        pass

    # @abstractmethod
    def create_one_database(self, database) -> str:
        pass

    # @abstractmethod
    def find_one_database_by_name(self, name: str) -> dict:
        pass

    # @abstractmethod
    def delete_one_database_by_name(self, name: str) -> bool:
        pass

    # @abstractmethod
    def delete_vectors_by_database_name(self, name: str) -> bool:
        pass

    # @abstractmethod
    def create_vectors(self, vectors: []) -> bool:
        pass

    # @abstractmethod
    def get_vectors(self, db_name: str, ids: []) -> list:
        pass

    # @abstractmethod
    def create_one_index(self, index) -> str:
        pass

    # @abstractmethod
    def delete_one_index(self, index) -> bool:
        pass
