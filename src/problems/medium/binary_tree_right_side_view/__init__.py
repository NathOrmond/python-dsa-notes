# This file makes the directory a Python package
# Auto-imports all public functions from the main module

def _auto_import_functions():
    """Automatically import all public functions from the main module."""
    import importlib
    import inspect
    from pathlib import Path
    
    try:
        # Get the main module name (same as directory name)
        module_name = Path(__file__).parent.name
        
        # Import the main module
        main_module = importlib.import_module(f'.{module_name}', package=__package__)
        
        # Get all public functions and import them
        imported_functions = []
        for name in dir(main_module):
            if not name.startswith('_'):
                obj = getattr(main_module, name)
                if inspect.isfunction(obj):
                    globals()[name] = obj
                    imported_functions.append(name)
        
        return imported_functions
    except Exception:
        # Fallback to manual import if dynamic discovery fails
        from .binary_tree_right_side_view import binary_tree_right_side_view, binary_tree_right_side_view_brute_force, binary_tree_right_side_view_optimized
        return ['binary_tree_right_side_view', 'binary_tree_right_side_view_brute_force', 'binary_tree_right_side_view_optimized']

# Auto-import all functions
__all__ = _auto_import_functions()
