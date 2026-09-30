import unittest

from progress import show_progress
from storage import load_data, save_data


class TestFitnessTracker(unittest.TestCase):

    def test_data_structure(self):
        data = load_data()

        self.assertIn("workouts", data)
        self.assertIn("habits", data)

    def test_save_and_load(self):
        test_data = {
            "workouts": [],
            "habits": []
        }

        save_data(test_data)

        loaded_data = load_data()

        self.assertEqual(test_data, loaded_data)


if __name__ == "__main__":
    unittest.main()