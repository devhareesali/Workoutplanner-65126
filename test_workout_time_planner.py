import pytest
from workout_time_planner import calculate_bmi, get_recommendation

# --------- Tests for BMI Calculation ---------
def test_calculate_bmi_normal():
    assert calculate_bmi(70, 175) == 22.86

def test_calculate_bmi_edge_cases():
    assert calculate_bmi(50, 170) == 17.3
    assert calculate_bmi(80, 170) == 27.68

def test_calculate_bmi_invalid_values():
    with pytest.raises(ValueError):
        calculate_bmi(0, 175)
    with pytest.raises(ValueError):
        calculate_bmi(-70, 180)

# --------- Tests for Recommendation Logic ---------
def test_get_recommendation_underweight():
    category, workout, diet = get_recommendation(17.0)
    assert category == "Underweight"
    assert "light exercise" in workout.lower()
    assert "protein" in diet.lower()

def test_get_recommendation_healthy():
    category, workout, diet = get_recommendation(22.0)
    assert category == "Healthy"

def test_get_recommendation_overweight():
    category, workout, diet = get_recommendation(27.5)
    assert category == "Overweight"

def test_get_recommendation_obese():
    category, workout, diet = get_recommendation(35.0)
    assert category == "Obese"
