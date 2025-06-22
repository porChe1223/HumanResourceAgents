from langchain_text_splitters import CharacterTextSplitter


def chunk_text(document):
  """
  テキストを分割する

  Args:
    document: 分割するテキスト

  Returns:
    list: 分割されたテキストのリスト
  """
  text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=80000, chunk_overlap=0
  )
  texts = text_splitter.split_text(document)
  return texts

if __name__ == "__main__":
  print(chunk_text("Hello, world!"))
