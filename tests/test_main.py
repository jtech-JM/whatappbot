import os
import sys
# Ensure repository root is importable when running tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import run_workflow


def test_run_workflow_creates_output(tmp_path):
    out = tmp_path / "final_output.md"
    evaluation, path = run_workflow("Test Topic", output_file=str(out), verbose=False)
    assert path == str(out)
    if evaluation.evaluation_status == "APPROVED":
        assert out.exists()
    else:
        # If rejected, no file should be created
        assert not out.exists()


def test_research_brief_schema():
    from schemas import ResearchBriefPayload
    from datetime import datetime

    brief = ResearchBriefPayload(
        timestamp=datetime.utcnow(),
        topic="T",
        source_grounding=[{"source_url":"https://example.com","extracted_fact":"f","metric_data":"m"}],
        core_breakthroughs=[{"title":"t","technical_summary":"s"}],
    )
    assert brief.topic == "T"
