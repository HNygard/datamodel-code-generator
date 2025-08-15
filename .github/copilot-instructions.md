# Copilot Instructions for datamodel-code-generator

## About the Project

This is **datamodel-code-generator**, a Python code generator that creates data models (Pydantic, dataclasses, TypedDict, msgspec) from schema definitions including OpenAPI, JSON Schema, GraphQL, and more.

## Project Structure

### Core Components
- **`src/datamodel_code_generator/`** - Main source code
  - **`parser/`** - Contains parsers for different input formats (OpenAPI, JSON Schema, GraphQL, etc.)
  - **`model/`** - Model generation and template handling
  - **`arguments.py`** - CLI argument parsing and validation
  - **`format.py`** - Code formatting (Black, isort, ruff)
  - **`imports.py`** - Import management for generated code

### Key Parser Classes
- **`OpenAPIParser`** - Handles OpenAPI 3.x specifications
- **`JsonSchemaParser`** - Processes JSON Schema documents  
- **`GraphQLParser`** - Parses GraphQL schemas
- **`DataParser`** - Handles raw JSON/YAML/CSV data

### Testing
- **`tests/`** - Comprehensive test suite
  - **`tests/data/`** - Test fixtures (OpenAPI specs, JSON schemas, etc.)
  - **`tests/parser/`** - Parser-specific tests
  - **`tests/model/`** - Model generation tests

## Development Guidelines

### Code Style
- Use **Ruff** for linting and formatting (configured in `pyproject.toml`)
- Use **Black** for code formatting
- Use **isort** for import sorting
- Follow type hints throughout the codebase

### Testing Approach
- Add test fixtures to `tests/data/` for new input formats
- Create expected output files for validation
- Use parametrized tests for different input/output combinations
- Test both positive and edge cases

### Key Patterns

#### Adding New Input Format Support
1. Create parser class inheriting from `Parser` base class
2. Implement `parse_raw()` method to process the input format
3. Add format detection logic to `infer_input_type()`
4. Add CLI argument support in `arguments.py`
5. Create comprehensive tests with fixtures

#### Adding New Output Format Support
1. Create model template in appropriate template directory
2. Update model generation logic in `model/` package
3. Add CLI option in `arguments.py`
4. Test with various input formats

#### OpenAPI Scope Handling
- **Schemas**: Component schemas (`#/components/schemas`)
- **Paths**: API endpoints and their operations
- **Tags**: Operation groupings
- **Parameters**: Reusable parameter definitions
- **Webhooks**: Incoming webhook definitions (OpenAPI 3.1+)

### Common Tasks

#### Adding New CLI Options
- Update `arguments.py` with new argument definition
- Add validation logic if needed
- Update help text and documentation
- Add tests for the new option

#### Parser Extensions
- Extend existing parsers by overriding specific methods
- Reuse common parsing logic where possible
- Handle edge cases and malformed input gracefully
- Add comprehensive error messages

#### Template Customization
- Use Jinja2 templates for code generation
- Support custom template directories via `--custom-template-dir`
- Allow template data injection via `--extra-template-data`

### Performance Considerations
- Use caching for repeated schema resolutions
- Implement lazy loading for large specifications
- Optimize reference resolution with proper deduplication

### Error Handling
- Provide clear error messages with line numbers when possible
- Use specific exception types for different error categories
- Include suggestions for fixing common issues

## Testing Commands

```bash
# Run all tests
pytest

# Run specific parser tests
pytest tests/parser/

# Run with coverage
pytest --cov=datamodel_code_generator

# Format code
ruff format .
ruff check . --fix

# Run pre-commit hooks
pre-commit run --all-files
```

## Common Debugging Tips

### Schema Resolution Issues
- Check `$ref` resolution paths
- Verify remote schema accessibility with `--http-ignore-tls` if needed
- Use `--debug` flag for detailed parsing information

### Generation Issues
- Validate input schema syntax first
- Check scope selection (`--openapi-scopes`)
- Test with minimal example to isolate issues
- Review generated imports and type annotations

### Performance Problems
- Profile with large schemas to identify bottlenecks
- Consider memory usage with deeply nested structures
- Check for circular reference handling

## Code Contribution Guidelines
- Follow existing code patterns and naming conventions
- Add type hints to all new functions and methods
- Include docstrings for public APIs
- Update tests and documentation for new features
- Ensure backward compatibility or provide migration path