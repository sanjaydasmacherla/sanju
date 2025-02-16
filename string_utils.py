# string_utils.py
def reverse_string(s):
    return s[::-1]

text = "hello"
reversed_text = reverse_string(text)
print(f"Original: {text}, Reversed: {reversed_text}")
git add string_utils.py  
git commit -m "Added a function to reverse a string in Python"  
git push origin main  
