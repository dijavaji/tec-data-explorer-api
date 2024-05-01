from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}})
products_list=["1","2","3"]
#products_list= {"user1":{id: 1, "name":"iphone", "value":500, "type":"movil"},
                #"user2": {id: 2,"name":"tv LG", "value":300, "type":"tv"} }

@router.get("/")
async def products():
    return products_list

# http://127.0.0.1:8000/products/0
@router.get("/{id}")
async def productsId(id: int):
    return products_list[id]