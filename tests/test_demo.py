from src.sample_module import greet

def test_greet():
    assert greet("GitHub") == "Hello, GitHub"
