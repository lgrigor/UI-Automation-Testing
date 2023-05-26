# UI Automation Test Suite and Architecture

[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)


The purpose of automation is to demonstrate an example of how to efficiently and effectively automate the testing process for the www.saucedemo.com website. By providing a comprehensive UI automation test suite and a well-designed automation architecture, this repository serves as a practical demonstration of automating repetitive and time-consuming tasks involved in testing the website.

Overall, this repository serves as an example of how automation can significantly enhance the testing process by saving time, increasing efficiency, improving test coverage, and providing reliable results. It demonstrates best practices and showcases a structured approach to UI automation for the Saucedemo website, serving as a valuable resource for individuals or teams looking to adopt automation in their testing workflows.

<br>

## Table of Contents

- [Features](#features)


<br>

## Features

### Naming Conventions
The project follows a consistent and structured naming convention for test files and test cases.

* Test Suite: Each test suite is named with a specific format, such as `01_Login_test.py` where the two digits at the beginning indicate the test suite number (01 in this example).

* Test Case: Each test case within a test suite is named with a descriptive format, such as `test_login_standard_user_0102` where the first two digits at the end (02) correspond to the test suite number, and the last two digits (02) indicate the test case number.

<br>

### Selective Test Execution
The architecture supports selective execution of specific test cases using the pytest -k option. By providing the corresponding test case identifier, such as `-k "0102"` you can instruct pytest to execute only the test case with the matching identifier.

<br>

### Parallel Execution
The architecture supports parallel execution of test cases, allowing for faster and more efficient testing.

<br>

### Allure Report Integration
The architecture seamlessly integrates with Allure, a powerful test report generation tool. It automatically generates detailed and visually appealing reports for the test execution results.

<br>

### Regression Run History
This architecture maintains a history of previous regression runs, allowing you to keep track of test execution results over time.

<br>
