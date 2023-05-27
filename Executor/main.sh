#!/usr/bin/bash

# Configurable Variables
TEST_MARK="ui"
TEST_NAME="0103"
PARALLEL_EXEC=4


# Paths
PYTEST_LOG="./Results/pytest.log"
PYTEST_RESULT="./Results/pytest_results"
ALLURE_REPORT_DIR="./Results/allure-report"
PYTEST_RESULT_HISTORY="$PYTEST_RESULT/history"
ALLURE_REPORT_HISTORY="$ALLURE_REPORT_DIR/history"


# Function to run PyTest
pytest_runner() {
  printf "MAIN-STARTED:\n"
  OPTIONS=" --alluredir=$PYTEST_RESULT -n $PARALLEL_EXEC"

  if [ -n "${TEST_MARK}" ]; then
    echo "MAIN-INFO: Test Marker - $TEST_MARK"
    OPTIONS+=" -m $TEST_MARK"
  fi

  if [ -n "${TEST_NAME}" ]; then
    echo "MAIN-INFO: Test NAME - $TEST_NAME"
    OPTIONS+=" -k $TEST_NAME"
  fi

  echo "MAIN-RUNNING: pytest $OPTIONS > $PYTEST_LOG"

  # shellcheck disable=SC2086
  pytest $OPTIONS > "$PYTEST_LOG"

  if grep -q 'ERROR' "$PYTEST_LOG"; then
    cleanup_after_pytest
    echo "MAIN-RUNNING: ERROR Detected! Skipping Allure report generation..."
    echo "MAIN-RUNNING: Press any key to Exit..."
    read -r
    exit 1
  fi
  printf "MAIN-RUNNING: PyTest Execution Finished Successfully!\n"
}

# Function to remove junk files after PyTest
cleanup_after_pytest() {
    printf "\nMAIN-RUNNING: Removing Junk Files after PyTest...\n"
    rm -rf .pytest_cache
    rm -rf Resource/__pycache__
    rm -rf Resource/Pages/__pycache__
    rm -rf Resource/Common/__pycache__
    rm -rf Tests/__pycache__
}

# Function to generate Allure report
generate_allure_report() {
    printf "\nMAIN-RUNNING: Generating Allure report...\n"

    # Remove old result history if it exists
    if [ -d "$ALLURE_REPORT_HISTORY" ] && [ -d "$PYTEST_RESULT_HISTORY" ]; then
        echo "MAIN-RUNNING: Removing old result history!"
        rm -rf "$PYTEST_RESULT_HISTORY"
    fi

    # Move new result history before generating report
    if [ -d "$ALLURE_REPORT_HISTORY" ]; then
        echo "MAIN-RUNNING: Moving new result history before generation!"
        mv -f "$ALLURE_REPORT_HISTORY" "$PYTEST_RESULT"
    fi

    # Generate Allure report and open it in the browser
    allure generate "$PYTEST_RESULT" --clean -o "$ALLURE_REPORT_DIR"
}

# Function to add environment properties
add_env_properties() {
  printf "\nMAIN-RUNNING: Adding environment properties file\n"
  {
    echo Server=QA
    echo Test.Filter.Mark=TEST_MARK
    echo Test.Filter.Name=TEST_MARK
    echo Pytest.Parallel.Execution=$PARALLEL_EXEC
    echo "Pytest.Version=$(pip show pytest | grep Version)"
    echo "Allure.Version=$(pip show allure-pytest | grep Version)"
  } > $PYTEST_RESULT/environment.properties
}

# Function to open Allure report in browser
open_allure_report() {
    printf "\nMAIN-RUNNING: Opening Allure report in browser...\n"
    allure open "$ALLURE_REPORT_DIR"
}


pytest_runner
cleanup_after_pytest
add_env_properties
generate_allure_report
open_allure_report
