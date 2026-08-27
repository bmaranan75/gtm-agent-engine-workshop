import unittest

from gtm_agent import data_service


class UpdateProspectInfoTest(unittest.TestCase):
    def test_update_persists_technology(self):
        prospect_id = "LEAD-71001"
        original_tech_stack = list(data_service.PROSPECTS[prospect_id]["tech_stack"])
        data_service._PROFILES.pop(prospect_id, None)
        try:
            data_service.update_prospect_info(prospect_id, "Terraform")
            self.assertIn("Terraform", data_service.fetch_tech_stack(prospect_id))
        finally:
            data_service.PROSPECTS[prospect_id]["tech_stack"] = original_tech_stack
            data_service._PROFILES.pop(prospect_id, None)


if __name__ == "__main__":
    unittest.main()
