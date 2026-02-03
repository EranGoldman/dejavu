# DejaVu Tests

This directory contains all tests for the DejaVu project.

## Structure

```
tests/
├── device/           # Tests for device components
├── backend/          # Tests for backend API
├── integration/      # Integration tests
└── fixtures/         # Test data and fixtures
```

## Running Tests

### All Tests
```bash
# From project root
python -m pytest tests/

# With coverage
python -m pytest tests/ --cov=. --cov-report=html
```

### Device Tests
```bash
python -m pytest tests/device/
```

### Backend Tests
```bash
python -m pytest tests/backend/
```

### Integration Tests
```bash
python -m pytest tests/integration/
```

## Writing Tests

### Test Structure

Each test file should follow this structure:
```python
import pytest
from module import function_to_test


class TestFeatureName:
    """Test suite for feature X"""
    
    def test_basic_functionality(self):
        """Test basic case"""
        result = function_to_test()
        assert result == expected
    
    def test_edge_case(self):
        """Test edge case"""
        # Test implementation
        pass
```

### Fixtures

Common fixtures are available in `conftest.py`:
- `mock_device` - Mock device for testing
- `test_client` - Flask test client for API testing
- `sample_image` - Sample image for testing uploads

### Best Practices

1. **Test Naming**: Use descriptive names that explain what is being tested
2. **Isolation**: Each test should be independent and not rely on other tests
3. **Coverage**: Aim for >80% code coverage
4. **Mock External Services**: Use mocks for API calls, file I/O, etc.
5. **Fast Tests**: Keep tests fast by avoiding unnecessary delays

## Continuous Integration

Tests are automatically run on:
- Pull requests
- Pushes to main branch
- Scheduled nightly builds

## Test Requirements

Install test dependencies:
```bash
pip install -r requirements-test.txt
```

Required packages:
- pytest
- pytest-cov
- pytest-mock
- requests-mock
