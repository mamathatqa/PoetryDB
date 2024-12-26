# API Testing Framework with pytest

## Overview
This project demonstrates an API testing framework using `pytest`. It includes structured test cases for validating API requests with valid and invalid inputs based on test data stored in JSON files.

## Project Structure
```
├── .env                # Contains confidential environment variables
├── .gitignore          # Specifies files/folders to be ignored in version control
├── invalid_data.json   # Test data for invalid API requests
├── valid_data.json     # Test data for valid API requests
├── test_api.py         # Test file containing test cases
```

## Prerequisites
Before running the tests, ensure the following are installed on your system:

1. **Python**: Install the latest version from [Python Official Site](https://www.python.org/downloads/).
2. **pytest**: Install using `pip install pytest`.
3. **dotenv**: Install using `pip install python-dotenv`.
4. **requests**: Install using `pip install requests`.

## Installation

1. Clone the project repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure a `requirements.txt` file is available containing necessary dependencies like `pytest`, `dotenv`, `requests`.)*
   Here, make sure that versions are included in requirements.txt file.

## Running the Tests

To execute the test cases, use the following commands:

1. Run all tests with verbose output:
   ```bash
   pytest -v
   ```

2. Debug failed tests by including print statements and using the `-s` flag:
   ```bash
   pytest -s
   ```

## Test Cases

### 1. Loading Test Data
The `load_test_data()` method is used to dynamically load test data from JSON files (`valid_data.json` and `invalid_data.json`). This method is reusable and can be integrated into multiple test cases.

### 2. Test for Valid Inputs
- **File**: `test_api.py`
- **Test**: `test_valid_input()`
- **Description**: Sends API requests using valid inputs from `valid_data.json` and validates the responses.
- **Assertions**: Checks that responses match the expected outputs defined in the JSON file.

### 3. Test for Invalid Inputs
- **File**: `test_api.py`
- **Test**: `test_invalid_input()`
- **Description**: Sends API requests using invalid inputs from `invalid_data.json` and validates the error responses.
- **Assertions**: Checks that responses match the expected error messages defined in the JSON file.

## Key Features
- Modular and reusable test data loader (`load_test_data()`).
- Separate JSON files for valid and invalid inputs for better test management.
- Debugging support using `pytest -s`.

## Example Commands
1. Run tests:
   ```bash
   pytest -v
   ```

2. Debug tests:
   ```bash
   pytest -s
   ```

3. Run specific tests:
   ```bash
   pytest test_api.py::test_valid_input
   ```

## Additional Resources
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Requests Library](https://docs.python-requests.org/en/latest/)
- [dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)

---
*Note*: Ensure the `.env` file is properly configured with necessary environment variables, and it is excluded from version control using `.gitignore` for security reasons.
