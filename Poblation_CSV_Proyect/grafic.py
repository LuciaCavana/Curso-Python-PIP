import matplotlib.pyplot as plt
def generate_bar_chart(labels,values,name):
    fig,ax = plt.subplots()
    ax.bar(labels,values)
    plt.title(name)
    plt.show() 
