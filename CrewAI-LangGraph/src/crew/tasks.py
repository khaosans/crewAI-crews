from crewai import Task
from textwrap import dedent
import logging

class EmailFilterTasks:
    def filter_emails_task(self, agent, emails):
        return Task(
            description=dedent(f"""\
                Analyze a batch of emails and filter out
                non-essential ones such as newsletters, promotional content, and notifications.

                Use your expertise in email content analysis to distinguish
                important emails from the rest, paying attention to the sender and avoiding invalid emails.

                Make sure to filter the messages actually directed at the user and avoid notifications.

                EMAILS
                -------
                {emails}

                Your final answer MUST be the relevant thread_ids and the sender, presented in bullet points.
                """),
            agent=agent
        )

    def action_required_emails_task(self, agent):
        return Task(
            description=dedent("""\
                For each email thread, pull and analyze the complete threads using only the actual Thread ID.
                Understand the context, key points, and the overall sentiment
                of the conversation.

                Identify the main query or concerns that need to be
                addressed in the response for each.

                Your final answer MUST be a list for all emails with:
                - the thread_id
                - a summary of the email thread
                - a highlight of the main points
                - identification of the user and who they will be responding to
                - communication style in the thread
                - the sender's email address.
                """),
            agent=agent,
            run=lambda inputs: self._process_threads(inputs, agent)
        )

    def _process_threads(self, inputs, agent):
        results = []
        for thread_id in inputs['thread_ids']:
            try:
                thread_data = agent.use_tool('get_gmail_thread', {'thread_id': thread_id})
                if not thread_data:
                    logging.error(f"No data found for Thread ID: {thread_id}")
                    continue

                # Process the thread data
                # Extract necessary information here...

                results.append({
                    'thread_id': thread_id,
                    # Add the extracted information here...
                })

            except Exception as e:
                logging.error(f"Error processing Thread ID: {thread_id}: {str(e)}")
                continue

        return results

    def draft_responses_task(self, agent):
        return Task(
            description=dedent(f"""\
                Based on the action-required emails identified, draft responses for each.
                Ensure that each response is tailored to address the specific needs
                and context outlined in the email.

                - Assume the persona of the user and mimic the communication style in the thread.
                - Feel free to do research on the topic to provide a more detailed response, IF NECESSARY.
                - IF research is necessary, do it BEFORE drafting the response.
                - If you need to pull the thread again, do it using only the actual Thread ID.

                Use the tool provided to draft each of the responses.
                When using the tool, pass the following input:
                - to (sender to be responded to)
                - subject
                - message

                You MUST create all drafts before sending your final answer.
                Your final answer MUST be a confirmation that all email responses have been successfully drafted.
                """),
            agent=agent
        )
