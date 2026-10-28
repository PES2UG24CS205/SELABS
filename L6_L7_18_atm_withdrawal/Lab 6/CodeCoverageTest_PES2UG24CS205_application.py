import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup

# --- withdraw() tests ---
def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_withdraw_unknown_account():
    with pytest.raises(ValueError, match="unknown account"):
        withdraw(5000, 1000, "checking", True)

def test_withdraw_invalid_amount_zero():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 0, "savings", True)

def test_withdraw_invalid_amount_not_multiple_100():
    with pytest.raises(ValueError, match="invalid amount"):
        withdraw(5000, 150, "savings", True)

def test_withdraw_limit_exceeded():
    assert withdraw(50000, 26000, "savings", True) == "limit exceeded"

def test_withdraw_different_bank_small_amount():
    # triggers 20 fee
    assert withdraw(5000, 1000, "savings", False) == 3980

def test_withdraw_different_bank_large_amount():
    # triggers 20 + 10 = 30 fee
    assert withdraw(20000, 11000, "savings", False) == 8970

def test_withdraw_insufficient_funds():
    assert withdraw(1000, 2000, "savings", True) == "insufficient funds"

def test_withdraw_insufficient_funds_with_fee():
    assert withdraw(1010, 1000, "savings", False) == "insufficient funds"

# --- pin_check() tests ---
def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"

def test_pin_check_attempts_exhausted():
    assert pin_check(1111, 1234, 3) == "card blocked"

def test_pin_check_second_attempt_fail():
    assert pin_check(1111, 1234, 2) == "card blocked"

def test_pin_check_first_attempt_fail():
    assert pin_check(1111, 1234, 1) == "retry"

# --- note_breakup() tests ---
def test_note_breakup_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        note_breakup(150)

def test_note_breakup_with_200s():
    # 1700 = 3x500 + 1x200 + 0x100
    assert note_breakup(1700) == (3, 1, 0)

def test_note_breakup_without_200s():
    # 1600 = 3x500 + 0x200 + 1x100
    assert note_breakup(1600) == (3, 0, 1)