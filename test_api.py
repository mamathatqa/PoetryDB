from dotenv import load_dotenv
import pytest
import requests
import json
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def load_test_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

@pytest.mark.parametrize("test_case", load_test_data("valid_data.json"), ids=lambda tc: tc["name"])
def test_valid_input(test_case):
    input_data = test_case["url"]
    expected_output = test_case["output"]
    response = requests.get(f"{BASE_URL}"+input_data)
    assert response.status_code == 200
    actual_output = response.json()
    assert(actual_output[0]) == expected_output

@pytest.mark.parametrize("test_case", load_test_data("invalid_data.json"), ids=lambda tc: tc["name"])
def test_invalid_input(test_case):
    input_data = test_case["url"]
    expected_output = test_case["output"]
    response = requests.get(f"{BASE_URL}"+input_data)
    assert response.status_code == 200
    actual_output = response.json()
    assert(actual_output) == expected_output