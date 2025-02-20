import speech_to_text as Stt

def fin_list():
    from speech_to_text import stt
    text = stt().upper()
    valid_labels = {chr(i) for i in range(65, 91)}  # Set of 'A' to 'Z'
    alphabet_list = [f"{char}.jpg" if char in valid_labels else "space.jpg" for char in text if char in valid_labels or char == " "]
    return alphabet_list



