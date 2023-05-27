import logging

from dotenv import load_dotenv

load_dotenv(".")

from uvicorn import run

import axilium_gpt


def main() -> int:
    run(axilium_gpt.app,
        log_level=logging.ERROR)
    return 0


if __name__ == "__main__":
    exit(main())

