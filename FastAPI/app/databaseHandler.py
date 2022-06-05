import psycopg2
import app.orm as orm


class DatabaseHandler:
    def __init__(self, db_name: str, db_user: str, db_pass: str, db_host: str = "localhost"):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_pass,
            host=self.db_host
        )
        self.cursor = self.connection.cursor()

    # Account ------------------------------------------------------------------------------------------------------------

    def createAccount(self, account: orm.user_account) -> None:
        if account.sir_name is None and account.last_name is None:
            self.cursor.execute('''INSERT INTO user_account (account_id, login, passwd) VALUES (%s, %s, %s)''',
                                (account.account_id, account.login, account.passwd))
        elif account.sir_name is None:
            self.cursor.execute('''INSERT INTO user_account (account_id, login, passwd, last_name) VALUES (%s, %s, %s, %s)''',
                                (account.account_id, account.login, account.passwd, account.last_name))
        elif account.last_name is None:
            self.cursor.execute('''INSERT INTO user_account (account_id, login, passwd, sir_name) VALUES (%s, %s, %s, %s)''',
                                (account.account_id, account.login, account.passwd, account.sir_name))
        else:
            self.cursor.execute('''INSERT INTO user_account (account_id, login, passwd, sir_name, last_name) VALUES (%s, %s, %s, %s, %s)''',
                                (account.account_id, account.login, account.passwd, account.sir_name, account.last_name))
        self.connection.commit()

    def deleteAccount(self, account_id: int):
        self.cursor.execute(
            '''DELETE FROM user_account WHERE account_id = %s''', (account_id,))
        self.connection.commit()

    # Device ------------------------------------------------------------------------------------------------------------

    def createDevice(self, device: orm.device) -> None:
        self.cursor.execute('''INSERT INTO device (device_id, device_name) VALUES (%s, %s)''',
                            (device.device_id, device.device_name))
        self.connection.commit()

    def renameDevice(self, device: orm.device) -> None:
        self.cursor.execute('''UPDATE device SET device_name = %s WHERE device_id = %s''',
                            (device.device_name, device.device_id))
        self.connection.commit()

    def deleteDevice(self, device_id: int) -> None:
        self.cursor.execute(
            '''DELETE FROM device WHERE device_id = %s''', (device_id,))
        self.connection.commit()

    def connectDevice(self, account_device_relation: orm.account_device_relation) -> None:
        self.cursor.execute('''INSERT INTO account_device_relation (account_id, device_id) VALUES (%s, %s)''',
                            (account_device_relation.account_id, account_device_relation.device_id))
        self.connection.commit()

    def disconnectDevice(self, account_device_relation: orm.account_device_relation) -> None:
        self.cursor.execute('''DELETE FROM account_device_relation WHERE account_id = %s AND device_id = %s''',
                            (account_device_relation.account_id, account_device_relation.device_id))
        self.connection.commit()

    # Product ------------------------------------------------------------------------------------------------------------

    def createProduct(self, product: orm.product) -> None:
        if product.barcode_id is None:
            self.cursor.execute('''INSERT INTO product (product_id, product_name) VALUES (%s, %s)''',
                                (product.product_id, product.product_name))
        else:
            self.cursor.execute('''INSERT INTO product (product_id, product_name, barcode_id) VALUES (%s, %s, %s)''',
                                (product.product_id, product.product_name, product.barcode_id))
        self.connection.commit()

    def renameProduct(self, product: orm.product) -> None:
        self.cursor.execute('''UPDATE product SET product_name = %s WHERE product_id = %s''',
                            (product.product_name, product.product_id))
        self.connection.commit()

    def deleteProduct(self, product_id: int) -> None:
        self.cursor.execute(
            '''DELETE FROM product WHERE product_id = %s''', (product_id,))
        self.connection.commit()

    def fillProduct(self, device_content: orm.device_content) -> None:
        self.cursor.execute('''INSERT INTO device_content (device_id, product_id) VALUES (%s, %s)''',
                            (device_content.device_id, device_content.product_id))
        self.connection.commit()

    def dropProduct(self, device_content: orm.device_content) -> None:
        self.cursor.execute('''UPDATE device_content SET dropped_out = NOW() WHERE device_id = %s AND product_id = %s''',
                            (device_content.device_id, device_content.product_id))
        self.connection.commit()

    # Categories ------------------------------------------------------------------------------------------------------------

    def createCategory(self, category: orm.product_category) -> None:
        self.cursor.execute('''INSERT INTO category (category_id, category_name) VALUES (%s, %s)''',
                            (category.category_id, category.category_name))
        self.connection.commit()

    def renameCategory(self, category: orm.product_category) -> None:
        self.cursor.execute('''UPDATE category SET category_name = %s WHERE category_id = %s''',
                            (category.category_name, category.category_id))
        self.connection.commit()

    def deleteCategory(self, category_id: int) -> None:
        self.cursor.execute(
            '''DELETE FROM category WHERE category_id = %s''', (category_id,))
        self.connection.commit()

    def categorizeProduct(self, product_category_relation: orm.product_category_relation) -> None:
        self.cursor.execute('''INSERT INTO product_category_relation (product_id, category_id) VALUES (%s, %s)''',
                            (product_category_relation.product_id, product_category_relation.category_id))
        self.connection.commit()

    def uncategorizeProduct(self, product_category_relation: orm.product_category_relation) -> None:
        self.cursor.execute('''DELETE FROM product_category_relation WHERE product_id = %s AND category_id = %s''',
                            (product_category_relation.product_id, product_category_relation.category_id))
        self.connection.commit()

    # Units ------------------------------------------------------------------------------------------------------------

    def createUnit(self, unit: orm.unit) -> None:
        self.cursor.execute('''INSERT INTO unit (unit_id, unit_symbol) VALUES (%s, %s)''',
                            (unit.unit_id, unit.unit_symbol))
        self.connection.commit()

    def updateUnitSymbol(self, unit: orm.unit) -> None:
        self.cursor.execute('''UPDATE unit SET unit_symbol = %s WHERE unit_id = %s''',
                            (unit.unit_symbol, unit.unit_id))
        self.connection.commit()

    def deleteUnit(self, unit_id: int) -> None:
        self.cursor.execute('''DELETE FROM unit WHERE unit_id = %s''',
                            (unit_id,))
        self.connection.commit()
