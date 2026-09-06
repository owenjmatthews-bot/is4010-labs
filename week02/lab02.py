def make_greeting(name: str) -> str:
	"""Return exactly 'Hello, NAME!' using the supplied name."""
	return f"Hello, {name}!"


def is_even(number: int) -> bool:
	"""Return True when number is even and False otherwise."""
	return number % 2 == 0


def count_vowels(text: str) -> int:
	"""Return the number of vowels in text, ignoring case."""
	return sum(1 for char in text.lower() if char in "aeiou")
