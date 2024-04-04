import pytest
from notioncodegen.generator import generate_python_class


@pytest.fixture
def default_schema() -> dict:
    return {
        "title": [{"plain_text": "Test"}],
        "properties": {
            "Title": {"type": "title"},
        },
    }


@pytest.fixture
def default_expected() -> str:
    expected = f"from dataclasses import dataclass\n"
    expected += f"\n\n"
    expected += f"@dataclass\n"
    expected += f"class Test:\n"
    expected += f"    database_id: str\n"
    expected += f"    id: int\n"

    return expected


def test_default_properties(default_schema: dict, default_expected: str) -> None:
    schema = default_schema
    expected = default_expected
    expected += f"    title: str\n"

    result = generate_python_class(schema)
    assert result == expected


def test_number_propertie(default_schema: dict, default_expected: str) -> None:
    schema = default_schema
    schema["properties"] = schema["properties"] | {"Number": {"type": "number"}}

    expected = default_expected
    expected += f"    title: str\n"
    expected += f"    number: float\n"

    result = generate_python_class(schema)
    assert result == expected
