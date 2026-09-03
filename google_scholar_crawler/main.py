from datetime import datetime, timezone
import json
import os
from pathlib import Path

from scholarly import scholarly


def write_json(path: Path, payload: dict) -> None:
    """Write JSON atomically so a failed crawl cannot leave partial data."""
    temporary_path = path.with_suffix(f"{path.suffix}.tmp")
    temporary_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary_path.replace(path)


def main() -> None:
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"].strip()
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is empty")

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
    )

    required_fields = ("name", "citedby", "publications")
    missing_fields = [field for field in required_fields if field not in author]
    if missing_fields:
        raise RuntimeError(
            "Google Scholar returned an incomplete profile; missing: "
            + ", ".join(missing_fields)
        )

    publications = author["publications"]
    if not isinstance(publications, list):
        raise RuntimeError("Google Scholar returned an invalid publications payload")

    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in publications
        if publication.get("author_pub_id")
    }

    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    write_json(results_dir / "gs_data.json", author)
    write_json(
        results_dir / "gs_data_shieldsio.json",
        {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(author["citedby"]),
        },
    )

    print(
        f"Fetched {len(author['publications'])} publications and "
        f"{author['citedby']} citations for {author['name']}."
    )


if __name__ == "__main__":
    main()
