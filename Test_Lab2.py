import Lab2
print("Test_Lab2")

def test_find_min_max():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_result = [11, 90]
    result = Lab2.find_min_max(input_arr)
    assert (result == expected_result)

def test_calc_average():
    result = []
    input_arr = [10, 20, 30, 40]
    expected_result = 25
    result = Lab2.calc_average(input_arr)
    assert (result == expected_result)

def test_calc_median_temp():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_result = 25
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == expected_result)