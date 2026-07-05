"""File-system tools for the agent: virtual path backend + read/write/grep/ls."""
from src.tools.filesys.backend import VirtualFileSystem, get_vfs, resolve
from src.tools.filesys.file_tools import grep_files, list_directory, read_file, write_file

__all__ = [
    "read_file",
    "write_file",
    "grep_files",
    "list_directory",
    "VirtualFileSystem",
    "get_vfs",
    "resolve",
]
