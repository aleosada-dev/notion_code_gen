import click


@click.command()
@click.option(
    "-d", "--database_id", required=True, type=str, help="ID of the Notion database"
)
def main(database_id: str):
    print(database_id)


if __name__ == "__main__":
    main()
