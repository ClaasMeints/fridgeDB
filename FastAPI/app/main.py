from fastapi import FastAPI

from app.databaseHandler import DatabaseHandler
from app.orm import user_account, account_device_relation, device, device_content, product, product_category_relation, product_category, unit, unit_conversion

app = FastAPI()
db: DatabaseHandler = DatabaseHandler(
    'fridgedb', 'docker', 'docker')


@app.post("/user_account")
def create_user_account(user_account: user_account):
    db.createUserAccount(user_account)


@app.delete("/user_account/{account_id}")
def delete_user_account(account_id: int):
    db.deleteUserAccount(account_id)


@app.post("/device")
def create_device(device: device):
    db.createDevice(device)


@app.put("/device")
def rename_device(device: device):
    db.renameDevice(device)


@app.delete("/device/{device_id}")
def delete_device(device_id: int):
    db.deleteDevice(device_id)


@app.post("/account_device_relation")
def connect_device(account_device_relation: account_device_relation):
    db.connectDevice(account_device_relation)


@app.delete("/account_device_relation")
def disconnect_device(account_device_relation: account_device_relation):
    db.disconnectDevice(account_device_relation)


@app.post("/product")
def create_product(product: product):
    db.createProduct(product)


@app.put("/product")
def rename_product(product: product):
    db.renameProduct(product)


@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    db.deleteProduct(product_id)


@app.post("/device_content")
def fillProduct(device_content: device_content):
    db.fillProduct(device_content)


@app.put("/device_content")
def dropProduct(device_content: device_content):
    db.dropProduct(device_content)


@app.post("/product_category")
def create_product_category(product_category: product_category):
    db.createProductCategory(product_category)


@app.put("/product_category")
def rename_product_category(product_category: product_category):
    db.renameProductCategory(product_category)


@app.delete("/product_category/{product_category_id}")
def delete_product_category(product_category_id: int):
    db.deleteProductCategory(product_category_id)


@app.post("/product_category_relation")
def categorize_product(product_category_relation: product_category_relation):
    db.categorizeProduct(product_category_relation)


@app.delete("/product_category_relation")
def uncategorize_product(product_category_relation: product_category_relation):
    db.uncategorizeProduct(product_category_relation)


@app.post("/unit")
def create_unit(unit: unit):
    db.createUnit(unit)


@app.put("/unit")
def rename_unit(unit: unit):
    db.renameUnit(unit)


@app.delete("/unit/{unit_id}")
def delete_unit(unit_id: int):
    db.deleteUnit(unit_id)
