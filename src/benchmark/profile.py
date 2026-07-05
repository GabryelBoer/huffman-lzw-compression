import math
import re
from dataclasses import dataclass
from typing import Dict, List


PYTHON_TOKENS = [
    "def", "import", "from", "return", "class", "if", "else", "elif",
    "for", "while", "try", "except", "with", "as", "self", "None", "True", "False",
]

C_TOKENS = [
    "int", "void", "char", "return", "if", "else", "for", "while",
    "struct", "typedef", "static", "const", "include", "define",
]


@dataclass
class FileProfile:
    entropy: float
    unique_bytes: int
    lexical_repetition_rate: float
    token_density: float
    category: str


def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    frequencies: Dict[int, int] = {}
    for byte in data:
        frequencies[byte] = frequencies.get(byte, 0) + 1
    length = len(data)
    entropy = 0.0
    for count in frequencies.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    return entropy


def lexical_repetition_rate(text: str, tokens: List[str]) -> float:
    if not text:
        return 0.0
    total_occurrences = 0
    for token in tokens:
        total_occurrences += len(re.findall(rf"\b{re.escape(token)}\b", text))
    words = len(re.findall(r"\b\w+\b", text))
    if words == 0:
        return 0.0
    return total_occurrences / words


def token_density(text: str, tokens: List[str]) -> float:
    if not text:
        return 0.0
    chars = len(text)
    token_chars = sum(text.count(token) * len(token) for token in tokens)
    return token_chars / chars if chars > 0 else 0.0


def classify_file(path: str, data: bytes) -> str:
    suffix = path.lower()
    if suffix.endswith(".py"):
        if shannon_entropy(data) > 6.5:
            return "py_alta_entropia"
        if len(data) < 10_000:
            return "py_pequeno"
        return "py_medio"
    if suffix.endswith(".c"):
        return "c_medio"
    if suffix.endswith(".log"):
        return "baseline_log"
    return "outro"


def analyze_file(path: str, data: bytes) -> FileProfile:
    text = data.decode("utf-8", errors="replace")
    category = classify_file(path, data)
    tokens = PYTHON_TOKENS if path.endswith(".py") else C_TOKENS if path.endswith(".c") else PYTHON_TOKENS

    return FileProfile(
        entropy=shannon_entropy(data),
        unique_bytes=len(set(data)),
        lexical_repetition_rate=lexical_repetition_rate(text, tokens),
        token_density=token_density(text, tokens),
        category=category,
    )
