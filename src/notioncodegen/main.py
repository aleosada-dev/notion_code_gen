import click
import os
from notioncodegen.notion import fetch_database_schema
from notioncodegen.generator import generate_python_class
from dotenv import load_dotenv

load_dotenv()


@click.command()
@click.option(
    "-d", "--database_id", required=True, type=str, help="ID of the Notion database"
)
@click.option("-o", "--output", required=False, type=str, default="output.py")
def main(database_id: str, output: str) -> None:
    """
    Generate a Python class based on the schema of a Notion database
    :param database_id: ID of the Notion database
    """
    api_key = os.getenv("NOTION_APIKEY")
    schema = fetch_database_schema(api_key, database_id)
    class_definition = generate_python_class(schema)
    save_to_file(output, class_definition)


def save_to_file(output: str, class_definition: str) -> None:
    with open(output, "w") as f:
        f.write(class_definition)
