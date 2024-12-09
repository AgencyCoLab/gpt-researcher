# from gpt_researcher import agent
from gpt_researcher.agent import GPTResearcher
import asyncio
from datetime import datetime

# Start time
start_time = datetime.now()

async def get_report(query: str, report_type: str):
    researcher = GPTResearcher(query, report_type)
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
    query = """Brand: Guinness Zero

EXPECTED OUTPUT: Please structure your response with precision and ensure strict adherence to the word limit for clarity and conciseness. Your response should be well-organized, using headers, subheaders, and lists for easy readability. It is critical that you adhere to the specified word count to ensure the output is focused and relevant.
TITLE: # The Target
BODY: [Write in a clear, professional voice that balances strategic insight with straightforward communication. Use precise language that articulates key points without unnecessary flourish. Focus on facts and meaningful insights, avoiding marketing jargon and coined phrases. The tone should be confident yet grounded, delivering information in a way that resonates with business leaders who value clarity and strategic thinking. Outputs should be through a Canadian lens, however do not over-emphasize the Canadian aspect. Provide in 100 words or less]:
Core Demographics: Who they are [Key identifiers including age, gender, income, location in Canada, and life stage that define our target.]
Lifestyle & Values: How they think [Their beliefs, priorities, and values that shape their worldview and daily choices as they pertain to digital marketing engagement and online purchasing behavior.]
Digital Behavioral Patterns: How they engage [Their online habits, preferred platforms, search behaviors, social media usage patterns, and typical conversion journey across digital touchpoints.]
INSTRUCTIONS:
Review audience research, including demographics, psychographics, and digital behavioral data
Analyze existing customer insights and digital engagement metrics
Define clear audience characteristics and online behavioral patterns
Identify specific digital actions and conversions we want to drive
FINALIZATION: Please structure your response with precision and ensure strict adherence to the word limit for clarity and conciseness. Your response should be well-organized, using headers, subheaders, and lists for easy readability. Confirm that the text adheres to the specified word count. Non-compliance with the word count may result in the need for revision or non-acceptance of the work.
"""


    report_type = "audience_report"
    # "brand_report"
    # "audience_report"
    # "market_report"
    # "research_report"

    report, context, costs, images, sources, source_urls = asyncio.run(get_report(query, report_type))
    
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