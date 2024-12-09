from multi_agents.agents import ChiefEditorAgent

chief_editor = ChiefEditorAgent({
  "query": """Brand: Guinness Zero

EXPECTED OUTPUT: Please structure your response with precision and ensure strict adherence to the word limit for clarity and conciseness. Your response should be well-organized, using headers, subheaders, and lists for easy readability. It is critical that you adhere to the specified word count to ensure the output is focused and relevant.

**TITLE:** # Voice & Visuals

**BODY:** 

[Write in a clear, professional voice that balances strategic insight with straightforward communication. Use precise language that articulates key points without unnecessary flourish. Focus on facts and meaningful insights, avoiding marketing jargon and coined phrases. The tone should be confident yet grounded, delivering information in a way that resonates with business leaders who value clarity and strategic thinking. Outputs should be through a Canadian lens, however do not over-emphasize the Canadian aspect. Provide In 150 words or less]:

## **Voice & Visual Characteristics**

**Voice:** How the Brand Speaks [List five adjectives that define the brand's voice. Follow with a brief, unified description of how these qualities work together to create its distinctive tone]

**Visual:** How the Brand Appears [Describe the key principles and characteristics that guide the brand's visual expression]

INSTRUCTIONS:
1. Review brand personality and values
2. Define clear voice characteristics
3. Establish visual principles
4. Set clear behavioral boundaries

**FINALIZATION:** Please structure your response with precision and ensure strict adherence to the word limit for clarity and conciseness. Your response should be well-organized, using headers, subheaders, and lists for easy readability. Confirm that the text adheres to the specified word count. Non-compliance with the word count may result in the need for revision or non-acceptance of the work.
""",
  "max_sections": 3,
  "follow_guidelines": True,
  "model": "gpt-4o",
  "guidelines": [
    "The report MUST be structured with precision and ensure strict adherence to the word limit for clarity and conciseness. Your response should be well-organized, using headers, subheaders, and lists for easy readability.",
    "It is critical that you adhere to the specified word count to ensure the output is focused and relevant.",
    "The body should be a clear, professional voice that balances strategic insight with straightforward communication. Follow with a brief, unified description of how these qualities work together to create its distinctive tone.",
    "The body should be 150 words or less."
  ],
  "verbose": False
}, websocket=None, stream_output=None)
graph = chief_editor.init_research_team()
graph = graph.compile()