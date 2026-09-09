# A01 — California Housing Boxplot

## Project Overview

This project demonstrates a basic GitHub and Python data analysis workflow. It loads the California Housing dataset from `scikit-learn`, analyzes key features, generates a boxplot of median house values, and saves the resulting figure to a local directory.

## Data Overview

This project uses the **California Housing dataset**, which is loaded using:

`sklearn.datasets.fetch_california_housing(as_frame=True)`

The dataset contains aggregate statistics for California census tracts.

### Features

* **MedInc**: Median income in block group
* **HouseAge**: Median house age in block group
* **AveRooms**: Average number of rooms per household
* **AveBedrms**: Average number of bedrooms per household
* **Population**: Block group population
* **AveOccup**: Average number of household members
* **Latitude**: Block group latitude
* **Longitude**: Block group longitude
* **MedHouseVal**: Median house value for California districts, expressed in $100,000s

## Repository Structure

```text
A01/
├── figs/
│   └── boxplot.png
├── src/
│   └── boxplot.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements

This project requires **Python 3** and the following dependencies:

* pandas
* matplotlib
* scikit-learn

All required libraries are listed in `requirements.txt`.

## How to Run

### 1. Clone the Repository

Clone this repository to your local machine using GitHub Desktop or the command line:

```bash
git clone https://github.com/iym24004/A01.git
```

### 2. Navigate to the Project Directory

Open a terminal or command prompt and navigate to the project root directory:

```bash
cd A01
```

### 3. Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### 4. Execute the Script

Run the Python script:

```bash
python src/boxplot.py
```

## Expected Output

When the script executes successfully:

* Summary information from the dataset is printed to the terminal.
* The dataset's `head()` and `shape` information are displayed.
* A boxplot of median house values is generated.
* The resulting image is saved in the `figs/` directory.

The generated figure can be found at:

```text
figs/boxplot.png
```

## Git Workflow

This project follows a standard feature-branch Git workflow:

1. Development work is completed on the dedicated `dev` branch.
2. Code updates and generated output files are committed and pushed to `dev`.
3. A Pull Request is opened to review and merge changes from `dev` into `main`.
4. The `dev` branch is deleted after the merge to maintain repository hygiene.

## Author

**Parvathi Meghanath**

University of Connecticut

MS in Business Analytics & Project Management

OPIM 5512
