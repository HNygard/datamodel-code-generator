#!/usr/bin/env python3

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Test if the OpenAPIScope includes Webhooks
try:
    from datamodel_code_generator import OpenAPIScope
    print("Available OpenAPI scopes:")
    for scope in OpenAPIScope:
        print(f"  - {scope.name}: {scope.value}")
    
    # Test if Webhooks is in the enum
    assert hasattr(OpenAPIScope, 'Webhooks'), "Webhooks scope not found in OpenAPIScope enum"
    assert OpenAPIScope.Webhooks.value == "webhooks", "Webhooks scope value should be 'webhooks'"
    
    print("\n✓ OpenAPIScope.Webhooks successfully added!")
    
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)