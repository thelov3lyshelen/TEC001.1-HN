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

mock_database = [Property(103, "88 Tay Ho Rd", 12.0, 120), Property(104, "5 Nguyen Trai", 3.2, 50), Property(101, "12A Cau Giay St", 4.5, 65)]
for property in mock_database:
    property.display_metrics()
for property1 in mock_database:
    increased_price = property1.price_bill_vnd * 1.10
    property1.update_price(increased_price)
mock_database[2].display_metrics()
nguyentrai = mock_database[1]
tayho = mock_database[0]

#favorite = mock_database[2]
#print("Deep Introspection begins.")
#rint(type(favorite))
#print(dir(favorite))
#print("Saving data...")
#print(favorite.__dict__)

# comparison = tayho.is_larger_than(nguyentrai)
# print(f"Is ID 103 larger than ID 104? {comparison}")

# p1 = Property(101, "12A Cau Giay St", 4.5, 65)
# p2 = Property(102, "Unknown Alley", -1.0, 0)
# p1.display_metrics()
# print(p1.is_affordable(5.0))