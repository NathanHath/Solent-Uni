def search_books(file):
    sections  = ""
    books = "Books:\n"
    with open(file) as f:
        for line in f:
            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done")
    return f"{sections}\n\n{books}"

def save(file2, data):
    print("Saving...")
    with open(file2, "w") as f:
        f.write(data)
    print("Done")

def run_tsak4():
    data = search_books("books")
    save("books_saved", data)
run_tsak4()

