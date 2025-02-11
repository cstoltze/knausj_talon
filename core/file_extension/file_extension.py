from talon import Context, Module

from ..user_settings import get_list_from_csv

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

_file_extensions_defaults = {
    "bee tea": ".bt",
    "build": ".build",
    "back": ".bak",
    "backup": ".bkp",
    "batch": ".bat",
    "bin": ".bin",
    "bend": ".bin",
    "bit map": ".bmp",
    "bump": ".bmp",
    "B Z two": ".bz2",
    "B zip": ".bz2",
    "check": ".chk",
    "C G I": ".cgi",
    "C F G": ".cfg",
    "conf": ".conf",
    "config": ".config",
    "com": ".com",
    "C S V": ".csv",
    "data": ".data",
    "database": ".db",
    "deb": ".deb",
    "debug": ".debug",
    "desktop": ".desktop",
    "dock X": ".docx",
    "dock": ".doc",
    "draw eye oh": ".drawio",
    "E F I": ".efi",
    "elf": ".elf",
    "E M L": ".eml",
    "exe": ".exe",
    "flack": ".flac",
    "G bag": ".gdb",
    "G D B": ".gdb",
    "git": ".git",
    "G Z": ".gz",
    "G zip": ".gz",
    # NOTE - H conflicted with way too much
    "header": ".h",
    "hex": ".hex",
    "H T M L": "html",
    "hypertext": "html",
    "ida": ".idb",
    "I sixty four": ".i64",
    "image": "img",
    "jar": ".jar",
    "java": ".java",
    "J S": ".js",
    "javascript": ".js",
    "jason five": ".json5",
    "jason": ".json",
    "J peg": ".jpg",
    "key": ".key",
    "K O": ".ko",
    "kay oh": ".ko",
    "local": ".local",
    "log": ".log",
    "lua": ".lua",
    "M D": ".md",
    "mark down": ".md",
    "message": ".msg",
    "oh": ".o",
    "object": ".o",
    "net": ".net",
    "nse": ".nse",
    "org": ".org",
    "out": ".out",
    "patch": ".patch",
    "P D F": ".pdf",
    "pam": ".pem",
    "P cap": "pcap",
    "P H P": ".php",
    "P L": ".pl",
    "pearl": ".pl",
    "pickle": ".pkl",
    "pie": ".py",
    "pie four": ".py4",
    "ping": ".png",
    "postscript": ".ps",
    "P S": ".ps",
    "power shell": ".ps1",
    "pretty": ".pretty.js",
    "pub": ".pub",
    "queue el": ".ql",
    "R C": ".rc",
    "run": ".run",
    # "R S": ".rs",
    "rust": ".rs",
    "C S": ".cs",
    "see sharp": ".cs",
    "see": ".c",
    "Q cow too": ".qcow2",
    "Q cow": ".qcow2",
    "rules": ".rules",
    "service": ".service",
    "session": ".session",
    "S H": ".sh",
    "shell": ".sh",
    "snippets": ".snippets",
    "S O": ".so",
    "so": ".so",
    "socket": ".socket",
    "S T P": ".stp",
    "talon": ".talon",
    "tar": ".tar",
    "tar G Z": ".tar.gz",
    "tar G zip": ".tar.gz",
    "tar B Z": ".tar.bz2",
    "tar B zip": ".tar.bz2",
    "tar X Z": ".tar.xz",
    "task": ".task",
    "text": ".txt",
    "timer": ".timer",
    "tom L": ".toml",
    "N map": ".nse",
    "N S E": ".nse",
    "neo vim": ".nvim",
    "N vim": ".nvim",
    "web P": ".webp",
    "vim": ".vim",
    "X Z": ".xz",
    "X M L": ".xml",
    "yaml": ".yml",
    "z shell": ".zsh",
    "zsh": ".zsh",
    "zip": ".zip",
    # tlds
    "com": ".com",
    "net": ".net",
    "org": ".org",
    "us": ".us",
    "U S": ".us",
    "C A": ".ca",
    "C X": ".cx",
    "T W": ".tw",
}

file_extensions = get_list_from_csv(
    "file_extensions.csv",
    headers=("File extension", "Name"),
    default=_file_extensions_defaults,
)

ctx = Context()
ctx.lists["user.file_extension"] = file_extensions
