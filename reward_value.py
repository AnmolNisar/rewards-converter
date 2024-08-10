class RewardValue:
    def __init__(self, cash_value):
        self.cash_value = cash_value

    def to_airline_miles(self):
        # Example conversion rate: 1 dollar = 10 airline miles
        conversion_rate = 10
        return self.cash_value * conversion_rate