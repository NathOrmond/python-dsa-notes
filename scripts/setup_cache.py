#!/usr/bin/env python3
"""
Cache Configuration Helper

This script helps configure Python cache settings for the DSA project.
"""

import os
import sys
from pathlib import Path


def setup_centralized_cache():
    """Set up centralized cache directory and provide instructions."""
    project_root = Path(__file__).parent.parent  # Go up one level from scripts/
    
    # Create cache directory
    cache_dir = project_root / ".cache" / "python"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    print("🔧 Python Cache Configuration")
    print("=" * 40)
    print()
    print("✅ Centralized cache directory created at:", cache_dir)
    print()
    print("📋 To use centralized cache, choose one of these options:")
    print()
    print("   Option 1: Use .env file (recommended)")
    print("   cp env.example .env")
    print("   # Then edit .env and uncomment PYTHONPYCACHEPREFIX")
    print()
    print("   Option 2: Add to your shell profile")
    print("   (.bashrc, .zshrc, .profile, etc.)")
    print(f"   export PYTHONPYCACHEPREFIX={cache_dir.absolute()}")
    print()
    print("   Option 3: Run in current shell")
    print(f"   export PYTHONPYCACHEPREFIX={cache_dir.absolute()}")
    print()
    print("💡 Benefits:")
    print("   - No more __pycache__ directories in your source code")
    print("   - Cleaner project structure")
    print("   - Centralized cache management")
    print()
    print("🧹 To clean cache: make clean-cache")


def show_cache_info():
    """Show current cache configuration."""
    print("📊 Current Cache Configuration")
    print("=" * 35)
    print()
    
    cache_prefix = os.environ.get('PYTHONPYCACHEPREFIX')
    if cache_prefix:
        print(f"✅ Centralized cache enabled: {cache_prefix}")
    else:
        print("❌ Centralized cache not enabled")
        print("   Run: python scripts/setup_cache.py")
    
    print()
    print("🔍 Current __pycache__ directories:")
    project_root = Path(__file__).parent.parent  # Go up one level from scripts/
    cache_dirs = list(project_root.rglob("__pycache__"))
    
    if cache_dirs:
        for cache_dir in cache_dirs:
            print(f"   - {cache_dir.relative_to(project_root)}")
    else:
        print("   ✅ No __pycache__ directories found")


def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == "info":
        show_cache_info()
    else:
        setup_centralized_cache()


if __name__ == "__main__":
    main()
