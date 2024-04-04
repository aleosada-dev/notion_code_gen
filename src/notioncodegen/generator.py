def generate_enum(class_name: str, prop_name: str, prop_details: dict) -> str:
    enum_name = f"{prop_name.capitalize()}Enum"
    enum_values = prop_details[prop_details["type"]]["options"]

    enum_definition = f"class {class_name}{enum_name}(Enum):\n"
    for value in enum_values:
        enum_definition += (
            f"    {value['name'].replace(' ', '_').upper()} = '{value['name']}'\n"
        )

    enum_definition += f"\n\n"
    return enum_definition


def generate_python_class(schema: dict) -> str:
    class_name = schema["title"][0]["plain_text"]
    properties = schema["properties"]
    class_definition = f"from dataclasses import dataclass\n"

    if any(
        property["type"] in ["select", "status"] for property in properties.values()
    ):
        class_definition += f"from enum import Enum\n"

    if any(property["type"] == "date" for property in properties.values()):
        class_definition += f"import pendulum\n"

    class_definition += f"\n\n"

    for prop_name_snake_case, prop_details in [
        (key, value)
        for key, value in properties.items()
        if value["type"] in ["select", "status"]
    ]:
        class_definition += generate_enum(
            class_name, prop_name_snake_case, prop_details
        )

    # Start defining the class
    class_definition += f"@dataclass\n"
    class_definition += f"class {class_name}:\n"
    class_definition += f"    database_id: str\n"
    class_definition += f"    id: int\n"

    for prop_name, prop_details in properties.items():
        prop_name_snake_case = prop_name.replace(" ", "_").lower()

        if prop_details["type"] == "text":
            class_definition += f"    {prop_name_snake_case}: str\n"
        if prop_details["type"] == "title":
            class_definition += f"    {prop_name_snake_case}: str\n"
        if prop_details["type"] == "number":
            class_definition += f"    {prop_name_snake_case}: float\n"
        if prop_details["type"] == "select":
            class_definition += (
                f"    {prop_name_snake_case}: {class_name}{prop_name}Enum\n"
            )
        if prop_details["type"] == "date":
            class_definition += f"    {prop_name_snake_case}: pendulum.datetime\n"

    return class_definition
