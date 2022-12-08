import pytest
from grade_boundries import calc_grade


# Normal tests
def test_calc_grade():
    assert calc_grade(6) == "U"
    assert calc_grade(250) == "D"


# Boundary tests
test_data = [(0, 'U'),
             (72, 'E'),
             (111, 'D'),
             (150, 'C'),
             (189, 'B'),
             (229, 'A'),
             (264, 'A*'),
             ]


@pytest.mark.parametrize('score, grade', test_data)
def test_calc_grade_min_boundary(score, grade):
    assert calc_grade(score) == grade
