from orchestrate.tool.create_assignee import create_assignee

# 調査エージェントにタスクを渡す
assign_research_chain = create_assignee(
    chain_name="research_chain",
    description="Assign task to a research agent.",
)
