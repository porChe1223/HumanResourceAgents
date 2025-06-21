"""
テキストファイルを読み込む
"""
def read_txt(file_path):
  with open(file_path, "r", encoding="utf-8") as file:
    return file.read()

if __name__ == "__main__":
  print(read_txt("tests/llm_developer/application_requirements.txt"))
