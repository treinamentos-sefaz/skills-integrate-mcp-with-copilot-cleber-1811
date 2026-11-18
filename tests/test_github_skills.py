import unittest

from fastapi import HTTPException

from src.app import activities, get_activities, signup_for_activity, unregister_from_activity


class GitHubSkillsTest(unittest.TestCase):
    def test_activity_is_available_for_signup(self):
        activity = get_activities()["GitHub Skills"]
        self.assertIn("schedule", activity)
        self.assertIn("max_participants", activity)

        email = "github-skills-test@mergington.edu"
        self.assertNotIn(email, activity["participants"])
        try:
            signup_for_activity("GitHub Skills", email)
            self.assertIn(email, get_activities()["GitHub Skills"]["participants"])
            with self.assertRaises(HTTPException) as error:
                signup_for_activity("GitHub Skills", email)
            self.assertEqual(error.exception.status_code, 400)
        finally:
            if email in activities["GitHub Skills"]["participants"]:
                unregister_from_activity("GitHub Skills", email)


if __name__ == "__main__":
    unittest.main()
