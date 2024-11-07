---
title: 通过整合视觉模型变革RAG，提升文档处理能力
description: 传统的检索增强生成（RAG）方法已经彻底改变了我们与文档的交互方式，但仍存在一些不足。本文探讨通过整合视觉模型如何提升文档处理的效率与准确性，提升信息检索和生成的能力，进而改善用户体验。
pubDatetime: 2024-11-04T16:29:02+08:00
ogImage: https://miro.medium.com/v2/resize:fit:1200/1*5NhR7e1E9EEXMYYAg82YiA.png
tags: 
  - raw
---

[原文链接](https://medium.com/@manthapavankumar11/revolutionizing-rag-by-integrating-vision-models-for-enhanced-document-processing-b3aaa7ab386a) | [原文内容](../raw/revolutionizing-rag-vision-models-document-processing) | [AI 总结](../summary/revolutionizing-rag-vision-models-document-processing)

---

[![Image 1: M K Pavan Kumar](https://miro.medium.com/v2/resize:fill:88:88/1*hm4EMU6eAUOoFTldl_OzNg.jpeg)](https://medium.com/@manthapavankumar11?source=post_page---byline--b3aaa7ab386a--------------------------------)

The traditional Retrieval-Augmented Generation (RAG) approach has revolutionized how we interact with documents, but it still misses crucial visual context. What if RAG could not just read, but also see? By integrating Vision-Language Models (VLMs) alongside conventional text processing, we’ve developed a dual-stream RAG architecture that processes both textual and visual content from PDF documents. Our approach leverages `Qdrant’s` multi-vector capabilities to store both text and image embeddings, enabling richer context retrieval. When queried, the system doesn’t just match text — it actually “sees” the document pages, leading to more accurate and contextually aware responses. In this article, we’ll explore how this vision-enhanced RAG system opens new possibilities for document understanding and retrieval.

created by author M K Pavan Kumar

The Architecture:
-----------------

Let me explain the architecture of this innovative vision-enhanced RAG system based on the diagram.

The system begins with PDF documents as the primary input, which undergo dual processing streams to maximize information extraction. In the first stream, each page is converted into an image, while in the parallel stream, text is extracted from each page. This dual approach ensures no information is lost during the processing phase. The extracted content is then vectorized and stored in Qdrant, a vector database that efficiently handles multiple vector types per document. Each entry in Qdrant contains both the image and text vectors, along with essential metadata including page numbers, the base64-encoded page images, and the extracted text.

When a user submits a query, Qdrant’s prefetch capability comes into play, retrieving the top three most relevant results (as configured in this implementation) based on vector similarity. This is where the architecture becomes particularly interesting — the system doesn’t stop at traditional text-based retrieval. The same user query, along with the retrieved base64-encoded images, is passed to a Vision Language Model (VLM), specifically OpenAI’s vision model in this case. This allows the system to perform visual analysis of the actual document layout and content, providing an additional layer of understanding.

The final piece of the architecture involves an aggregating Language Learning Model (LLM) that combines the results from both the text-based retrieval and the vision model’s analysis. This aggregator synthesizes the information from both streams, producing a comprehensive response that leverages both textual and visual understanding of the documents. The result is a more robust and context-aware system that can provide answers with strong supporting evidence from both textual and visual perspectives.

The brilliance of this architecture lies in its ability to understand documents not just as text, but as they were meant to be seen — complete with layout, formatting, and visual elements that often carry crucial contextual information. This dual-stream approach, combined with modern vector search capabilities and vision models, represents a significant advancement in RAG systems.

> Sometimes the Text might not be sufficient to answer your query and hence is the vision.

The Implementation:
-------------------

Let us look at the Ingestion part of the architecture as below.

Data ingestion to vec-store

Let us design a class called `pdf_processor.py` with the shown methods in place.

The outline of the pdf processor class.

from pdf2image import convert\_from\_path  
from pypdf import PdfReader  
import osclass PDFProcessor:  
    """  
    A class to handle PDF processing operations including text extraction and image conversion.  
    """

def \_\_init\_\_(self, pdf\_path, output\_dir):  
        """  
        Initialize the PDF processor.

Parameters:  
        - pdf\_path: str, path to the PDF file  
        - output\_dir: str, directory to save the outputs  
        """  
        self.pdf\_path = pdf\_path  
        self.output\_dir = output\_dir  
        self.saved\_images = \[\]  
        self.page\_texts = \[\]  
        self.page\_dicts = \[\]

# Create output directory if it doesn't exist  
        os.makedirs(self.output\_dir, exist\_ok=True)

def extract\_text(self):  
        """  
        Extract text from each page of the PDF.  
        """  
        print("Extracting text from PDF...")  
        reader = PdfReader(self.pdf\_path)

# Extract text from each page  
        for i, page in enumerate(reader.pages):  
            text = page.extract\_text()  
            self.page\_texts.append(text)

# Save text to file  
            text\_file\_path = os.path.join(self.output\_dir, f'page\_{i + 1}.txt')  
            with open(text\_file\_path, 'w', encoding='utf-8') as f:  
                f.write(text)  
            print(f"Saved text from page {i + 1} to {text\_file\_path}")

def convert\_to\_images(self, dpi=200, fmt='png'):  
        """  
        Convert each page of the PDF to images.

Parameters:  
        - dpi: int, resolution of output images  
        - fmt: str, output image format  
        """  
        print("Converting PDF pages to images...")  
        pages = convert\_from\_path(self.pdf\_path, dpi=dpi)

# Save each page as an image  
        for i, page in enumerate(pages):  
            image\_path = os.path.join(self.output\_dir, f'page\_{i + 1}.{fmt}')  
            page.save(image\_path, fmt)  
            self.saved\_images.append(image\_path)  
            print(f"Saved image from page {i + 1} to {image\_path}")

def create\_page\_dicts(self, fmt='png'):  
        """  
        Create a list of dictionaries containing page information.

Parameters:  
        - fmt: str, image format used (needed for filenames)

Returns:  
        - list of dictionaries with page information  
        """  
        num\_pages = max(len(self.saved\_images) if self.saved\_images else 0,  
                        len(self.page\_texts) if self.page\_texts else 0)

self.page\_dicts = \[\]  
        for i in range(num\_pages):  
            page\_dict = {  
                "image": f"page\_{i + 1}.{fmt}" if self.saved\_images else None,  
                "text": f"page\_{i + 1}.txt" if self.page\_texts else None  
            }  
            self.page\_dicts.append(page\_dict)

return self.page\_dicts

def process(self, extract\_images=True, extract\_text=True, dpi=200, fmt='png'):  
        """  
        Process the PDF file with specified operations.

Parameters:  
        - extract\_images: bool, whether to convert pages to images  
        - extract\_text: bool, whether to extract text  
        - dpi: int, resolution of output images  
        - fmt: str, output image format

Returns:  
        - tuple: (list of image paths, list of text content, list of page dictionaries)  
        """  
        try:  
            if extract\_text:  
                self.extract\_text()

if extract\_images:  
                self.convert\_to\_images(dpi=dpi, fmt=fmt)

self.create\_page\_dicts(fmt=fmt)

return self.saved\_images, self.page\_texts, self.page\_dicts

except Exception as e:  
            print(f"Error processing PDF: {str(e)}")  
            return \[\], \[\], \[\]

def print\_extracted\_text(self):  
        """  
        Print the extracted text from each page with clear separation.  
        """  
        for i, text in enumerate(self.page\_texts, 1):  
            print(f"\\n{'=' \* 40}")  
            print(f"Page {i}")  
            print(f"{'=' \* 40}")  
            print(text.strip())

\# Example driver usage  
\# if \_\_name\_\_ == "\_\_main\_\_":  
\#     # Example parameters  
\#     pdf\_file = "data/rag.pdf"  # infact any pdf as input here.  
\#     output\_folder = "pdf\_output"  
#  
\#     # Create processor instance  
\#     processor = PDFProcessor(pdf\_file, output\_folder)  
#  
\#     # Process PDF - extract both images and text  
\#     image\_paths, texts, page\_dicts = processor.process(  
\#         extract\_images=True,  
\#         extract\_text=True,  
\#         dpi=200,  
\#         fmt='png'  
\#     )  
#  
\#     print("\\nProcessing complete.")  
\#     print("\\nPage information:")  
\#     for i, page\_info in enumerate(page\_dicts, 1):  
\#         print(f"Page {i}:", page\_info)

The `pdf_output` collects the images and full\_text for further processing. Now let us create another class `DataIndexerAndRetriever.py` as shown below.

The outline of the pdf processor class.

from dotenv import load\_dotenv, find\_dotenv  
from qdrant\_client import QdrantClient, models  
from fastembed import TextEmbedding  
from sentence\_transformers import SentenceTransformer  
from PIL import Image  
import openai  
import base64  
import io  
import osfrom pdf\_processor import PDFProcessor

class DataIndexerAndRetriever:  
    def \_\_init\_\_(self, data\_dir='./pdf\_output', qdrant\_url="http://localhost:6333", qdrant\_api\_key='th3s3cr3tk3y'):  
        """  
        Initialize the Research Paper Processor.

Parameters:  
        - data\_dir: str, directory containing PDF output files  
        - qdrant\_url: str, Qdrant server URL  
        - qdrant\_api\_key: str, Qdrant API key  
        """  
        # Load environment variables  
        \_ = load\_dotenv(find\_dotenv())

self.data\_dir = data\_dir  
        self.collection\_name = 'research\_papers'

# Initialize models  
        self.client = QdrantClient(url=qdrant\_url, api\_key=qdrant\_api\_key)  
        self.image\_embedding\_model = SentenceTransformer("clip-ViT-B-32")  
        self.text\_embedding\_model = TextEmbedding(  
            model\_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'  
        )  
        # Initialize OpenAI API  
        api\_key = 'sk-proj-api-key'  
        self.openai\_client = openai.OpenAI(api\_key=api\_key)

# Initialize collection if it doesn't exist  
        self.\_initialize\_collection()

def \_initialize\_collection(self):  
        """Initialize Qdrant collection if it doesn't exist."""  
        if not self.client.collection\_exists(collection\_name=self.collection\_name):  
            self.client.create\_collection(  
                collection\_name=self.collection\_name,  
                vectors\_config={  
                    "clip-ViT-B-32": models.VectorParams(  
                        size=512,  
                        distance=models.Distance.COSINE  
                    ),  
                    "paraphrase-multilingual-MiniLM-L12-v2": models.VectorParams(  
                        size=384,  
                        distance=models.Distance.COSINE  
                    ),  
                }  
            )

def get\_text\_embeddings(self, text\_file\_path):  
        """  
        Get embeddings for text file content.

Parameters:  
        - text\_file\_path: str, path to text file

Returns:  
        - tuple: (text embeddings, full text content)  
        """  
        with open(file=text\_file\_path, mode='r') as data:  
            full\_text = data.read()  
        return next(self.text\_embedding\_model.passage\_embed(full\_text)), full\_text

def image\_to\_base64(self, image\_path):  
        """  
        Convert image to base64 and get embeddings.

Parameters:  
        - image\_path: str, path to image file

Returns:  
        - tuple: (image embeddings, base64 encoded string)  
        """  
        try:  
            with open(image\_path, "rb") as image\_file:  
                encoded\_string = base64.b64encode(image\_file.read()).decode('utf-8')  
            with Image.open(image\_path) as img:  
                image\_embedding = self.image\_embedding\_model.encode(img).tolist()  
            return image\_embedding, encoded\_string  
        except Exception as e:  
            print(f"Error converting image to base64: {str(e)}")  
            return None

def base64\_to\_image(self, base64\_string, output\_path=None, fmt='png'):  
        """  
        Convert base64 string back to image.

Parameters:  
        - base64\_string: str, base64 encoded image string  
        - output\_path: str, path to save decoded image (optional)  
        - fmt: str, image format (default: 'png')

Returns:  
        - PIL.Image or str: Image object or path to saved image  
        """  
        try:  
            image\_data = base64.b64decode(base64\_string)  
            image = Image.open(io.BytesIO(image\_data))

if output\_path:  
                image.save(output\_path, fmt)  
                return output\_path

return image  
        except Exception as e:  
            print(f"Error converting base64 to image: {str(e)}")  
            return None

def index\_pages(self, pages\_data):  
        """  
        Process and index pages data.

Parameters:  
        - pages\_data: list of dict, containing image and text file information  
        """  
        for index, obj in enumerate(pages\_data):  
            image\_path = os.path.join(self.data\_dir, obj\["image"\])  
            text\_file\_path = os.path.join(self.data\_dir, obj\["text"\])

image\_embedding, base64str = self.image\_to\_base64(image\_path)  
            text\_embedding, full\_text = self.get\_text\_embeddings(text\_file\_path=text\_file\_path)

points = \[  
                models.PointStruct(  
                    id=index + 1,  
                    vector={  
                        "clip-ViT-B-32": image\_embedding,  
                        "paraphrase-multilingual-MiniLM-L12-v2": text\_embedding  
                    },  
                    payload={  
                        "\_id": index + 1,  
                        "base64str": base64str,  
                        "full\_text": full\_text,  
                        "page": index + 1  
                    }  
                )  
            \]

self.client.upsert(  
                collection\_name=self.collection\_name,  
                points=points  
            )

def query\_with\_rrf(self, query\_text: str = '', query\_image\_path: str = ''):  
        """  
        Query the collection using Reciprocal Rank Fusion.

Parameters:  
        - query\_text: str, text query  
        - query\_image\_path: str, path to query image

Returns:  
        - list: search results  
        """  
        text\_embedding = None  
        if query\_text != '':  
            text\_embedding = next(self.text\_embedding\_model.embed(query\_text)).tolist()

image\_embedding = None  
        if query\_image\_path != '':  
            with Image.open(query\_image\_path) as img:  
                image\_embedding = self.image\_embedding\_model.encode(img).tolist()

prefetch = None  
        if text\_embedding and len(text\_embedding) \> 0:  
            prefetch = \[  
                models.Prefetch(  
                    query=text\_embedding,  
                    using="paraphrase-multilingual-MiniLM-L12-v2",  
                    limit=3,  
                )  
            \]  
        if image\_embedding and len(image\_embedding) \> 0:  
            prefetch = \[  
                models.Prefetch(  
                    query=image\_embedding,  
                    using="clip-ViT-B-32",  
                    limit=3,  
                )  
            \]

results = self.client.query\_points(  
            collection\_name=self.collection\_name,  
            prefetch=prefetch,  
            query=models.FusionQuery(  
                fusion=models.Fusion.RRF  
            ),  
            with\_payload=True,  
            limit=3,  
        )  
        return results

# Function to ask a question about the image using OpenAI API  
    def ask\_image\_question(self, base64\_image, question):  
        try:  
            # Send the image and question to the OpenAI API  
            response = self.openai\_client.chat.completions.create(  
                model="gpt-4o-mini",  
                messages=\[  
                    {  
                        "role": "user",  
                        "content": \[  
                            {  
                                "type": "text",  
                                "text": question + ". Support your answer with evidence from given context. example: page number, section heading etc",  
                            },  
                            {  
                                "type": "image\_url",  
                                "image\_url": {  
                                    "url": f"data:image/jpeg;base64,{base64\_image}"  
                                },  
                            },  
                        \],  
                    }  
                \],  
            )

# Extract and return the response  
            answer = response.choices\[0\].message.content  
            return answer

except Exception as e:  
            print(f"Error during API call: {e}")  
            return None

\# Example usage  
if \_\_name\_\_ == "\_\_main\_\_":  
    # Sample pages data  
    # Example parameters  
    pdf\_file = "data/rag.pdf"  
    output\_folder = "pdf\_output"

# Create processor instance (open the below comments for the first time   
    # when you want to process the pdf file)  
    # processor = PDFProcessor(pdf\_file, output\_folder)

# Process PDF - extract both images and text  
    # image\_paths, texts, page\_dicts = processor.process(  
    #     extract\_images=True,  
    #     extract\_text=True,  
    #     dpi=200,  
    #     fmt='png'  
    # )

# Initialize processor  
    processor = DataIndexerAndRetriever()

# Process pages (uncomment to run indexing into qdrant)  
    # processor.index\_pages(page\_dicts)

# Query example  
    question = 'What is the OpenAI assistants workflow?'  
    result = processor.query\_with\_rrf(query\_text=question)  
    for point in result.points:  
        response = processor.ask\_image\_question(base64\_image=point.payload\['base64str'\],  
                                                question=question)  
        print("-" \* 50)  
        print(response)

Here’s a brief summary of the code’s key functionalities:

1\. The `DataIndexerAndRetriever` class handles dual-stream document processing with text and image capabilities:

\- Initializes connections to `Qdrant` vector database and loads required embedding models (CLIP for images, MiniLM for text)  
\- Sets up OpenAI client for vision model integration

2\. Core Processing Functions:  
\- Converts PDF pages to both images and text  
\- Generates embeddings for both image and text content  
\- Stores data in Qdrant with dual vectors per document page

3\. Retrieval System:  
\- Uses `Reciprocal Rank Fusion (RRF)` to search across both text and image vectors  
\- Returns top 3 most relevant results by default  
\- Includes original base64 images and full text in results

4\. Vision Integration:  
\- Processes queries using `OpenAI’s GPT-4o` Vision model  
\- Takes user questions and relevant page images  
\- Returns answers with evidence from the document context

5\. Main Workflow:  
\- Processes PDF documents  
\- Indexes content in Qdrant  
\- Accepts user queries  
\- Returns contextual answers using both text and vision capabilities

The Result:
-----------

Observe the question that we have asked and see how OpenAi evidently responded saying its clearly mention in “Figure 2" as attached below.

The Conclusion:
---------------

In conclusion, integrating vision models into Retrieval-Augmented Generation (RAG) systems represents a significant advancement in document processing. By leveraging both image and text data, we enhance the indexing and retrieval capabilities, allowing for richer and more contextually relevant responses. This innovative approach not only improves the accuracy of information retrieval but also provides compelling evidence that strengthens the insights derived from documents. As we continue to explore the synergy between vision and language models, the potential for more effective and nuanced document understanding becomes increasingly attainable.
