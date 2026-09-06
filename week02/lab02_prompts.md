# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI. A non-sensitive verification detail is
that the command accepted the `-p` prompt option and returned a Python implementation.

### Antigravity CLI

I installed and authenticated Antigravity CLI. A non-sensitive verification detail is
that the `agy -p` command accepted the shared prompt and returned a Python implementation.

## Shared task

### Shared prompt

I submitted this exact prompt to both CLI tools:

```text
Write a Python function called count_vowels that takes a string and returns the count of vowels (a, e, i, o, u). Don't count y. Ignore case.
```

### Copilot CLI observations

Copilot suggested a function with a string parameter and an integer return annotation. Its
implementation lowercased the entire input and counted characters that appeared in the
literal string `aeiou`. This correctly handles uppercase vowels and naturally ignores y,
consonants, spaces, punctuation, and digits. I questioned whether the generator expression
would return an integer, so I verified that `sum` adds one for each matching character and
returns zero for an empty string. I also checked examples containing mixed case and no vowels.

### Antigravity CLI observations

Antigravity suggested a shorter implementation using `sum` over boolean comparisons. It
lowercased each character before checking membership in `aeiou`, so the result remains
case-insensitive and y is not counted. I considered whether summing booleans is valid Python;
it is, because `True` and `False` behave as one and zero in numeric addition. I would still
verify empty input, punctuation, repeated vowels, uppercase text, and words such as rhythms
that contain y but no counted vowels.

### Comparison

Both responses were correct and used the same essential algorithm: inspect each character,
normalize case, test membership in the five allowed vowels, and add the matches. Copilot's
generator expression was slightly more explicit because it yields one for matching
characters, which makes the counting behavior easy for a beginner to read. Antigravity's
boolean-sum version was more concise, but it relies on understanding that booleans are
subclasses of integers in Python. Neither response counted y, and both handled empty strings
without special cases. I selected the Copilot-style expression for the repository because its
intent is especially clear while remaining compact. I also verified the result against the
provided tests and the function contracts for the other two functions.

## Test-guided implementation

The initial implementation contained only `count_vowels`, so test collection failed before
the behavioral tests could run because the test module also imported `make_greeting` and
`is_even`. The lab contract explicitly required all three functions, so I added
`make_greeting` using an f-string that preserves the supplied name exactly, including an
empty name or spaces. I added `is_even` using `number % 2 == 0`, which works for positive,
zero, and negative integers. After that revision, all function behavior tests passed:
greetings matched the required punctuation, even and odd values returned the expected
booleans, and vowel counting handled mixed case, y, consonants, and empty text. The final
code therefore implements each documented contract rather than merely handling one example.

## Preferred tool combination

A browser chat is useful for exploring an idea conversationally and asking follow-up
questions, especially when I want explanations or several alternatives. GitHub Copilot in
VS Code is convenient when the surrounding files, symbols, and diagnostics matter because
the suggestion appears beside the code being edited. Copilot CLI is efficient for a focused
prompt from the repository terminal and fits well with quick command-line experiments.
Antigravity CLI provides a useful independent comparison, which can reveal differences in
style or assumptions. I currently prefer VS Code with Copilot for multi-file work, plus
Copilot CLI for small isolated tasks and tests. I would change that choice for a task where
an independent second answer is important, or where browser-based discussion is better for
learning an unfamiliar concept before editing code.
