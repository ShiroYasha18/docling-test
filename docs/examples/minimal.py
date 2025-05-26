from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
<<<<<<< HEAD
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())
=======

converter = DocumentConverter()
doc = converter.convert(source).document

print(doc.export_to_markdown())
>>>>>>> origin/main
# output: ## Docling Technical Report [...]"
