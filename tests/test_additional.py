from src.sample_module import greet

def test_greet_upper():
    assert greet("test").isupper() == False
