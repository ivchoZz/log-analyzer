from analyzer import count_log_levels, percentage_levels
import pytest

#Тестваме функцията log_levels с pytest
def test_count_log_levels():
    sample_lines = [
        "2026-08-19 10:00:00 ERROR Something failed\n",
        "2026-08-19 10:01:00 WARNING Low disk space\n",
        "2026-08-19 10:02:00 INFO All good\n",
        "2026-08-19 10:03:00 ERROR Something failed\n"
    ]
    error_count, warning_count = count_log_levels(sample_lines)
    assert error_count == 2
    assert warning_count == 1

def test_count_log_levels_empty():
    sample_lines = []
    error_count, warning_count = count_log_levels(sample_lines)
    assert error_count == 0
    assert warning_count == 0

def test_count_log_levels_no_matches():
    sample_lines = [
        "2026-08-19 10:00:00 INFO Server started\n",
        "2026-08-19 10:01:00 INFO Request processed\n"
    ]
    error_count, warning_count = count_log_levels(sample_lines)
    assert error_count == 0
    assert warning_count == 0

#Тестваме функцията percentage_levels с pytest
def test_percеntage_levels():
    sample_lines = [
                    "2026-08-19 10:21:10 ERROR Timeout on request",
                    "2026-08-19 10:22:00 INFO Server started",              
                    "2026-08-19 11:20:02 ERROR Database connection failed",
                    "2026-08-19 10:19:15 INFO User logged in"
                    ]
    percentages = percentage_levels(sample_lines)
    assert percentages["ERROR"] == 50
    assert percentages["INFO"] == 50

def test_percentage_levels_log_levels_empty():
    sample_lines = []
    percentages = percentage_levels(sample_lines)
    assert not percentages





