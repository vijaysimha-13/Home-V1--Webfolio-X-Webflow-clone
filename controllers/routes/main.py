from .atri import Atri
from fastapi import Request, Response
from atri_utils import *


def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.header_name_box.styles.fontWeight = 900
    at.past_projects.styles.fontWeight = 900
    at.TextBox27.styles.fontWeight = 900
    at.TextBox28.styles.fontWeight = 700
    at.TextBox30.styles.fontWeight = 700
    at.TextBox32.styles.fontWeight = 700
    at.TextBox34.styles.fontWeight = 700
    at.TextBox36.styles.fontWeight = 700
    at.TextBox38.styles.fontWeight = 700
    at.TextBox44.styles.fontWeight = 700
    at.TextBox46.styles.fontWeight = 700
    at.TextBox52.styles.fontWeight = 900
    at.TextBox57.styles.fontWeight = 900
    at.TextBox59.styles.fontWeight = 900
    at.TextBox104.styles.fontWeight = 900

    pass


def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass


def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    pass
