from datetime import datetime, timezone
from pathlib import Path


RUN_LOG = Path(__file__).resolve().parent / "automation_log.txt"


def write_run_log() -> None:
    timestamp = datetime.now(timezone.utc)
    message = f"Hello automation ran at {timestamp:%Y-%m-%d %H:%M:%S UTC}\n"
    RUN_LOG.write_text(message, encoding="utf-8")
    print(message.strip())


def main() -> None:
    write_run_log()


if __name__ == "__main__":
    main()
