import pytest
from collections import defaultdict

from string_parser import parse_string

def test_parse_string_valid_input():
    input_string = "file1.txt, file2.csv, file3.txt, file4.csv"
    expected_output = "file1.txt, file3.txt\nfile2.csv, file4.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_single_file():
    input_string = "file1.txt"
    expected_output = "file1.txt"
    assert parse_string(input_string) == expected_output

def test_parse_string_no_extension():
    with pytest.raises(ValueError, match="Invalid file format: file1"):
        parse_string("file1")

def test_parse_string_multiple_dots():
    input_string = "file1.tar.gz, file2.txt"
    expected_output = "file1.tar.gz\nfile2.txt"
    assert parse_string(input_string) == expected_output

def test_parse_string_different_extensions():
    input_string = "file1.txt, file2.csv, file3.doc, file4.pdf"
    expected_output = "file1.txt\nfile2.csv\nfile3.doc\nfile4.pdf"
    assert parse_string(input_string) == expected_output

def test_parse_string_duplicate_files():
    input_string = "file1.txt, file2.csv, file1.txt, file2.csv"
    expected_output = "file1.txt, file1.txt\nfile2.csv, file2.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_empty_file_name():
    with pytest.raises(ValueError, match="Invalid file format:"):
        parse_string(", file1.txt")

def test_parse_string_only_spaces():
    with pytest.raises(ValueError, match="Input string cannot be empty or whitespace only"):
        parse_string("   ")

def test_parse_string_leading_trailing_spaces():
    input_string = "  file1.txt  ,  file2.csv  "
    expected_output = "file1.txt\nfile2.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_inconsistent_spacing():
    input_string = "file1.txt  ,file2.csv,   file3.txt  "
    expected_output = "file1.txt, file3.txt\nfile2.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_large_input():
    input_string = ", ".join(f"file{i}.txt" for i in range(100))
    expected_output = ", ".join(f"file{i}.txt" for i in range(100))
    assert parse_string(input_string) == expected_output

def test_parse_string_invalid_characters():
    input_string = "file1.txt, file2|csv"
    with pytest.raises(ValueError, match="Invalid file format: file2|csv"):
        parse_string(input_string)

def test_parse_string_case_insensitive_grouping():
    input_string = "file1.txt, file2.Txt, file3.TXT"
    expected_output = "file1.txt, file2.Txt, file3.TXT"
    assert parse_string(input_string) == expected_output

def test_parse_string_special_characters():
    input_string = "file1@.txt, file2#.csv"
    expected_output = "file1@.txt\nfile2#.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_missing_file_name():
    with pytest.raises(ValueError, match="Invalid file format: .txt"):
        parse_string(".txt, file1.csv")

def test_parse_string_empty_input():
    with pytest.raises(ValueError, match="Input string cannot be empty or whitespace only"):
        parse_string("")

def test_parse_string_no_input():
    with pytest.raises(TypeError):
        parse_string()

def test_parse_string_trailing_spaces():
    with pytest.raises(ValueError, match="Invalid file format: "):
        parse_string("file1.txt, file2.csv, ")

def test_parse_string_multiple_spaces_in_between():
    input_string = "file1.txt  ,   file2.csv, file3.txt"
    expected_output = "file1.txt, file3.txt\nfile2.csv"
    assert parse_string(input_string) == expected_output

def test_parse_string_comma_spacing():
    input_string = "file1.txt, file2.csv ,file3.doc"
    expected_output = "file1.txt\nfile2.csv\nfile3.doc"
    assert parse_string(input_string) == expected_output
