from django.test import TestCase

from openai_integration.openai_chat import Chat


class ChatTestCase(TestCase):
    def test_openai_chat(self):
        chat = Chat()
        chat.create_user_message('Hi')
        run = chat.run_assistant()
        chat.wait_until_run_is_completed(run)

        chat.create_user_message('How are you?')
        run = chat.run_assistant()
        chat.wait_until_run_is_completed(run)
        status = chat.check_run_status(run)

        chat.log_message_content()
        self.assertEquals(status.status, 'completed')
