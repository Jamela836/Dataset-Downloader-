import requests

file_url="https://example.com/dataset.csv"  # Replace with your dataset URL
file_name='file_name.csv'

def download (url,file):
    response=requests.get(url)
    if response.status_code==200:
        with open (file,'wb') as f:
            f.write(response.content)
        print(f'File Downloaded Successfully as {file}')
    else:
        print(f'Failed to Download File. Status code = {response.status_code}')
        
download(file_url, file_name)

"""

When you use requests.get(url) in Python:
    It does send the request URL to the server.
    "Hey server, I want this thing located at url. Please send it to me."
    1.requests.get() sends an HTTP GET request to the server at the given URL.
    2.The server receives this request and processes it.
    3.If everything is okay, the server responds with a status code (like 200) and the requested data (like a file or web content).
    4.That response is stored in the response object.
    
When you're downloading a file from the internet — especially non-text files (like PDFs, images, videos, etc.) —
    the data you get from requests.get() is in binary format (response.content gives you raw bytes).
    Using 'wb' ensures Python writes the raw bytes exactly as they are, 
    without trying to interpret them as text (which could corrupt the file).
    
What happens when you download the file:
    When you download a .csv file, the data is still just raw bytes (like b'Name,Age\nAlice,30\nBob,25').
    The server sends this binary data with the .csv extension, and you save it to your system (using wb mode).
    Why it looks like rows and columns when opened:
        When you open this file in a program like VS Code or Excel, the program recognizes it as CSV 
        because the data is structured in a way that separates values with commas, 
        and each row is separated by newlines (\n).
        VS Code or Excel reads this binary content (the bytes) and formats it for you as readable rows and columns.
        How the file is saved on the server determines how it's transmitted and how it will be interpreted when you download it
"""



