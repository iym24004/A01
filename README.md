# A01
A01 - doing my first assignment
# A01 — California Housing Boxplot

This project loads the California Housing dataset, creates a boxplot to visualize the distribution of a selected variable, and saves the resulting figure as an image.

## Data

The project uses the **California Housing dataset** provided through `scikit-learn`.

The dataset contains information about California districts, including features such as median income, house age, average rooms, population, and median house value.

## Project Structure

```text
A01/
├── README.md
├── requirements.txt
├── src/
│   └── boxplot.py
└── figs/
    └── boxplot.png
```

## How to Run

1. Clone the repository to your computer.
2. Create and activate a Python environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the plotting script:

```bash
python src/boxplot.py
```

More detailed instructions will be added later.

## Expected Output

Running the script will create a boxplot and save it as:

```text
figs/boxplot.png
```

The saved image will show the distribution of the selected California Housing dataset variable(s).

## Requirements

The project requires:

* Python
* pandas
* matplotlib
* scikit-learn
