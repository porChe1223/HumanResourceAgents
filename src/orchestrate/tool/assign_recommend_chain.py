from orchestrate.tool.create_assignee import create_assignee

# 推薦エージェントにタスクを渡す
assign_recommend_chain = create_assignee(
    chain_name="recommend_chain",
    description="Assign task to a recommend agent.",
)
