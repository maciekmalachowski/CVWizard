from taipy.gui import Gui
import taipy.gui.builder as tgb
from llama_index.llms.openai import OpenAI
# from scrapper import get_data
from cv_reader import read_cv

# Initialize state variables
fselector = None
file_path = None
file_name = None
ivalue = None

# Function to update the file selector partial dynamically
def on_change(state, name, val):
    if name == "fselector":
        fname = list(val.split("\\")[-1].split('.'))
        state.file_name = f"{fname[0]}.{fname[-1]}"
        with tgb.Page() as changed_page:
            tgb.file_selector(
                content="{fselector}",
                label=state.file_name,
                extensions=".pdf",
                drop_message="Drop here to Upload",
                class_name="fullwidth",
            )
            tgb.part(partial="{url_input}")
        state.file_selector_partial.update_content(state, changed_page)
    
    if name == "ivalue":
        activation = False if not val else True
        with tgb.Page() as change_button:
            tgb.button("Search for offer", on_action=read_cv, class_name="fullwidth plain", active=activation)
        state.search_button.update_content(state, change_button)

    print(name, val)

# Define the page
with tgb.Page() as page:
    with tgb.part(class_name="text-center"):
        tgb.text("Check how good is your CV", class_name="h1")
    with tgb.part(class_name="container align_columns_center"):
        with tgb.part(class_name="card"):
            tgb.part(partial="{file_selector_partial}")
            

# Initialize the GUI
if __name__ == "__main__":
    gui = Gui(page)
    # Initialize partials
    file_selector_partial = gui.add_partial("<|{fselector}|file_selector|label=Upload your CV|extensions=.pdf|drop_message=Drop here to Upload|class_name=fullwidth|>")
    url_input = gui.add_partial("<|{ivalue}|input|label=Paste the url link to the job posting.|class_name=fullwidth|><|part|partial={search_button}|>")
    search_button = gui.add_partial("<|Search for offer|button|on_action=read_cv|class_name=fullwidth plain|active=False|>")
    # Run the GUI
    gui.run(title="🧙‍♂️CVWizard", use_reloader=True)
