from snake import Snake

def test_move():
    s = Snake()
    old_head = s.body[0]
    s.move()
    assert s.body[0] != old_head

def test_growth():
    s = Snake()
    s.grow()
    s.move()
    assert len(s.body) == 2