from reward_value import RewardValue

def test_to_airline_miles():
    reward = RewardValue(100)  # 100 dollars
    assert reward.to_airline_miles() == 1000  # Expecting 1000 miles

if __name__ == "__main__":
    test_to_airline_miles()
    print("All tests passed!")
    