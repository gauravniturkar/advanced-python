# calculator.py - Module to be tested
class Calculator:
    """Simple calculator class for demonstration"""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exp):
        return base ** exp


# user.py - Another module for testing
class User:
    """User class for demonstration"""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False
    
    def activate(self):
        self.is_active = True
    
    def update_email(self, new_email):
        if '@' not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email


# test_calculator.py - Test cases for Calculator
import pytest


class TestCalculator:
    """Test suite for Calculator class"""
    
    @pytest.fixture
    def calc(self):
        """Fixture to create a Calculator instance"""
        return Calculator()
    
    def test_add(self, calc):
        """Test addition operation"""
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
    
    def test_subtract(self, calc):
        """Test subtraction operation"""
        assert calc.subtract(5, 3) == 2
        assert calc.subtract(0, 5) == -5
    
    def test_multiply(self, calc):
        """Test multiplication operation"""
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0
    
    def test_divide(self, calc):
        """Test division operation"""
        assert calc.divide(10, 2) == 5
        assert calc.divide(9, 3) == 3
        assert calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self, calc):
        """Test division by zero raises exception"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
    
    @pytest.mark.parametrize("base,exp,expected", [
        (2, 3, 8),
        (5, 2, 25),
        (10, 0, 1),
        (3, 4, 81),
    ])
    def test_power_parametrized(self, calc, base, exp, expected):
        """Test power operation with multiple parameters"""
        assert calc.power(base, exp) == expected


# test_user.py - Test cases for User
import pytest


class TestUser:
    """Test suite for User class"""
    
    @pytest.fixture
    def user(self):
        """Fixture to create a User instance"""
        return User("john_doe", "john@example.com")
    
    def test_user_creation(self, user):
        """Test user is created correctly"""
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.is_active is True
    
    def test_deactivate_user(self, user):
        """Test user deactivation"""
        user.deactivate()
        assert user.is_active is False
    
    def test_activate_user(self, user):
        """Test user activation"""
        user.deactivate()
        user.activate()
        assert user.is_active is True
    
    def test_update_email_valid(self, user):
        """Test updating email with valid format"""
        user.update_email("newemail@example.com")
        assert user.email == "newemail@example.com"
    
    def test_update_email_invalid(self, user):
        """Test updating email with invalid format raises error"""
        with pytest.raises(ValueError, match="Invalid email format"):
            user.update_email("invalidemail")
    
    @pytest.mark.parametrize("email", [
        "test@test.com",
        "user@domain.org",
        "admin@company.co.uk"
    ])
    def test_valid_emails(self, user, email):
        """Test multiple valid email formats"""
        user.update_email(email)
        assert user.email == email


# conftest.py - Shared fixtures and configuration
import pytest


@pytest.fixture(scope="session")
def setup_teardown():
    """Session-scoped fixture for setup and teardown"""
    print("\n=== Setting up test session ===")
    yield
    print("\n=== Tearing down test session ===")


@pytest.fixture
def sample_data():
    """Fixture providing sample test data"""
    return {
        'numbers': [1, 2, 3, 4, 5],
        'strings': ['apple', 'banana', 'cherry'],
        'mixed': [1, 'two', 3.0, True]
    }


# test_advanced_features.py - Advanced pytest features
import pytest


@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow (can be skipped with -m "not slow")"""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    """Test that will be skipped"""
    assert False


@pytest.mark.skipif(pytest.__version__ < "7.0", reason="Requires pytest 7.0+")
def test_new_pytest_feature():
    """Test that runs only on newer pytest versions"""
    assert True


@pytest.mark.xfail(reason="Known bug in division")
def test_known_failure():
    """Test expected to fail"""
    assert 1 / 3 * 3 == 1  # Floating point precision issue


def test_with_sample_data(sample_data):
    """Test using shared fixture"""
    assert len(sample_data['numbers']) == 5
    assert 'banana' in sample_data['strings']


class TestGroupedTests:
    """Grouped tests using a class"""
    
    @pytest.fixture(autouse=True)
    def setup_method_fixture(self):
        """Auto-used fixture for this class"""
        self.value = 42
    
    def test_value_set(self):
        """Test that fixture set the value"""
        assert self.value == 42
    
    def test_value_manipulation(self):
        """Test value manipulation"""
        self.value *= 2
        assert self.value == 84


# How to run these tests:
# 1. Install pytest: pip install pytest
# 2. Run all tests: pytest
# 3. Run with verbose output: pytest -v
# 4. Run specific test file: pytest test_calculator.py
# 5. Run specific test: pytest test_calculator.py::TestCalculator::test_add
# 6. Run tests matching pattern: pytest -k "divide"
# 7. Run tests with markers: pytest -m "not slow"
# 8. Show print statements: pytest -s
# 9. Generate coverage report: pytest --cov=. --cov-report=html