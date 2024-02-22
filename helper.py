"""
Format a string into a more viewable format by inserting newlines after each sentence. 
Two space characters are also added to help streamlit markdown processor actually create a new line.
"""
def format_transcript(str):
    import re
    x = re.sub(r"([.!?])", r'\1  \n', str)
    return x
