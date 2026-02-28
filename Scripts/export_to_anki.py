import json
import csv
from pathlib import Path


def main():
    input_path = Path("data/gemini_cards.jsonl")
    output_path = Path("data/anki_flashcards.csv")

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    records = []

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    if not records:
        print("No records found.")
        return

    with output_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Optional: Header (Anki braucht keinen, aber gut für Lesbarkeit)
        writer.writerow(["Front", "Back"])

        for r in records:
            article = r.get("article") or ""
            lemma = r.get("lemma") or ""
            plural = r.get("plural") or ""
            pos = r.get("part_of_speech") or ""

            front = f"{article} {lemma}".strip()
            back = f"Plural: {plural} | POS: {pos}"

            writer.writerow([front, back])

    print(f"Anki CSV written to: {output_path}")
    print(f"{len(records)} flashcards exported.")


if __name__ == "__main__":
    main()