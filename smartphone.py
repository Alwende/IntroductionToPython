class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours battery life"

class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, strap_material):
        super().__init__(brand, model, storage, battery_life)
        self.strap_material = strap_material

    def track_steps(self, steps):
        print(f"Tracking {steps} steps on {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, {self.battery_life} hours battery life, and {self.strap_material} strap"

# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 13", 128, 20)
    phone2 = Smartphone("Samsung", "Galaxy S21", 256, 22)

    print(phone1)
    print(phone2)

    phone1.make_call("123-456-7890")
    phone2.send_message("987-654-3210", "Hello!")

    watch1 = Smartwatch("Apple", "Apple Watch Series 7", 32, 18, "Silicone")
    watch2 = Smartwatch("Samsung", "Galaxy Watch 4", 16, 20, "Leather")

    print(watch1)
    print(watch2)

    watch1.track_steps(5000)
    watch2.make_call("123-456-7890")