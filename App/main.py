from taipy.gui import Gui, State, notify
import taipy.gui.builder as tgb
from llama_index.llms.openai import OpenAI
from scrapper import get_data
from cv_reader import read_cv

# Initialize state variables
fselector = None
file_path = None
file_name = None
ivalue = None
offer_link = None
correct_cv = None
pdf_engine = None
scrapped_data = None

# Call read_cv to analize user's CV
def call_read_cv(state: State):
    try:
        state.pdf_engine = read_cv(state.file_path)        
        state.correct_cv = True
    except:
        state.correct_cv = False
        notify(state, notification_type="error", message="Something is wrong with your CV")
    finally:
        state.progress_text.update_content(state, "")
        notify(state, notification_type="success", message="CV successfully analyzed")

# Call get_data to scrape given url for job posting skills and description
def call_get_data(state: State):
    try:
        state.scrapped_data = get_data(state.offer_link)
    except:
        notify(state, notification_type="error", message="Wrong link")
    finally:
        notify(state, notification_type="success", message="Job details are ready")


# Function to update the file selector partial dynamically
def on_change(state, name, val):
    if name == "fselector":
        fname = list(val.split("\\")[-1].split('.'))
        state.file_name = f"{fname[0]}.{fname[-1]}"
        state.file_path = val
        with tgb.Page() as changed_page:
            tgb.file_selector(
                content="{fselector}",
                label=state.file_name,
                extensions=".pdf",
                drop_message="Drop here to Upload",
                class_name="fullwidth",
                notify=False,
                on_action=call_read_cv
            )
            tgb.part(partial="{progress_text}")
            if state.correct_cv:
                tgb.part(partial="{url_input}")
        state.file_selector_partial.update_content(state, changed_page)
    
    if name == "ivalue":
        state.offer_link = val
        with tgb.Page() as change_button:
            tgb.button("Search for offer", on_action=call_get_data, class_name="fullwidth plain", active=bool(val))
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
    file_selector_partial = gui.add_partial("<|{fselector}|file_selector|label=Upload your CV|extensions=.pdf|drop_message=Drop here to Upload|class_name=fullwidth|notify=False|on_action=call_read_cv|>")
    url_input = gui.add_partial("<|{ivalue}|input|label=Paste the url link to the job posting.|class_name=fullwidth|><|part|partial={search_button}|>")
    search_button = gui.add_partial("<|Search for offer|button|class_name=fullwidth plain|active=False|>")
    progress_text = gui.add_partial("<|⏳Processing...|text|>")
    # Run the GUI
    gui.run(title="🧙‍♂️CVWizard", use_reloader=True)
