import json
import os

os.environ.setdefault("OPENAI_API_KEY", "test-key")

from gtm_agent.gtm_agent import build_prospect_profile, get_prospect
from gtm_agent.gtm_records import PROSPECTS


def test_prospect_tools_exclude_billing_fields():
    sensitive_keys = (
        "tax_id",
        "date_of_birth",
        "card_on_file",
        "credit_check_ref",
        "billing_qualification",
    )

    for prospect_id in PROSPECTS:
        results = [
            get_prospect.invoke({"prospect_id": prospect_id}),
            build_prospect_profile.invoke({"prospect_id": prospect_id}),
        ]
        serialized = json.dumps(results)
        assert all(key not in serialized for key in sensitive_keys)
