from functools import reduce

class Property:
    def __init__(self, prop_id, address, price_bill_vnd, sqm):
        if prop_id > 0 and price_bill_vnd > 0 and sqm > 0:
            self.prop_id = prop_id
            self.address = address
            self.price_bill_vnd = price_bill_vnd
            self.sqm = sqm
            print(f"System: [ID: {prop_id}] at [Address: {address}] successfully constructed.")
        else:
            print(f"System: [ID: {prop_id}] not found.")

    def display_metrics(self):
        result = self.price_bill_vnd / self.sqm
        print(f"ID: {self.prop_id} | Listing: {self.address} | Price: {result} billion VND per square meters.")

    def is_affordable(self, budget):
        if budget > self.price_bill_vnd:
            is_affordable = True
            print("You can afford this property.")
        else:
            is_affordable = False
            print("Insufficient budget.")
        return is_affordable
    def update_price(self, new_price):
        self.price_bill_vnd = new_price
        print(f"ID {self.prop_id} price updated to {new_price} billion VND.")
    def is_larger_than(self, propertyy):
        return self.sqm > propertyy.sqm
class Apartment(Property):
    def __init__(self, prop_id, address, price_bill_vnd, sqm, floor_level):
        super().__init__(prop_id, address, price_bill_vnd, sqm)
        self.floor_level = floor_level

    def get_actual_area(self):
        return self.sqm * 1.05

    def display_listings(self):
        bonus_area = self.get_actual_area()
        print(f"[APT] ID: {self.prop_id} |  {self.address} | {self.price_bill_vnd}B VND | Area: {bonus_area:.2f} sqm | Floor {self.floor_level}")
class Villa(Property):
    def __init__(self, prop_id, address, price_bill_vnd, sqm, has_pool):
        super().__init__(prop_id, address, price_bill_vnd, sqm)
        self.has_pool = has_pool

    def calculate_maintenance(self):
        return self.price_bill_vnd * 0.005

    def display_listings(self):
        bills = self.calculate_maintenance()
        print(f"[VILLA] ID: {self.prop_id} | {self.address} | {self.price_bill_vnd}B VND | Pool: {self.has_pool} | Maintenance: {bills:.2f}B VND")

    def add_pool(self):
        self.has_pool = True
class Penthouse(Property):
    def __init__(self, prop_id, address, price_bill_vnd, sqm, has_private_elevator):
        super().__init__(prop_id, address, price_bill_vnd, sqm)
        self.has_private_elevator = has_private_elevator

    def get_taxed_price(self):
        return self.price_bill_vnd * 1.1

    def display_listings(self):
        tax = self.get_taxed_price()
        print(f"[PENTHOUSE] ID: {self.prop_id} | Elevator: {self.has_private_elevator} | Total Price (with Tax): {tax:.2f}B VND | {self.address}")
def generate_market_report(listings):
    sum_value = 0
    for i in listings:
        i.display_listings()
        sum_value += i.price_bill_vnd
    print(f"Total Market Value: {sum_value:.2f}B VND")
def villa_inspection(listings):
    for l in listings:
        if isinstance(l, Villa):
            print(f"--- Inspection Required for Pool at Property {l.prop_id} ---")
        else:
            print(f"--- Property {l.prop_id} does not require pool inspection ---")
p1 = Apartment(201, "Ocean Park, Gia Lam", 3.1, 55, 15)
p1.display_listings()
p2 = Villa(301, "Vinhomes Riverside", 35.0, 300, True)
p2.display_listings()
p3 = Penthouse(401, "Keangnam Landmark 72", 15.5, 250, True)
p3.display_listings()
market_dashboard = [
    Apartment(201, "Ocean Park, Gia Lam", 3.1, 55, 15),
    Apartment(202, "Times City", 4.5, 75, 20),
    Villa(301, "Vinhomes Riverside", 35.0, 300, True),
    Villa(302, "Ciputra Hanoi", 42.0, 450, False),
    Penthouse(401, "Keangnam Landmark 72", 15.5, 250, True),
    Penthouse(402, "Lotte Center", 18.0, 280, True)
]
generate_market_report(market_dashboard)
villa_inspection(market_dashboard)
villa = market_dashboard[3]
villa.display_listings()
villa.add_pool()
villa.display_listings()




best_value_properties = list(filter(lambda x: x.price_bill_vnd < 10.0 and x.sqm > 60, market_dashboard))
for prop in best_value_properties:
    prop.display_listings()

analysis_list = list(map(lambda x: f"[ID: {x.prop_id}] at [{x.address}] | Unit Price: {x.price_bill_vnd / x.sqm:.4f}B per sqm", market_dashboard))
for analysis in analysis_list:
    print(analysis)

market_leader = reduce(lambda x, y: x if x.price_bill_vnd > y.price_bill_vnd else y, market_dashboard)
market_leader.display_listings()

sorted_by_size = sorted(market_dashboard, key=lambda x: x.sqm, reverse=True)
for prop in sorted_by_size:
    print(f"ID: {prop.prop_id} | Address: {prop.address} | Size: {prop.sqm} sqm")

def make_currency_converter(exchange_rate):
    def converter(price):
        return price * 1000000 * exchange_rate
    return converter
to_usd = make_currency_converter(1 / 25000)
to_euro = make_currency_converter(1 / 27000)
penthouse_price = p3.price_bill_vnd
price_usd = to_usd(penthouse_price)
price_eur = to_euro(penthouse_price)

print(f"penthouse original price: {penthouse_price}B VND")
print(f"USD: {price_usd:.6f} Billion USD")
print(f"EUR: {price_eur:.6f} Billion EUR")

projected_market = [
    {"ID": prop.prop_id, "Taxed_Price in billion VND": round(prop.price_bill_vnd * 1.1, 2)}
    for prop in market_dashboard
    if isinstance(prop, (Apartment, Penthouse))
]
for item in projected_market:
    print(item)

def audit_log(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"[LOG] Executing: {func_name}...")
        result = func(*args, **kwargs)
        print(f"[LOG] {func_name} complete.")
        return result
    return wrapper
def update_listing_status(prop_id, status):
    print(f"Property {prop_id} status updated to: {status}")
update_listing_status(202, "SOLD")
update_listing_status(401, "UNDER CONTRACT")