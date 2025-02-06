from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from dotenv import load_dotenv

def get_insights(cv_data, job_data):
    load_dotenv()
    # Extract relevant details
    cv_summary = cv_data.get("summary", "No summary available.")
    cv_skills = set(cv_data.get("skills", []))
    job_title = job_data.get("title", "No title available.")
    job_description = job_data.get("description", "No description available.")
    job_skills = set(job_data.get("skills", []))
    
    # Find matched and missing keywords
    matched_keywords = list(cv_skills & job_skills)
    missing_keywords = list(job_skills - cv_skills)
    
    # Calculate alignment score
    alignment_score = round((len(matched_keywords) / len(job_skills)) * 100, 0) if job_skills else 0
    
    # Generate AI-powered improvement suggestions
    llm = OpenAI(model="gpt-4-turbo")
    messages = [
        ChatMessage(role="system", content="You are an expert career advisor helping candidates tailor their CV and skills to align with job requirements. Focus on providing actionable suggestions directly without introductory phrases."),
        
        # Introduce the job title and description
        ChatMessage(role="user", content=f"I'm applying for a job as a {job_title}. The job description is as follows: {job_description}"),
        ChatMessage(role="assistant", content=f"To strengthen your CV for the {job_title} role, emphasize your experience in machine learning, Python, and relevant technologies like TensorFlow and Kubernetes. If you have experience with scalable ML models or cloud platforms like AWS or Azure, make sure to highlight that. If not, you could consider taking courses or working on related projects to demonstrate your readiness."),

        # Introduce your CV summary and skills
        ChatMessage(role="user", content=f"Here's a summary of my CV: {cv_summary}. These are the key skills I have listed: {', '.join(cv_skills)}."),
        ChatMessage(role="assistant", content=f"Your CV summary is strong, showcasing relevant experience in machine learning. To further strengthen it, ensure that your skills like Python, Pandas, Docker, and Scikit-learn are highlighted throughout your CV. If you have experience with deploying models or using these technologies in real-world projects, be sure to mention that, as it will align well with the job requirements."),

        # Share the job requirements (skills)
        ChatMessage(role="user", content=f"The job requires the following skills: {', '.join(job_skills)}."),
        ChatMessage(role="assistant", content=f"Focus on adding experience with TensorFlow and Kubernetes to your CV. If you lack these skills, consider learning through tutorials or personal projects to showcase your ability to work with these technologies. Demonstrating that you are proactive in learning new skills is a valuable trait for employers."),

        # Mention missing skills and ask for advice
        ChatMessage(role="user", content=f"Based on my current CV, I'm missing these key skills: {', '.join(missing_keywords)}. Could you provide personalized suggestions to help me improve my CV and better match the job? Specifically, how can I work on my missing skills and enhance my profile? Thank you!"),
        ChatMessage(role="assistant", content=f"To address the missing skills like TensorFlow, Kubernetes, and SQL, try to gain hands-on experience through online courses, tutorials, or personal projects. These will help you build a portfolio that demonstrates your capabilities. Consider focusing on completing certifications in these technologies or contributing to open-source projects."),

        # Job description wrap-up
        ChatMessage(role="user", content=f"The job description I mentioned earlier is very important to me, so I'd appreciate suggestions tailored to it."),
        ChatMessage(role="assistant", content=f"Absolutely! Focusing on cloud computing, scalable ML models, and expertise in Python and TensorFlow will make your CV stand out. Don't forget to mention any relevant experiences you've had with cloud platforms and model deployment. If you are lacking hands-on experience, building small projects in these areas will help close the gap.")
    ]

    response = llm.chat(messages)

    return {
        "alignmentScore": alignment_score,
        "matchedKeywords": matched_keywords,
        "missingKeywords": missing_keywords,
        "suggestions": response.message.content if response else "No suggestions available."
    }

# Example Usage
cv_insights = {
    "summary": "John Doe is a software engineer...",
    "skills": ["Python", "HTML", "Numpy", "Pandas", "Docker", "Java", "Jupyter Notebook", "LLMs", "Langchain", "LlamaIndex", "AutoML", "Scikit-learn", "Hugging Face"],
    "languages": ["English", "Spanish"]
}

job_data = {
    "title": "Machine Learning Engineer",
    "skills": ["Python", "TensorFlow", "Pandas", "Docker", "Kubernetes", "Scikit-learn", "SQL"],
    "description": "Looking for an ML Engineer with experience in Python, TensorFlow, and Kubernetes."
}

print(get_insights(cv_insights, job_data))
