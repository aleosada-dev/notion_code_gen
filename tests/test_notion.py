import os
from notioncodegen.notion import fetch_database_schema
from dotenv import load_dotenv

load_dotenv()


def test_fetch_database_schema():
    """
    Integration test for the fetch_database_schema function
    """
    api_key = os.getenv("NOTION_APIKEY")
    database_id = "256bf5a547a74346ab4f85506a0f7d36"
    schema = fetch_database_schema(api_key, database_id)
    assert schema["object"] == "database"
    assert schema["id"] == database_id
