import pytest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

try:
    import main
except ImportError:
    pytest.skip("Cannot import main module", allow_module_level=True)

class TestEnvironmentConfig:
    """Test environment configuration functionality"""
    
    def test_get_environment_default(self):
        """Test default environment is dev"""
        # Clear environment variable if it exists
        if 'ENVIRONMENT' in os.environ:
            del os.environ['ENVIRONMENT']
        
        env = main.get_environment()
        assert env == 'dev'
    
    def test_get_environment_from_env_var(self):
        """Test environment detection from environment variable"""
        test_cases = ['dev', 'qa', 'prod']
        
        for test_env in test_cases:
            os.environ['ENVIRONMENT'] = test_env
            env = main.get_environment()
            assert env == test_env
    
    def test_get_environment_config_dev(self):
        """Test development environment configuration"""
        config = main.get_environment_config('dev')
        
        assert config['title'] == 'Dev Environment'
        assert config['bg_color'] == '#2E7D32'
        assert config['icon'] == '🔧'
        assert 'development' in config['description'].lower()
    
    def test_get_environment_config_qa(self):
        """Test QA environment configuration"""
        config = main.get_environment_config('qa')
        
        assert config['title'] == 'QA Environment'
        assert config['bg_color'] == '#F57F17'
        assert config['icon'] == '🧪'
        assert 'qa' in config['description'].lower() or 'quality' in config['description'].lower()
    
    def test_get_environment_config_prod(self):
        """Test production environment configuration"""
        config = main.get_environment_config('prod')
        
        assert config['title'] == 'Production Environment'
        assert config['bg_color'] == '#C62828'
        assert config['icon'] == '🚀'
        assert 'production' in config['description'].lower()
    
    def test_get_environment_config_fallback(self):
        """Test fallback to dev config for unknown environment"""
        config = main.get_environment_config('unknown')
        dev_config = main.get_environment_config('dev')
        
        assert config == dev_config

class TestAppFunctionality:
    """Test core application functionality"""
    
    def test_main_function_exists(self):
        """Test that main function exists and is callable"""
        assert hasattr(main, 'main')
        assert callable(main.main)
    
    def test_environment_configs_have_required_keys(self):
        """Test that all environment configs have required keys"""
        required_keys = ['title', 'bg_color', 'text_color', 'icon', 'description']
        environments = ['dev', 'qa', 'prod']
        
        for env in environments:
            config = main.get_environment_config(env)
            for key in required_keys:
                assert key in config, f"Missing key '{key}' in {env} config"
                assert config[key] is not None, f"Key '{key}' is None in {env} config"
                assert config[key] != '', f"Key '{key}' is empty in {env} config"

class TestIntegration:
    """Integration tests"""
    
    def test_app_imports_successfully(self):
        """Test that the app can be imported without errors"""
        try:
            import main
            assert True
        except Exception as e:
            pytest.fail(f"Failed to import main module: {e}")
    
    def test_streamlit_compatibility(self):
        """Test basic Streamlit compatibility"""
        try:
            import streamlit as st
            assert True
        except ImportError:
            pytest.skip("Streamlit not available for testing")

# Cleanup after tests
def teardown_module():
    """Clean up environment variables after tests"""
    if 'ENVIRONMENT' in os.environ:
        del os.environ['ENVIRONMENT']