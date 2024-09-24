import warnings

def deprecated_function():
    warnings.warn("This function is deprecated.", DeprecationWarning)
    return "Deprecated function result"


# import warnings
#
# warnings.simplefilter("ignore", DeprecationWarning)

# Usage example
result = deprecated_function()
print(result)  # Output: Deprecated function result