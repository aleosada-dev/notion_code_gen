import requests


def fetch_database_schema(api_key, database_id):
    """
    Test the fetch_database_schema function
    :param api_key: API key for the Notion integration
    :param database_id: ID of the Notion database
    :return: JSON response from the API with the schema of the table
    """
    url = f"https://api.notion.com/v1/databases/{database_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2021-05-13",  # Use the latest supported version
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch database schema: {response.text}")
