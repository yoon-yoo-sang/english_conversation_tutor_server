import logging
import os
import time

from dotenv import load_dotenv
from openai import OpenAI
from openai.pagination import SyncCursorPage
from openai.types.beta import Assistant, Thread
from openai.types.beta.threads import Run, ThreadMessage

from openai_integration.choices import OpenAIModel


class Chat(OpenAI):
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        super().__init__(api_key=api_key)

        instruction = """
            I want to learn English conversation, and you are an English conversation teacher. 
            You can talk to me in English, but point me out if I have an awkward conversation.
        """

        try:
            self.english_tutor: Assistant = self.beta.assistants.create(
                name="English Tutor",
                instructions=instruction,
                tools=[{"type": "code_interpreter"}],
                model=OpenAIModel.NEW_GPT4.value
            )

            self.thread: Thread = self.beta.threads.create()
        except Exception as e:
            logging.error(e)

    def create_user_message(self, content) -> ThreadMessage:
        try:
            message: ThreadMessage = self.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=content
            )
            return message
        except Exception as e:
            logging.error(e)

    def run_assistant(self) -> Run:
        try:
            run: Run = self.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.english_tutor.id,
            )
            return run
        except Exception as e:
            logging.error(e)

    def check_run_status(self, run) -> Run:
        try:
            run: Run = self.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )
            return run
        except Exception as e:
            logging.error(e)

    def list_messages(self) -> SyncCursorPage[ThreadMessage]:
        try:
            messages: SyncCursorPage[ThreadMessage] = self.beta.threads.messages.list(
                thread_id=self.thread.id
            )
            return messages
        except Exception as e:
            logging.error(e)

    def log_message_content(self):
        messages = self.list_messages().data
        messages.reverse()
        for message in messages:
            print(message.role, ":", message.content[0].text.value)

    def wait_until_run_is_completed(self, run):
        try:
            while True:
                status = self.check_run_status(run)
                if status.status == 'completed':
                    break
                elif status.status == 'failed':
                    raise Exception(status.error)
                time.sleep(1)
        except Exception as e:
            logging.error(e)
