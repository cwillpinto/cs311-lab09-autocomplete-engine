# Lab 9: Autocomplete Engine
## CS 311: Data Structures & Algorithms (Fall 2026)

### 📱 The Mission
Every time a USI student's thumb hovers over a keyboard, their phone is racing to guess the next word before they finish typing it. That guess isn't magic — it's a **Trie (Prefix Tree)**, a structure built specifically so that "what words start with these letters?" can be answered by walking a handful of nodes instead of scanning an entire dictionary. Your task is to build the engine's brain: a Trie that can store a dictionary and instantly surface every word that shares a given prefix.

---

### Part A: The Proof Detective (50 Points)
**Instructions:** Answer the following questions in a separate document (PDF or Markdown). Use the requested tables and diagrams with brief explanations; no essay is required.

1. **The Space Trade-Off:**
   A naive autocomplete could store 100,000 English words in a Python `set` and, for every keystroke, scan the whole set for matching prefixes.
   - What is the time complexity of that scan-based approach per keystroke, in terms of the number of words `n`?
   - A Trie answers a prefix query in time proportional only to the length of the prefix, `O(L)`. Explain in your own words why sharing common prefixes across words (e.g., "CAT" and "CAR" sharing the "CA" path) is what makes this possible.
2. **Visual Tracing:**
   Insert the following words into an empty Trie, in order: `CAT, CAR, CARD, CARE, DOG`.
   - Draw the resulting Trie, labeling which nodes mark the end of a complete word.
   - List every word your Trie would suggest for the prefix `"CAR"`.
3. **PDC Reasoning:**
   Imagine a shared, campus-wide Trie that thousands of students' phones query simultaneously, and where new slang words get inserted in real time. One thread is walking the Trie to collect autocomplete suggestions for `"pro"` while another thread is inserting the brand-new word `"proctor"`. Could the reading thread ever see a corrupted or half-built path? Where would you place a lock to make this safe without locking the entire Trie for every read?
4. **Balanced Trees — Rotation Tracing:**
   Prefix Trees keep their shape based on the words inserted, but this week's lecture also covers **AVL Trees**, which rebalance themselves after every insertion. Insert the sequence `30, 20, 40, 10, 25, 35, 5` into an empty **AVL Tree**, applying rotations immediately whenever a node's balance factor leaves the range `[-1, 1]`. For each insertion that triggers a rotation:
   - Identify the rotation type (LL, RR, LR, or RL).
   - Draw the tree immediately before and immediately after the rotation.

   > [!CAUTION]
   > **The Brutality Clause:** Rotation tracing is graded as a structural proof. Any rotation step missing a clearly labeled "before" and "after" state, or a misidentified rotation type, will be treated as an unproven claim and scored accordingly.

---

### Part B: The Recursive Coder (50 Points)
**Instructions:** Complete the `insert`, `search`, `starts_with`, and `find_words_with_prefix` methods in the provided `test_autocomplete.py`.

**Requirements:**
1. `insert(word)` must be implemented **recursively**.
2. `search(word)` must return `True` only if `word` was inserted as a **complete** word (not merely present as a prefix of a longer word), and `starts_with(prefix)` must return `True` if any inserted word begins with `prefix`, complete or not.
3. `find_words_with_prefix` must be **recursive**: walk down the Trie to the end of the given prefix, then recursively collect every complete word found in the subtree below that node. Results must be returned as an alphabetically sorted Python list. If the prefix does not exist in the Trie at all, return an empty list rather than raising an exception.
4. **Base Case Required:** Every recursive method (including the collection helper) must correctly terminate at leaf nodes, empty children, or the end of the input string. Remember the **Brutality Clause** — a recursive method with no base case is an automatic 0.
5. **Verification:** Run the script using `python test_autocomplete.py`. If the public checks pass, record the Success Token. The token demonstrates those tested behaviors only; inspect your recursive base cases and explain your design separately.

---

### Lab contract
- **Category:** Virtual Labs (26% of course grade). **Points:** 100 (Part A 50; Part B 50). **Due:** Monday, October 26, 2026; confirm the Blackboard time setting before posting.
- **Starter:** use `test_autocomplete.py` from the instructor's public template at `https://github.com/cwillpinto/cs311-lab09-autocomplete-engine`. Create your own repository for your completed work.
- **Run:** `python test_autocomplete.py` from the repository root.
- **Submit in Blackboard Ultra:** the theory file, your student-owned repository URL and full commit SHA, and the token evidence below. Keep completed code in your repository rather than uploading a separate code file.

### 🚀 Submission
1. `Lab9_Theory.pdf` (or `Lab9_Theory.md`) containing the four written responses and labeled tree diagrams
2. Your student-owned GitHub repository URL and full commit SHA. The repository must contain your completed `test_autocomplete.py`; do not push to the instructor starter repository.
3. The **Success Token** generated by the script, with terminal output or screenshot as evidence.
