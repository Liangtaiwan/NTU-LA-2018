from ..has_cycle import has_cycle


def test_case1():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][1] = 1
    set_[0][2] = -1
    set_[1][0] = 1
    set_[1][1] = -1
    set_[2][2] = 1
    set_[2][0] = -1
    set_[3][3] = 1
    set_[3][1] = -1
    assert(has_cycle(set_))


def test_case2():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[0][0] = -1
    set_[1][0] = 1
    set_[1][1] = -1
    set_[2][1] = 1
    set_[2][2] = -1
    set_[3][1] = 1
    set_[3][3] = -1
    assert(has_cycle(set_))


def test_case3():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[0][0] = -1
    set_[1][3] = 1
    set_[1][2] = -1
    set_[2][1] = 1
    set_[2][3] = -1
    set_[3][1] = 1
    set_[3][2] = -1
    assert(not has_cycle(set_))


def test_case4():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[2][1] = 1
    set_[1][0] = 1
    set_[0][2] = 1
    set_[1][3] = 1
    assert(has_cycle(set_))


def test_case5():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[1][0] = 1
    set_[2][1] = 1
    set_[3][1] = 1
    assert(has_cycle(set_))


def test_case6():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[2][3] = 1
    set_[3][1] = 1
    set_[2][1] = 1
    assert(not has_cycle(set_))


def test_case7():
    set_ = []
    for n in range(5):
        set_.append([0] * 4)
    set_[0][3] = 1
    set_[0][2] = -1
    set_[1][0] = 1
    set_[1][1] = -1
    set_[2][2] = 1
    set_[2][0] = -1
    set_[3][3] = 1
    set_[3][1] = -1
    set_[4][3] = 1
    set_[4][0] = -1
    assert(not has_cycle(set_))


def test_case8():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[0][0] = -1
    set_[1][0] = 1
    set_[1][1] = -1
    set_[2][1] = 1
    set_[2][2] = -1
    set_[3][1] = 1
    set_[3][3] = -1
    assert(has_cycle(set_))


def test_case9():
    set_ = []
    for n in range(4):
        set_.append([0] * 4)
    set_[0][2] = 1
    set_[0][0] = -1
    set_[1][3] = 1
    set_[1][2] = -1
    set_[2][1] = 1
    set_[2][3] = -1
    set_[3][1] = 1
    set_[3][2] = -1
    assert(not has_cycle(set_))
