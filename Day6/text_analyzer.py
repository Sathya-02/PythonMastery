import re
from collections import Counter

def analyze_text(text: str) -> dict:
    """
    Analyze input text and return comprehensive statistics.
    Useful for NLP pre-processing and content analysis.
    """
    # ── Basic cleaning ────────────────────────────────────────────
    cleaned   = text.strip()
    lower     = cleaned.lower()

    # ── Counts ───────────────────────────────────────────────────
    char_count       = len(cleaned)
    char_no_spaces   = len(cleaned.replace(" ", ""))
    words            = lower.split()
    word_count       = len(words)
    sentences        = [s.strip() for s in re.split(r'[.!?]+', cleaned) if s.strip()]
    sentence_count   = len(sentences)
    paragraphs       = [p.strip() for p in cleaned.split("\n\n") if p.strip()]

    # ── Word frequency ───────────────────────────────────────────
    clean_words = [re.sub(r'[^a-z]', '', w) for w in words]
    clean_words = [w for w in clean_words if w]
    word_freq   = Counter(clean_words)
    top_5       = word_freq.most_common(5)

    # ── Pattern extraction ───────────────────────────────────────
    emails = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', cleaned)
    urls   = re.findall(r'https?://\S+', cleaned)
    dates  = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', cleaned)
    phones = re.findall(r'\+?\d[\d\-]{8,12}\d', cleaned)

    # ── Readability estimate ─────────────────────────────────────
    avg_word_len      = sum(len(w) for w in clean_words) / max(word_count, 1)
    avg_sentence_len  = word_count / max(sentence_count, 1)
    unique_word_ratio = len(word_freq) / max(word_count, 1)

    return {
        "char_count"         : char_count,
        "char_no_spaces"     : char_no_spaces,
        "word_count"         : word_count,
        "sentence_count"     : sentence_count,
        "paragraph_count"    : len(paragraphs),
        "unique_words"       : len(word_freq),
        "unique_word_ratio"  : f"{unique_word_ratio:.2%}",
        "avg_word_length"    : f"{avg_word_len:.2f}",
        "avg_sentence_length": f"{avg_sentence_len:.1f} words",
        "top_5_words"        : top_5,
        "emails_found"       : emails,
        "urls_found"         : urls,
        "dates_found"        : dates,
        "phones_found"       : phones,
    }


def print_report(result: dict) -> None:
    """Pretty-print the analysis report."""
    print("=" * 50)
    print(f"{'📊 TEXT ANALYSIS REPORT':^50}")
    print("=" * 50)

    sections = {
        "📏 Counts": ["char_count", "char_no_spaces", "word_count",
                      "sentence_count", "paragraph_count"],
        "🔠 Vocabulary": ["unique_words", "unique_word_ratio",
                          "avg_word_length", "avg_sentence_length"],
        "🏆 Top 5 Words": ["top_5_words"],
        "🔍 Extracted Data": ["emails_found", "urls_found",
                               "dates_found", "phones_found"],
    }

    for section, keys in sections.items():
        print(f"\n{section}")
        print("-" * 30)
        for key in keys:
            label = key.replace("_", " ").title()
            value = result[key]
            if isinstance(value, list) and value and isinstance(value[0], tuple):
                print(f"  {label}:")
                for word, count in value:
                    print(f"    {word:<15} {count:>3}x")
            else:
                print(f"  {label:<22}: {value}")

    print("\n" + "=" * 50)


# ── Main ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    sample = """
    Python is an amazing programming language. Python is used in AI, ML,
    web development, and data science. Many developers love Python because
    Python is easy to learn and very powerful.

    Contact us at support@python.org or visit https://python.org for docs.
    Release date: 2024-10-07. Call: +91-9876543210.
    Python, python, PYTHON — all count as the same word after lowercasing!
    """

    result = analyze_text(sample)
    print_report(result)