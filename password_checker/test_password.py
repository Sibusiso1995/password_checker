import Password_checker as checker
import pytest


def test_password_is_valid_exist():
     # testing condintion 1
    with pytest.raises(Exception) as empty:
        assert checker.password_is_valid("")
        assert empty.value.args[0] == "password should exist"
    
def test_password_is_valid_len():
    # testing condition 2
    with pytest.raises(Exception) as less:
        assert checker.password_is_valid("Ab2")
        assert less.value.args[0] == "password should be longer than than 8 characters"

def test_password_is_valid_lowercase():
    # testing condition 3
    with pytest.raises(Exception) as small:
        assert checker.password_is_valid("SIBUSISO1!".lower())
        assert small.value.args[0] == "password should have at least one lowercase letter"

def test_password_is_valid_uppercase():
     # testing condition 4
    with pytest.raises(Exception) as caps:    
         assert checker.password_is_valid("sibusiso1!".upper())
         assert caps.value.args[0] == "password should have at least one uppercase letter"
        
def test_password_is_valid_digit():
    # testing condition 5
    with pytest.raises(Exception) as num:
        assert checker.password_is_valid("Indi%&GlH")
        assert num.value.args[0] == "password should at least have one digit"

def test_password_is_valid_characters():
    # testing condition 6
    with pytest.raises(Exception) as symbol:
        assert checker.password_is_valid("Sibu1234Z")
        assert symbol.value.args[0] == "password should have at least one special character"

def test_password_is_ok_exist():
    assert checker.password_is_ok("") == False

def test_password_is_ok_len():
    assert checker.password_is_ok("nid5#") == False
    assert checker.password_is_ok("nD5#") == False

def test_password_is_ok_pass():
    assert checker.password_is_ok("Sibusiso1!") == True





