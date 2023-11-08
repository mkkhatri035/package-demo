from demo_module import Add

def test_ADD():
    assert isinstance(Add(0.1,22.0), float),"Test failed"
    
    print(Add(0.1,22.8))