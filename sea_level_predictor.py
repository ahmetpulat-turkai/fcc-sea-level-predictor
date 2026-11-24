import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    r = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xs = np.arange(df['Year'].min(), 2051)
    ax.plot(xs, r.intercept + r.slope * xs, 'r')

    d2 = df[df['Year'] >= 2000]
    r2 = linregress(d2['Year'], d2['CSIRO Adjusted Sea Level'])
    xs2 = np.arange(2000, 2051)
    ax.plot(xs2, r2.intercept + r2.slope * xs2, 'g')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
