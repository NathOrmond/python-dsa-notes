#!/bin/bash
# Environment Setup Script for DSA Learning Project

echo "🔧 Setting up environment for DSA Learning Project"
echo "=================================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ .env file not found"
    echo "💡 Run: make setup-env"
    exit 1
fi

echo "✅ .env file found"

# Load environment variables
echo "📁 Loading environment variables..."
export $(grep -v '^#' .env | xargs)

echo "✅ Environment loaded"
echo "🔍 PYTHONPYCACHEPREFIX: $PYTHONPYCACHEPREFIX"
echo "🔍 PYTHONPATH: $PYTHONPATH"

# Test Python cache configuration
echo ""
echo "🧪 Testing Python cache configuration..."
python -c "
import sys
print(f'Python cache prefix: {sys.pycache_prefix}')
print(f'Cache directory: {sys.pycache_prefix}')
"

echo ""
echo "💡 To make this permanent, add to your shell profile:"
echo "   echo 'export PYTHONPYCACHEPREFIX=.cache/python' >> ~/.bashrc"
echo "   echo 'export PYTHONPATH=.' >> ~/.bashrc"
echo "   source ~/.bashrc"
