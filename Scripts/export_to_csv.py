import json
import csv
from pathlib import Path


def main():
    input_path = Path("data/gemini_cards.jsonl")
    output_path = Path("data/gemini_cards.csv")

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    records = []

    # 1️⃣ JSONL einlesen
    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                print("Skipping invalid JSON line:")
                print(line)

    if not records:
        print("No valid records found.")
        return

    # 2️⃣ CSV schreiben
    fieldnames = [
        "image_name",
        "language",
        "card_type",
        "article",
        "lemma",
        "plural",
        "part_of_speech",
        "raw_text",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            writer.writerow({
                "image_name": record.get("image_name"),
                "language": record.get("language"),
                "card_type": record.get("card_type"),
                "article": record.get("article"),
                "lemma": record.get("lemma"),
                "plural": record.get("plural"),
                "part_of_speech": record.get("part_of_speech"),
                "raw_text": record.get("raw_text"),
            })

    print(f"CSV successfully written to: {output_path}")
    print(f"{len(records)} records exported.")


if __name__ == "__main__":
    main()