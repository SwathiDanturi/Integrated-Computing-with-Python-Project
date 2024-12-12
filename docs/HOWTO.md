g## Project: New York City's Crime Data in 2024
### Developers: 
- T1: Olivia LaCroix
- T2: Swathi Danturi

# How to Use This Project

## Prerequisites
- Python 3.x installed
- `pip` (Python package installer)
- `pytest` for running tests
- `rainbow csv` extension in VSCode
- `black formatter` to format files

## Setup
1. **Clone the Repository**
    ```sh
    git clone <remote-repo-url> "folder_name"
    cd "folder_name"
    ```

2. **Install Dependencies**
    ```sh
    pip install -r "requirements.txt"
    ```

## Running the Project
1. **Run the Client**
    ```sh
    python "client.py"
    ```

2. **Run the Core Modules**
    ```sh
    python "analysis_t1.py"
    python "analysis_t2.py"
    ```

## Running Tests
1. **Run All Tests**
    ```sh
    pytest
    ```

2. **Run Specific Test Files**
    ```sh
    pytest "test_most_arrests_day_most_common_race.py"
    pytest "test_highest_felony_offense_in_borough.py"
    pytest "test_crime_most_committed_agegroup.py"
    pytest "test_avg_time_diff_between_arrests.py"
    ```

## Contributing
1. **Create a New Branch**
    ```sh
    git checkout -b "feature-branch-name"
    ```

2. **Make Changes and Commit**
    ```sh
    git add .
    git commit -m "Description of changes"
    ```

3. **Push Changes to Remote**
    ```sh
    git push origin "feature-branch-name"
    ```

4. **Create a Pull Request**
    - Go to the repository on GitHub
    - Click on "New Pull Request"
    - Select your branch and submit the pull request

5. **Merge a Pull Request**
    - Go to the repository on GitHub
    - Click on "Files changed" tab and review the changes
    - Click "review changes" and leave comments then either "approve" or "request changes"
    - Click "Pull merge request" and then click "Confirm merge"
    - Go to Visual Code and ensure you are in the correct directory
    - Open a python terminal
    - `git checkout main`, main branch
    - `git pull origin main`, merge all the changes 

## Additional Information
- For detailed project requirements, refer to [README.md](README.md)
- For design details, refer to [DESIGN.md](DESIGN.md)