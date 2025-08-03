import gradio as gr
from src.mental_health_bot.crew import create_crew

crew = create_crew()

def mental_health_support(user_input):
    result = crew.kickoff(inputs={'user_input': user_input})
    return result

iface = gr.Interface(
    fn=mental_health_support,
    inputs=gr.Textbox(lines=4, label="How are you feeling today?"),
    outputs=gr.Textbox(label="Support Response"),
    title="🧘‍♀️ Mental Health Support Bot",
    description="Enter how you're feeling and get support + a personalized self-care recommendation."
)

if __name__ == "__main__":
    iface.launch()
