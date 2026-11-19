import unittest
from jobs.services import JobBoardService
from jobs.views import handle_create_job, handle_submit_application

class TestJobBoard(unittest.TestCase):
    def setUp(self):
        self.svc = JobBoardService()

    def test_post_and_list_job(self):
        job = self.svc.post_job("Software Engineer Intern", "Google", "Remote", "Python/Java", "$45/hr")
        self.assertEqual(job.id, 1)
        self.assertEqual(job.title, "Software Engineer Intern")
        active = self.svc.list_jobs()
        self.assertEqual(len(active), 1)

    def test_submit_application(self):
        job = self.svc.post_job("Backend Engineer", "Stripe", "San Francisco", "Distributed Systems", "$160k")
        app = self.svc.apply_to_job(job.id, "Divya Sree Bestha", "divyasreebestha161@gmail.com", "https://portfolio.dev/resume.pdf")
        self.assertIsNotNone(app)
        self.assertEqual(app.status, "PENDING")
        apps = self.svc.get_applications_for_job(job.id)
        self.assertEqual(len(apps), 1)

if __name__ == "__main__":
    unittest.main()
