# scoop-search-directory
This Python script performs a search on the Scoop package manager repository and provides information on available applications. It allows users to install applications or add repositories directly from the command line interface (CLI).

### Usage

1. **Clone the repository**: Clone this repository using `git clone`.
2. **Navigate to the directory**: Go to the directory of the cloned repository.
3. **Install dependencies**: Install the required dependencies using `pip`.

```shell
git clone https://github.com/grisha765/scoop-search-directory.git
cd scoop-search-directory
pip install requests beautifulsoup4 prettytable lxml
```

### Run Script

1. Execute the script: Run the script and optionally provide a search query.

```shell
python main.py [search_query]
```

### Features

1. Searches the Scoop package manager repository based on the provided query.
2. Retrieves information about available applications including name, description, repository, version, and more.
3. Displays search results in a tabular format using PrettyTable.
4. Allows users to install applications or add repositories directly from the command line.
5. Supports interactive user input for selecting actions such as installing an application or adding a repository.
