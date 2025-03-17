import huffmanCoding as hc
import huffmanDecoding as hd
import tkinter as tk
from tkinter import filedialog
import pprint

def select_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()
    if file_path: 
        #open file
        file = open(file_path, "r")
        global codes, encoded
        codes = {}
        encoded = ""
        codes.clear()
        codes, encoded = hc.huffmanCoding(file.read())

        #files sizes
        original_bytes = len(open(file_path, "rb").read())
        encoded_bytes = len(encoded) // 8 + 1
        byte_label.config(text=f"Original: {original_bytes} bytes | Compressed: {encoded_bytes} bytes | Ratio: {encoded_bytes/original_bytes*100:.2f}%")
        
        #close file and print results
        file.close()
        pp = pprint.PrettyPrinter(indent=0)
        text_widget_1.delete(1.0, tk.END)
        text_widget_1.config(state=tk.NORMAL)
        text_widget_1.insert(tk.END, pp.pformat(codes).replace("{", "").replace("}", ""))
        text_widget_1.config(state=tk.DISABLED)

        
        
def decompress_file():
    global codes, encoded
    #could add catch for empty codes so the text does disappear
    text_widget_2.config(state=tk.NORMAL)
    text_widget_2.delete(1.0, tk.END)
    text_widget_2.insert(tk.END, hd.huffmanDecode(encoded, codes))
    text_widget_2.config(state=tk.DISABLED)
    codes.clear()
    encoded = ""
    
# Create the main window
root = tk.Tk()
root.title("Huffman Coding and Decoding")
root.geometry("500x400")

# Create basic UI elements
input_label = tk.Label(root, text="Huffman Coding and Decoding")
input_label.pack()

# Create a button to open file dialog
file_select_button = tk.Button(root, text="Select File", command=select_file)
file_select_button.pack()

# Create a label to display the selected file path
byte_label = tk.Label(root, text="")
byte_label.pack()

# Create a Text widget to display the content
text_widget_1 = tk.Text(root, width=50, height=10)
text_widget_1.pack()
text_widget_1.config(state=tk.DISABLED)

# Create basic UI elements
input_label = tk.Label(root, text="Output")
input_label.pack()

decompress_button = tk.Button(root, text="Decompress File", command=decompress_file)
decompress_button.pack()

text_widget_2 = tk.Text(root, width=50, height=10)
text_widget_2.pack(pady=10)
text_widget_2.config(state=tk.DISABLED)

# Run the Tkinter event loop
root.mainloop()