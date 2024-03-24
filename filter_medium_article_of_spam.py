import re

# test data
input_data = {
    # "title": "How to make $1000 in 1 day",
    "title": "Containerd image content, snapshot سلام",
    # "title": "Personal Finance Assistant cusTomer care service Toll free Number)+91)"
    # "title": "Photo by Francesco Ungaro on UnsplashAMP CREDIT LOAN APP CUSTOMER CARE HELPLINE Number"

}
def main():
    # Get the title from the input data
    title = input_data["title"]

    # Check if title is English
    # The unicode range [\u4e00-\u9fff] is for Chinese characters, and [\u0600-\u06FF] is for Arabic characters.
    if not bool(re.search('[\u4e00-\u9fff\u0600-\u06FF]', title)):

        # Define a list of words to filter out
        filter_words = ["finance", "loan", "+", "number", "customer", "credit", "call", "care", "8", "9", "0", "photo", "dit", "dinero", "£", "€", "$", "comparar", "¥"]

        # Initialize a flag to check if the title needs to be filtered
        filter_title = False

        # Loop through each word in the filter_words list
        for word in filter_words:
            # If the word is found in the title, set the filter_title flag to True
            if word.lower() in title.lower():
                filter_title = True
                # Break the loop as we don't need to check for any more words
                break

        # If the filter_title flag is True, print a message indicating that the title needs to be filtered
        if filter_title:
            print("Title needs to be filtered")
        # If the filter_title flag is False, print the title as it is
        else:
            print(title)

        # Store the filter_title flag and the title in a dictionary for output
        output = {"filter_title": filter_title, "title": title}
    else:
        # If the title is not in English, print a message indicating that the title needs to be filtered
        print("Title needs to be filtered")
        # Store the filter_title flag and the title in a dictionary for output
        output = {"filter_title": True, "title": title}

if __name__ == "__main__":
    main()