import streamlit as st
from crewai import Agent, Task, Crew

# === Setup Streamlit UI ===
st.set_page_config(page_title="AI Research Article Generator", layout="centered")

st.title("🧠 AI Research Content Pipeline")
st.write("This app uses a team of AI agents to generate an article based on AI trends in 2025.")

if st.button("Run Agents 🚀"):
    with st.spinner("Running agents..."):

        # === Define Agents ===
        research_agent = Agent(
            role="Research Specialist",
            goal="Discover and summarize the latest trends in AI for 2025",
            backstory="An expert in AI who keeps up with all the newest advancements in the field.",
            verbose=True
        )

        analyst_agent = Agent(
            role="Data Analyst",
            goal="Interpret research findings and identify patterns or insights",
            backstory="A skilled analyst who can find valuable insights from complex data.",
            verbose=True
        )

        writer_agent = Agent(
            role="Content Writer",
            goal="Write an engaging and informative article based on the findings",
            backstory="A talented writer who specializes in making technical content accessible and interesting.",
            verbose=True
        )

        # === Define Tasks ===
        research_task = Task(
            description="Research the top 3 most significant AI models or technologies released in 2025.",
            expected_output="A list of 3 key AI models or technologies released in 2025 with short summaries.",
            agent=research_agent
        )

        analysis_task = Task(
            description="Analyze the research findings and identify key trends, patterns, or business implications.",
            expected_output="A brief analysis outlining main trends and their potential business impact.",
            agent=analyst_agent
        )

        writing_task = Task(
            description="Write a 500-word article summarizing the research and analysis in a clear and engaging style.",
            expected_output="A well-written 500-word article suitable for publication.",
            agent=writer_agent
        )

        # === Create Crew ===
        crew = Crew(
            agents=[research_agent, analyst_agent, writer_agent],
            tasks=[research_task, analysis_task, writing_task],
            verbose=True
        )

        # === Run Crew ===
        result = crew.kickoff()
        st.success("Done! ✅")
        st.subheader("📄 Final Output")
        st.write(result)
