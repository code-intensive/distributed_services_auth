from src.server import server

from src.server import server, mysql


def main() -> None:
    server.run("0.0.0.0", port=8000, debug=True, load_dotenv=True)


if __name__ == "__main__":
    main()
