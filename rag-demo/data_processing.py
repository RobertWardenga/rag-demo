import os
from typing import List

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain_core.documents.base import Document

def load_split_pdf(files_dir: Optional[str], display_stats: bool = True) -> List[Document]:
	loader = DirectoryLoader(files_dir, glob="*.pdf", show_progress=True, loader_cls=PyMuPDFLoader)
	pages = loader.load_and_split()
	if display_stats:
		max_seq_len = max([len(page.page_content) for page in pages])
		print(f'Max Sequence in one page: {max_seq_len}')
	return pages
