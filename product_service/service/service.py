from typing import List
from product_service.entities.entities import Product
from product_service.repository import ProductRepository


class ProductService:
    def __init__(self, connection_string: str):
        self.product_repository = ProductRepository(connection_string)

    def Put(self, product: Product) -> Product:
        return self.product_repository.Add(product)

    def GetById(self, product_id: int) -> Product:
        return self.product_repository.GetById(product_id)

    def GetAll(self) -> List[Product]:
        return self.product_repository.GetAll()
