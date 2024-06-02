import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def fetch_amazon_top_rated_products(product_name, text_widget):
    driver = None
    try:
        # Start a Chrome webdriver (make sure chromedriver is installed and in PATH)
        driver = webdriver.Chrome()

        # Open Amazon website
        driver.get("https://www.amazon.com/")

        # Wait for the search input field to be visible
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox'))
        )

        # Clear any existing text in the search input field
        search_input.clear()

        # Enter the product name in the search input field
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]'))
        )

        # Find all products on the page
        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        # Initialize a list to store product details
        product_details = []

        # Iterate over each product to extract product information
        for product in products:
            # Find the product brand
            product_brand = product.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]')
            brand_name = product_brand.text.strip()

            # Find the product rating
            try:
                product_rating = float(product.find_element(By.XPATH, './/span[@class="a-icon-alt"]').get_attribute('innerHTML').split(' ')[0])
            except:
                product_rating = 0.0

            # Add product details to the list
            product_details.append((brand_name, product_rating))

        # Sort products by their ratings in descending order
        top_rated_products = sorted(product_details, key=lambda x: x[1], reverse=True)[:10]

        # Display the results in the text widget
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Amazon Top Rated Products:\n")
        for idx, (brand, rating) in enumerate(top_rated_products, 1):
            text_widget.insert(tk.END, f"{idx}. Brand: {brand}\n   Rating: {rating}\n\n")

        return [brand for brand, _ in top_rated_products]  # Return list of brands
    except TimeoutException:
        text_widget.insert(tk.END, "Timed out waiting for page to load\n")
        return []
    except WebDriverException as wde:
        text_widget.insert(tk.END, f"A WebDriverException occurred: {str(wde)}\n")
        return []
    except Exception as e:
        text_widget.insert(tk.END, f"An error occurred: {str(e)}\n")
        return []
    finally:
        if driver:
            driver.quit()

def fetch_myntra_popular_brands(product_name, text_widget):
    driver = None
    try:
        # Start a Chrome webdriver (make sure chromedriver is installed and in PATH)
        driver = webdriver.Chrome()

        # Open Myntra website
        driver.get("https://www.myntra.com/")

        # Wait for the search input field to be visible
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'desktop-searchBar'))
        )

        # Clear any existing text in the search input field
        search_input.clear()

        # Enter the product name in the search input field
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-brand'))
        )

        # Find all products on the page
        products = driver.find_elements(By.CLASS_NAME, 'product-brand')

        # Initialize a dictionary to store brand counts
        brand_counts = {}

        # Iterate over each product to extract brand names and count occurrences
        for product in products:
            brand_name = product.text.strip()
            brand_counts[brand_name] = brand_counts.get(brand_name, 0) + 1

        # Sort brands by their occurrence count in descending order
        popular_brands = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Display the results in the text widget
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Myntra Popular Brands:\n")
        for idx, (brand, count) in enumerate(popular_brands, 1):
            text_widget.insert(tk.END, f"{idx}. Brand: {brand}\n   Count: {count}\n\n")

        return [brand for brand, _ in popular_brands]  # Return list of brands
    except TimeoutException:
        text_widget.insert(tk.END, "Timed out waiting for page to load\n")
        return []
    except WebDriverException as wde:
        text_widget.insert(tk.END, f"A WebDriverException occurred: {str(wde)}\n")
        return []
    except Exception as e:
        text_widget.insert(tk.END, f"An error occurred: {str(e)}\n")
        return []
    finally:
        if driver:
            driver.quit()

def compare_brand_popularity(amazon_brands, myntra_brands, text_widget):
    # Compare brand popularity between Amazon and Myntra
    amazon_set = set(amazon_brands)
    myntra_set = set(myntra_brands)
    common_brands = amazon_set.intersection(myntra_set)
    if common_brands:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Brand Comparison:\n")
        text_widget.insert(tk.END, f"Common popular brands found in both Amazon and Myntra: {', '.join(common_brands)}\n")
    else:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "Brand Comparison:\n")
        text_widget.insert(tk.END, "No common popular brands found in both Amazon and Myntra\n")

def fetch_and_display(event=None):
    # Fetch top rated products from Amazon and display them
    amazon_brands = fetch_amazon_top_rated_products(entry.get(), text_widget_amazon)

    # Fetch popular brands from Myntra and display them
    myntra_brands = fetch_myntra_popular_brands(entry.get(), text_widget_myntra)

    # Compare brand popularity between Amazon and Myntra
    compare_brand_popularity(amazon_brands, myntra_brands, text_widget_comparison)

# Create a tkinter window
root = tk.Tk()
root.title("Amazon and Myntra Product Analysis")

# Create a frame for the search box
frame_search = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_search.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

label_search = tk.Label(frame_search, text="Enter Product Name:")
label_search.pack(side=tk.LEFT)

entry = tk.Entry(frame_search, width=50)
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", fetch_and_display)

button_search = tk.Button(frame_search, text="Search", command=fetch_and_display)
button_search.pack(side=tk.LEFT)

# Create a frame for Amazon
frame_amazon = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_amazon.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

label_amazon = tk.Label(frame_amazon, text="Amazon Top Rated Products")
label_amazon.pack(pady=5)

text_widget_amazon = scrolledtext.ScrolledText(frame_amazon, width=60, height=15)
text_widget_amazon.pack(pady=5)

# Create a frame for Myntra
frame_myntra = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_myntra.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

label_myntra = tk.Label(frame_myntra, text="Myntra Popular Brands")
label_myntra.pack(pady=5)

text_widget_myntra = scrolledtext.ScrolledText(frame_myntra, width=60, height=15)
text_widget_myntra.pack(pady=5)

# Create a frame for brand comparison
frame_comparison = tk.Frame(root, bd=2, relief=tk.GROOVE)
frame_comparison.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X)

label_comparison = tk.Label(frame_comparison, text="Brand Comparison")
label_comparison.pack(pady=5)

text_widget_comparison = scrolledtext.ScrolledText(frame_comparison, width=80, height=5)
text_widget_comparison.pack(pady=5)

# Run the tkinter event loop
root.mainloop()
