def generate_python_class(schema: dict) -> str:
    class_name = schema["title"][0]["plain_text"]
    properties = schema["properties"]

    # Start defining the class
    class_definition = f"from dataclasses import dataclass\n"
    class_definition += f"\n\n"
    class_definition += f"@dataclass\n"
    class_definition += f"class {class_name}:\n"

    for prop_name, prop_details in properties.items():
        prop_name = prop_name.replace(" ", "_").lower()

        if prop_details["type"] == "text":
            class_definition += f"    {prop_name}: str\n"
        if prop_details["type"] == "title":
            class_definition += f"    {prop_name}: str\n"

    return class_definition
