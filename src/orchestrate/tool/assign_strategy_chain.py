from orchestrate.tool.create_assignee import create_assignee

# 戦略決定エージェントにタスクを渡す
assign_to_strategy_chain = create_assignee(
    chain_name="strategy_chain",
    description="Assign task to a strategy agent.",
)
