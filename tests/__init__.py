import unittest
from app import create_app
from flask_testing import TestCase


class ContextTestCase(TestCase):
    """
    Handles context test cases for the application
    """
    render_templates = True

    def create_app(self):
        app = create_app("testing")
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def _pre_setup(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def __call__(self, result=None):
        try:
            self._pre_setup()
            super(ContextTestCase, self).__call__(result)
        finally:
            self._post_teardown()

            # def _post_teardown(self):
            #     if getattr(self, '_ctx') and self._ctx is not None:
            #         self._ctx.pop()
            #     del self._ctx


class BaseTestCase(ContextTestCase):
    """
    Base test case for application
    """

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()

        # self.create_user_account()
        # self.add_file()

    def tearDown(self):
        self.app_context.pop()

    # @staticmethod
    # def create_user_account():
    #     """
    #     Create a fictional Author for testing
    #     :return:
    #     """
    #     author = AuthorAccount.query.filter_by(email="guydemaupassant@hadithi.com").first()
    #     if author is None:
    #         try:
    #             author = AuthorAccount(full_name="Guy De Maupassant", email="guydemaupassant@hadithi.com",
    #                                    password="password", registered_on=datetime.now())
    #             db.session.add(author)
    #         except IntegrityError as ie:
    #             print(ie)
    #             db.session.rollback()
    #     return author
    #
    # def login(self):
    #     """
    #     Login in the user to the testing app
    #     :return: The authenticated user for the test app
    #     """
    #     return self.client.post(
    #         url_for("auth.login"),
    #         data=dict(email='guydemaupassant@hadithi.com', password='password', confirm='password'),
    #         follow_redirects=True
    #     )
    #
    # def add_file(self):
    #     """
    #     Adds a dummy story to the database
    #     :return:
    #     """
    #     author = self.create_user_account()
    #     story = Story.query.filter_by(author_id=author.id).first()
    #     if story is None:
    #         try:
    #             story = Story(title="Gotham in flames", tagline="Dark city catches fire",
    #                           category="Fiction", content="", author_id=author.id)
    #             db.session.add(story)
    #         except IntegrityError as e:
    #             print(e)
    #             db.session.rollback()
    #     return story
    #
    # def save_user_file(self, story_id):
    #     return self.client.get(
    #         url_for("story.save_story", app_id=story_id),
    #         follow_redirects=True)


if __name__ == "__main__":
    unittest.main()
