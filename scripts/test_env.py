#!/usr/bin/env python3
"""
Environment Loader

This script loads environment variables from .env file and tests cache configuration.
"""

import os
from pathlib import Path


def load_env_file():
    """Load environment variables from .env file."""
    env_file = Path(__file__).parent.parent / ".env"
    
    if not env_file.exists():
        print("❌ .env file not found")
        return False
    
    print(f"📁 Loading environment from: {env_file}")
    
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse key=value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Set environment variable
                os.environ[key] = value
                print(f"✅ Set {key}={value}")
    
    return True


def test_cache_configuration():
    """Test the cache configuration."""
    print("\n🔍 Testing Cache Configuration")
    print("=" * 40)
    
    # Check if PYTHONPYCACHEPREFIX is set
    cache_prefix = os.environ.get('PYTHONPYCACHEPREFIX')
    if cache_prefix:
        print(f"✅ PYTHONPYCACHEPREFIX: {cache_prefix}")
        
        # Check if the cache directory exists
        cache_dir = Path(cache_prefix)
        if cache_dir.exists():
            print(f"✅ Cache directory exists: {cache_dir.absolute()}")
        else:
            print(f"⚠️  Cache directory doesn't exist: {cache_dir.absolute()}")
            print("   Run: make setup-cache")
    else:
        print("❌ PYTHONPYCACHEPREFIX not set")
    
    # Test Python cache behavior
    print("\n🧪 Testing Python Cache Behavior")
    print("-" * 30)
    
    # Import a module to trigger cache creation
    try:
        import sys
        sys.path.append('.')
        from src.problems.easy.two_sum import two_sum
        print("✅ Module imported successfully")
        
        # Check where cache files are created
        import tempfile
        import subprocess
        
        # Run a simple Python command to see cache behavior
        result = subprocess.run([
            sys.executable, '-c', 
            'import sys; print("Cache prefix:", sys.pycache_prefix)'
        ], capture_output=True, text=True, cwd=Path(__file__).parent)
        
        if result.returncode == 0:
            print(f"✅ Python cache prefix: {result.stdout.strip()}")
        else:
            print(f"❌ Error checking cache prefix: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error testing cache: {e}")


def main():
    """Main function."""
    print("🔧 Environment Configuration Test")
    print("=" * 50)
    
    # Load .env file
    if load_env_file():
        print("\n✅ Environment loaded successfully")
    else:
        print("\n❌ Failed to load environment")
        return
    
    # Test cache configuration
    test_cache_configuration()
    
    print("\n💡 Recommendations:")
    print("1. Add this to your shell profile (.bashrc, .zshrc, etc.):")
    print("   export PYTHONPYCACHEPREFIX=.cache/python")
    print("2. Or run: source .env (if your shell supports it)")
    print("3. Or use: python -c 'import os; exec(open(\".env\").read())'")


if __name__ == "__main__":
    main()
