# from gpt_researcher import agent
from gpt_researcher.agent import GPTResearcher
import asyncio
from datetime import datetime

# Start time
start_time = datetime.now()

async def get_report(query: str, report_type: str, report_source: str):
    researcher = GPTResearcher(query, report_type, report_source)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    
    # Get additional information
    source_urls = researcher.get_source_urls()
    research_context = researcher.get_research_context()
    research_costs = researcher.get_costs()
    research_images = researcher.get_research_images()
    research_sources = researcher.get_research_sources()
    
    return report, research_context, research_costs, research_images, research_sources, source_urls

if __name__ == "__main__":
    query = """Brand: Agencytoolkit.ai (AgencyAI)

Please write an audience analysis report for Agencytoolkit.ai (AgencyAI), No more than 300 words.
The report should include:
- What is the inspiration of Agencytoolkit.ai (AgencyAI)?
- What is the background of Agencytoolkit.ai (AgencyAI)?
- Core Demographics: Who they are [Key identifiers including age, gender, income, location in Canada, and life stage that define our target.]
- Lifestyle & Values: How they think [Their beliefs, priorities, and values that shape their worldview and daily choices as they pertain to digital marketing engagement and online purchasing behavior.]
- Digital Behavioral Patterns: How they engage [Their online habits, preferred platforms, search behaviors, social media usage patterns, and typical conversion journey across digital touchpoints.]
"""


    report_type = "audience_report"
    # "brand_report"
    # "audience_report"
    # "market_report"
    # "research_report"


    report_source = "web"
    # "hybrid"
    # "web"
    # "local"
    # "langchain_documents"
    # "langchain_vectorstore"

    report, context, costs, images, sources, source_urls = asyncio.run(get_report(query, report_type, report_source))
    
    # print("Report:")
    # print(report)
    # print("\nResearch Costs:")
    # print(costs)
    # print("\nNumber of Research Images:")
    # print(len(images))
    # print("\nNumber of Research Sources:")
    # print(len(sources))
    # print(sources)

    # End time
    end_time = datetime.now()

    # Calculate running time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")

 
    f = open(f"./task_tests/report.md", "w")
    f.write(report)
    f.close()

    f = open("./task_tests/mata.md", "w")
    meta_data = f"""Research Costs:
{costs}

Execution time:
{execution_time}

Number of Research Images:
{len(images)}

Number of Research Sources:
{len(sources)}
---
### Research URLs:
{source_urls}

----
### Query:
{query}

---
### Research Context:
{context}
"""
    
    f.write(meta_data)
    f.close()