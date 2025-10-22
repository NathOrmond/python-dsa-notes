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
        from .best_time_to_buy_and_sell_stock import best_time_to_buy_and_sell_stock, best_time_to_buy_and_sell_stock_brute_force, best_time_to_buy_and_sell_stock_optimized
        return ['best_time_to_buy_and_sell_stock', 'best_time_to_buy_and_sell_stock_brute_force', 'best_time_to_buy_and_sell_stock_optimized']

# Auto-import all functions
__all__ = _auto_import_functions()
