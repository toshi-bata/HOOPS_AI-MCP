import unittest
from unittest.mock import patch

import main


class FakeColumn(list):
    def astype(self, target_type):
        return [target_type(value) for value in self]


class FakeDatasetExplorer:
    def get_file_list(self, group, where):
        self.assert_group(group)
        self.assert_label_filter(where)
        return [101, "202", 303]

    def get_file_info_all(self):
        return {
            "id": FakeColumn([101, 202]),
            "description": ["bracket_a.stp", "housing_b.stp"],
        }

    @staticmethod
    def assert_group(group):
        if group != "Labels":
            raise AssertionError(f"Unexpected group: {group}")

    @staticmethod
    def assert_label_filter(where):
        if not where({"face_labels": 18}):
            raise AssertionError("Expected feature name to resolve to face label 18.")
        if where({"face_labels": 24}):
            raise AssertionError("Unexpected match for a different face label.")


class MFRSearchTests(unittest.TestCase):
    def test_search_MFR_file_names_returns_file_names_for_feature_name(self):
        with patch.object(main, "MFR_dataset_explorer", FakeDatasetExplorer()):
            file_names = main.search_MFR_file_names("circular blind step")

        self.assertEqual(file_names, ["bracket_a.stp", "housing_b.stp"])


if __name__ == "__main__":
    unittest.main()
