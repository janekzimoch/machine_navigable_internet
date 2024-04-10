import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def call_openai(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are part of a system that clarifies and summarises content and fuinctioanlity of a website. you are presented with a html or accesability tree representqation of a page and your job is to summarise what the page does."},
                {"role": "user", "content": prompt}
            ]
    )
    return completion.choices[0].message["content"]


def get_changes_descritpion(button_label, old_page, new_page, html=False):
    representation = 'HTML' if html else 'Accesability Tree'
    prompt = f"""
A user just presed a button on a page that may have introduced some changes to a web page. Below are {representation} representation of a webpage before and after the action (note a button could lead to an entirely new webpage). Your job is to compare the old and new webpage and describe what is the functionality of the button (infering that from the change of the pages). If the button just opened a completely new webpage describe functionality of the button in context of what the new page allows user to achieve. On the other hand, if the button just opened some drop down menu with a list of options (which resulted in a small change to the original page) describe what those changes were. 


Button that was clicked had label: {button_label}
Here is the old page: {old_page}
Here is the new page: {new_page}

Output button functioanlity description. Note when we present this descritpion to the user, they won't have had actually clicked it yet, we want to show them what would happen if they click it.
 Description:
"""
    return call_openai(prompt)
