from langchain_core.tools import tool
# from langchain_core.runnables import RunnableConfig

from api.myemailer.sender import send_mail
from api.myemailer.inbox_reader import read_inbox
from api.ai.services import generate_email_message

@tool
# def research_email(query:str, config: RunnableConfig):
def research_email(query:str):
    """
     TODO LangChain 的 tool 宣告，要附加使用的註解
    Perform research based on the query

    Arguments:
    - query: str - Topic of research
    """
    # print(config)
    response = generate_email_message(query)
    msg = f"Subject {response.subject}:\nBody: {response.content}"
    return msg

@tool
def send_me_email(subject:str, content:str) -> str:
    """
     TODO LangChain 的 tool 宣告，要附加使用的註解
    Send an email to myself with a subject and content.

    Arguments:
    - subject: str - Text subject of the email
    - content: str - Text body content of the email
    """
    try:
        send_mail(subject=subject, content=content)
    except:
        return "Not sent"
    return "Sent email"


@tool
def get_unread_emails(hours_ago:int=48) -> str:
    """
    TODO LangChain 的 tool 宣告，要附加使用的註解 
    Read all emails from my inbox within the last N hours

    Arguments:
    - hours_ago: int = 24 - number of hours ago to retrieve in the inbox
    
    Returns:
    A string of emails separated by a line "----"   
    """
    try:
        emails = read_inbox(hours_ago=hours_ago, verbose=False)
    except:
        return "Error getting latest emails"
    cleaned = []

    for email in emails:
        data = email.copy()
        if "html_body" in data:
            data.pop('html_body')
        msg = ""
        for k, v in data.items():
            msg += f"{k}:\t{v}"
        cleaned.append(msg)
    return "\n-----\n".join(cleaned)[:500]
