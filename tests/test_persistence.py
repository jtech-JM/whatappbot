import os
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from persistence import Persistence
from schemas import ResearchBriefPayload
from datetime import datetime


def test_save_session_creates_file(tmp_path):
    p = Persistence(data_dir=str(tmp_path))
    brief = ResearchBriefPayload(
        timestamp=datetime.utcnow(),
        topic="T",
        source_grounding=[{"source_url":"https://example.com","extracted_fact":"f","metric_data":"m"}],
        core_breakthroughs=[{"title":"t","technical_summary":"s"}],
    )
    session_id = "sess123"
    path = p.save_session(session_id, brief, "draft content", {"evaluation_status": "APPROVED"})
    assert os.path.exists(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["session_id"] == session_id
    assert data["brief"]["topic"] == "T"
    assert data["draft"] == "draft content"
