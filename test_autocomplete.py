"""
Lab 9: Autocomplete Engine -- starter + verification (single file).

Complete insert, search, starts_with, and find_words_with_prefix
below. TrieNode and the Trie constructor are already provided -- do
not modify them, or anything below the "VERIFICATION SUITE" line.

Run: python test_autocomplete.py
"""

import base64
import hashlib
import sys
from typing import Dict, List, Optional

ASSIGNMENT_ID = "LAB09"


class TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert `word` into the Trie. Must be recursive."""
        # TODO
        raise NotImplementedError

    def search(self, word: str) -> bool:
        """True only if `word` was inserted as a COMPLETE word (not merely a prefix of a longer one)."""
        # TODO
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        """True if any inserted word begins with `prefix` (complete or not)."""
        # TODO
        raise NotImplementedError

    def find_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Recursive: walk to the end of `prefix`, then recursively
        collect every complete word in the subtree below that node.
        Return an alphabetically sorted list. Return [] if `prefix`
        doesn't exist in the Trie at all.
        """
        # TODO
        raise NotImplementedError


# ============================== VERIFICATION SUITE ==============================
# Do not edit below this line.


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS311-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS311|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list = []

    trie = Trie()
    for word in ["CAT", "CAR", "CARD", "CARE", "DOG"]:  # from Part A, Question 2
        trie.insert(word)

    print("Testing search...\n")
    check("search('CAT') is True (inserted complete word)", trie.search("CAT") is True, failures)
    check("search('CA') is False (only a prefix, not inserted as a word)", trie.search("CA") is False, failures)
    check("search('CARDS') is False (not inserted)", trie.search("CARDS") is False, failures)
    check("search('DOG') is True", trie.search("DOG") is True, failures)

    print("\nTesting starts_with...\n")
    check("starts_with('CA') is True", trie.starts_with("CA") is True, failures)
    check("starts_with('CARD') is True (both a prefix and a full word)", trie.starts_with("CARD") is True, failures)
    check("starts_with('ZZZ') is False", trie.starts_with("ZZZ") is False, failures)
    check("starts_with('') is True (empty prefix matches everything)", trie.starts_with("") is True, failures)

    print("\nTesting find_words_with_prefix...\n")
    check(
        "find_words_with_prefix('CAR') == ['CAR', 'CARD', 'CARE'] (from Part A, Q2)",
        trie.find_words_with_prefix("CAR") == ["CAR", "CARD", "CARE"],
        failures,
    )
    check("find_words_with_prefix('DO') == ['DOG']", trie.find_words_with_prefix("DO") == ["DOG"], failures)
    check("find_words_with_prefix('ZZZ') == [] (prefix not in Trie)", trie.find_words_with_prefix("ZZZ") == [], failures)
    check(
        "find_words_with_prefix('') returns all 5 words, sorted",
        trie.find_words_with_prefix("") == ["CAR", "CARD", "CARE", "CAT", "DOG"],
        failures,
    )

    empty_trie = Trie()
    check("empty Trie: search returns False", empty_trie.search("anything") is False, failures)
    check("empty Trie: find_words_with_prefix('') returns []", empty_trie.find_words_with_prefix("") == [], failures)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed. No token issued.")
        return 1

    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
