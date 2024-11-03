# Domain Discovery Tool

This is a simple Python-based tool for discovering domains using an API. It allows users to grab either all available domains or filter by specific extensions, counting the number of new domains found and saving them to a file.

## Features

- **Grab all domains**: Retrieves all available domains from the API.
- **Grab by extension**: Allows users to specify a domain extension (e.g., `.id`) and grab only domains with that extension.
- **Multiple Attempts**: Specify how many times to scrape and the delay between each request.
- **Error Handling**: Automatically retries on 502 errors until successful.
- **Output Formatting**: Displays only the count of new domains found, and saves results to `result_discover.txt`.
