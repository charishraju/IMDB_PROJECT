# Define a function to perform random scrolling
def random_scroll():
    # Get the height of the webpage
    total_height = driver.execute_script("return document.body.scrollHeight")
    
    # Perform random scrolling for a specific number of times
    for _ in range(10):  # adjust the number of scrolls as needed
        # Generate a random position to scroll to
        random_position = random.randint(0, total_height)
        # Scroll to the random position
        driver.execute_script(f"window.scrollTo(0, {random_position});")
        # Wait for a short period of time
        time.sleep(random.uniform(5, 20))  
        
def scroll_to_bottom():
    """Scrolls to the bottom of the page."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Allow time for content to load

def scroll_to_element(element):
    """Scrolls smoothly to the given element."""
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(2)  # Small delay for UI adjustment