# webscraping1
webscraping : Extract the product details based  on the user input, it will show the top 10 brands of the product based on the user ratings for the product.
The project is an analysis tool for comparing top-rated products on Amazon with popular brands on Myntra, an e-commerce platform for fashion and lifestyle products. Here's a breakdown of the project:

1. **User Interface (UI)**:
   - The UI is built using the Tkinter library, a standard GUI toolkit for Python.
   - It consists of a main window with three sections: Amazon Top Rated Products, Myntra Popular Brands, and Brand Comparison.
   - Each section contains a scrolled text widget to display the relevant information fetched from the web.

2. **Functionality**:
   - Users can enter a product name into an entry field and press the "Search" button or hit Enter to initiate the search.
   - Upon clicking the "Search" button or pressing Enter, the program fetches and displays two sets of information:
     - **Amazon Top Rated Products**: The program opens a Chrome webdriver, navigates to Amazon, searches for the entered product, and extracts the brand names and ratings of the top-rated products related to the search query. This information is displayed in the Amazon Top Rated Products section.
     - **Myntra Popular Brands**: Similarly, the program opens another Chrome webdriver, navigates to Myntra, searches for the entered product, and extracts the brand names and their occurrence counts. The top popular brands are displayed in the Myntra Popular Brands section.
   - After fetching and displaying the information from both platforms, the program performs a comparison of brand popularity between Amazon and Myntra. It identifies common popular brands found on both platforms and displays the results in the Brand Comparison section.

3. **Dependencies**:
   - The project relies on the Tkinter library for the GUI, Selenium for web scraping, and the Chrome webdriver for browser automation.
   - Users need to have the Chromedriver installed and added to the system PATH for Selenium to work properly.

4. **Execution**:
   - Users interact with the UI by entering a product name and clicking the "Search" button.
   - The program then fetches and displays the relevant information in each section of the UI.
   - Users can analyze the displayed data to identify popular brands across both e-commerce platforms.

5. **Error Handling**:
   - The program incorporates error handling to manage potential issues such as timeout exceptions, WebDriver exceptions, and general errors during the web scraping process.
   - Error messages are displayed in the respective sections of the UI to notify users of any encountered issues.

Overall, the project provides a simple yet effective way for users to compare brand popularity between Amazon and Myntra for a given product category. It demonstrates the use of web scraping techniques and GUI development in Python to create a practical analysis tool.
