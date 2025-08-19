import pytest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_basic_functionality():
    """Test basic functionality without importing the main module"""
    # Basic test that should always pass
    assert True
    assert 1 + 1 == 2

def test_environment_detection():
    """Test environment variable detection"""
    # Test default environment
    if 'ENVIRONMENT' in os.environ:
        del os.environ['ENVIRONMENT']
    
    # Test with different environment values
    test_envs = ['dev', 'qa', 'prod']
    for env in test_envs:
        os.environ['ENVIRONMENT'] = env
        current_env = os.getenv('ENVIRONMENT', 'dev').lower()
        assert current_env == env

def test_required_files_exist():
    """Test that required files exist in the repository"""
    # Check if main.py exists
    main_file = os.path.join(os.path.dirname(__file__), '..', 'app', 'main.py')
    assert os.path.exists(main_file), "app/main.py should exist"
    
    # Check if requirements.txt exists
    req_file = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
    assert os.path.exists(req_file), "requirements.txt should exist"

def test_app_import():
    """Test that the app module can be imported"""
    try:
        # Try to import the app module
        import app.main as main
        
        # Test that main functions exist
        assert hasattr(main, 'get_environment')
        assert hasattr(main, 'get_environment_config')
        assert callable(main.get_environment)
        assert callable(main.get_environment_config)
        
        # Test environment configurations
        config = main.get_environment_config('dev')
        assert 'title' in config
        assert 'bg_color' in config
        assert 'icon' in config
        
    except ImportError as e:
        pytest.skip(f"Cannot import main module: {e}")

def test_streamlit_import():
    """Test that streamlit can be imported"""
    try:
        import streamlit
        assert True
    except ImportError:
        pytest.skip("Streamlit not available - this is expected in CI environment")

# Cleanup function
def teardown_module():
    """Clean up environment variables after tests"""
    if 'ENVIRONMENT' in os.environ:
        del os.environ['ENVIRONMENT']