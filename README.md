# A01 — California Housing Boxplot

This project demonstrates a basic GitHub and Python workflow by loading the California Housing dataset, creating a boxplot, and saving the resulting figure as an image.

## Data

This project uses the **California Housing dataset**, which is provided through `scikit-learn`.

The dataset is loaded using `fetch_california_housing(as_frame=True)` and contains information about California housing districts, including features such as:

* Median income
* House age
* Average number of rooms
* Average number of bedrooms
* Population
* Average occupancy
* Latitude and longitude
* Median house value

The dataset is loaded directly from `scikit-learn` when the Python script is executed.

## Repository Structure

```text
A01/
├── README.md
├── requirements.txt
├── src/
│   └── boxplot.py
└── figs/
    └── boxplot.png
```

## Requirements

The project uses Python and the following packages:

```text
pandas==2.1.4
matplotlib>=3.8
scikit-learn>=1.4
```

These dependencies are listed in `requirements.txt`.

## How to Run

### 1. Clone the Repository

Clone the `A01` repository to your computer using GitHub Desktop or Git:

```bash
git clone <your-repository-url>
```

### 2. Open the A01 Folder

Change your working directory to the A01 repository:

```bash
cd path/to/A01
```

### 3. Install the Required Packages

Run:

```bash
pip install -r requirements.txt
```

### 4. Run the Python Script

Run the boxplot script using:

```bash
python src/boxplot.py
```

The script will download/load the California Housing dataset, create a boxplot, and save the resulting figure in the `figs` folder.

## Expected Output

After successfully running the script, the following image file should be created:

```text
figs/boxplot.png
```

The image contains a boxplot based on a variable from the California Housing dataset.

## Git Workflow

This assignment uses a simple Git branching workflow.

* `main` — final version of the project
* `dev` — working branch used to make changes
* Changes are committed to `dev`
* A Pull Request is created from `dev` to `main`
* After the Pull Request is merged, the `dev` branch is deleted

## Author

**Parvathi Meghanath**

University of Connecticut
MS in Business Analytics & Project Management
OPIM 5512
