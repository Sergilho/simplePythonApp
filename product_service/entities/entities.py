from typing import List


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


# class ProductRepository:
#     def Add(self, product: Product) -> Product:
#         pass
#
#     def GetById(self, product_id: int) -> Product:
#         pass
#
#     def GetAll(self) -> List[Product]:
#         pass
#
#     def Update(self, product: Product) -> Product:
#         pass
#
#     def Delete(self, product_id: int) -> None:
#         pass
