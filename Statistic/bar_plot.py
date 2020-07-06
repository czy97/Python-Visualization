import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def autolabel(ax):
    """
    Attach a text label above each bar displaying its height
    """
    for patch in ax.patches:
        height = patch.get_height()
        ax.text(patch.get_x() + patch.get_width()/2., 1.0*height,
                '{}'.format(str(height)),
                ha='center', va='bottom')

def side_by_side_bar():
    # side_by_side bar plotting

    df = pd.DataFrame()

    df['percent'] = pd.Series([0.64, 0.36, 0.49, 0.51])
    df['gender'] = pd.Series(['M','F','M','F'])
    df['group'] =pd.Series([1,1,2,2])

    ax = sns.barplot(x='group',y='percent',data=df, hue='gender', palette="deep")

    autolabel(ax)
    plt.show()

if __name__ == "__main__":
    side_by_side_bar()