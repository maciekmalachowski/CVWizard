from taipy.gui import Gui
import taipy.gui.builder as tgb
import tempfile
import os
from llama_index.llms.openai import OpenAI
# from scrapper import get_data
from cv_reader import read_cv

selector = None
value = None

def on_change(state, name, val):
    # print(name, val)

    if name == "selector":
        state.file_path = val
        state.file_name = val.split("/")[-1]
        state.upload = True
    
    if name == "value":
        state.search = True

with tgb.Page() as page:
    with tgb.part(class_name="text-center"):
        tgb.text("Check how good is your CV", class_name="h1")
    with tgb.part(class_name="container align_columns_center"):
        with tgb.part(class_name="card"):
            tgb.file_selector(
                content="{selector}",
                label="Upload your CV",
                extensions=".pdf",
                drop_message="Drop here to Upload",
                class_name="fullwidth",
            )
        with tgb.part(class_name="card"):
            tgb.input("{value}", label="Paste the url link to the job posting.", class_name="fullwidth")
            if "{search}":
                tgb.button("Search for offer", on_action=read_cv, class_name="fullwidth plain")

if __name__ == "__main__":
    Gui(page).run(title="🧙‍♂️CVWizard", use_reloader=True)
