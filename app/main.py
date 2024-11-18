from logging import error

from app.services import add_and_commit
from app.setup import get_session


def generate_nested_json(level: int) -> None:
    nested_json = {}
    current_level = nested_json

    session = next(get_session())

    for i in range(0, level):
        current_level[f"level_{i}"] = {}
        current_level = current_level[f"level_{i}"]

        try:
            add_and_commit(session, nested_json)
        except Exception as e:
            error(f"Depth level of {i + 1} is not accepted!\n{repr(e)}")
            break


if __name__ == "__main__":
    generate_nested_json(1000)
