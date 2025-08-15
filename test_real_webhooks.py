import json
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# First, let's create a small test OpenAPI spec with webhooks for validation
test_spec = {
    "openapi": "3.1.0",
    "info": {
        "title": "Webhook Test",
        "version": "1.0.0"
    },
    "webhooks": {
        "newPet": {
            "post": {
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer"},
                                    "name": {"type": "string"}
                                },
                                "required": ["id", "name"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                }
            }
        }
    }
}

# Save the test spec
with open('/tmp/test_webhooks.json', 'w') as f:
    json.dump(test_spec, f, indent=2)

print("Created test OpenAPI spec with webhooks at /tmp/test_webhooks.json")
print(json.dumps(test_spec, indent=2))