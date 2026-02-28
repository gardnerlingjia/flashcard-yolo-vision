import os
import json
from pathlib import Path

from google import genai
from google.genai import types


# 1. Client from environment variable GEMINI_API_KEY (no need to pass it manually)
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. In your terminal run: export GEMINI_API_KEY='YOUR_KEY'"
    )

client = genai.Client(api_key=API_KEY)

# You can also omit api_key=... and just do:
# client = genai.Client()
# if you rely on the environment variable only.


def analyze_card(image_path: Path) -> dict:
    """
    Send a single flashcard image to Gemini and get structured information back.
    """

    # Read image bytes (we'll send inline bytes → see official docs)
    # https://ai.google.dev/gemini-api/docs/image-understanding
    with image_path.open("rb") as f:
        img_bytes = f.read()

    image_part = types.Part.from_bytes(
        data=img_bytes,
        mime_type="image/png",  # your cards are PNGs; change to image/jpeg if needed
    )

    prompt = """
You see an image of a German vocabulary flashcard.

Extract the following structured fields:

- language: always "German" for these cards
- card_type: always "vocabulary" for these cards
- article: the grammatical article (e.g. "der", "die", "das"), or null if none
- lemma: the main base form of the word (without article)
- plural: the plural form in angle brackets (e.g. from "<T-Shirts>" → "T-Shirts"), or null if none
- part_of_speech: e.g. "Nomen", "Verb", "Adjektiv"
- raw_text: the full text you can see on the card (verbatim)

Return ONLY valid JSON, no explanation, no markdown, no code fences.
Use this JSON schema:

{
  "language": "<string>",
  "card_type": "<string>",
  "article": "<string or null>",
  "lemma": "<string>",
  "plural": "<string or null>",
  "part_of_speech": "<string or null>",
  "raw_text": "<string>"
}
"""

    # New SDK call style:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",  # or e.g. "gemini-2.5-flash"
        contents=[
            image_part,   # image first
            prompt,       # then the instruction
        ],
    )

    raw = response.text.strip()

    # Try to parse JSON (ideal case)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: if model returns not-perfect JSON, keep raw text
        data = {
            "language": None,
            "side_type": None,
            "text": raw,
        }

    return data


def main():
    # 3. Test with a single card first
    single_card = Path("examples/output/card_0.png")
    if not single_card.exists():
        raise FileNotFoundError(f"Test image not found: {single_card}")

    print(f"Analyzing single card: {single_card}")
    result = analyze_card(single_card)
    print("Result for card_0.png:")
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # 4. Process all card_*.png files and save results
    cards_dir = Path("examples/output")
    outputs = []

    for img_path in sorted(cards_dir.glob("card_*.png"))[:3]:
        print(f"\nAnalyzing {img_path.name} ...")
        data = analyze_card(img_path)
        data["image_name"] = img_path.name
        outputs.append(data)

    # Save results as JSONL (one JSON object per line)
    out_path = Path("data") / "gemini_cards.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        for record in outputs:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"\nSaved {len(outputs)} records to {out_path}")


if __name__ == "__main__":
    main()