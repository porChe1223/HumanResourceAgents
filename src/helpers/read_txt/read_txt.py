def read_txt(file_path):
  """
  テキストファイルを読み込む

  Args:
    file_path: テキストファイルのパス

  Returns:
    str: テキストファイルの内容
  """
  with open(file_path, "r", encoding="utf-8") as file:
    return file.read()

if __name__ == "__main__":
  print(read_txt("tests/llm_developer/application_requirements.txt"))
