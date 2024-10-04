from my_lib import bubble_sort

def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
