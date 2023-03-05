import psycopg2
from typing import List

from product_service.entities.entities import Product


class ProductRepository(Product):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def Add(self, product: Product) -> Product:
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;
            """,
            (product.name, product.price)
        )
        product_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return Product(id=product_id, name=product.name, price=product.price)

    def GetById(self, product_id: int) -> Product | None:
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM products WHERE id = %s;
            """,
            (product_id,)
        )
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            return Product(id=result[0], name=result[1], price=result[2])

        return None

    def GetAll(self) -> List[Product]:
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM products;
            """
        )
        result = cur.fetchall()
        cur.close()
        conn.close()

        return [Product(id=row[0], name=row[1], price=row[2]) for row in result]
