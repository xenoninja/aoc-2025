import inspect
from pathlib import Path


def read_file_by_line(file_path):
    """Read a file line by line. If file_path is relative, resolve it relative to the caller's directory."""
    # Convert to Path object
    path = Path(file_path)

    # If path is relative, resolve it relative to the caller's file location
    if not path.is_absolute():
        # Get the caller's frame
        caller_frame = inspect.stack()[1]
        caller_file = Path(caller_frame.filename)
        # Resolve relative to caller's directory
        path = (caller_file.parent / path).resolve()

    try:
        with open(path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: File", file_path, "not found")
    except Exception as e:
        print("Error:", e)


def raw_read_file_by_line(file_path):
    """Read a file line by line. If file_path is relative, resolve it relative to the caller's directory."""
    # Convert to Path object
    path = Path(file_path)

    # If path is relative, resolve it relative to the caller's file location
    if not path.is_absolute():
        # Get the caller's frame
        caller_frame = inspect.stack()[1]
        caller_file = Path(caller_frame.filename)
        # Resolve relative to caller's directory
        path = (caller_file.parent / path).resolve()

    try:
        with open(path, "r") as file:
            return [line.strip("\n\r") for line in file]
    except FileNotFoundError:
        print("Error: File", file_path, "not found")
    except Exception as e:
        print("Error:", e)
