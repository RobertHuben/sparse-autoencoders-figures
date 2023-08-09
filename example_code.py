import pandas as pd
import matplotlib.pyplot as plt

def create_example_figure():
    in_file_name="data/example_data.csv"
    out_file_name="figures/example_figure.png"
    df=pd.read_csv(in_file_name)
    plt.plot(df['x'], df['y'], marker='o')
    plt.title("Perfectly Correlated Data")
    plt.xticks(df['x'])
    plt.yticks(df['y'])
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.savefig(out_file_name)

create_example_figure()