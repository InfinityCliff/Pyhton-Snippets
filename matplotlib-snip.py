import io
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import tkinter
from pylab import rcParams

def get_graph_image(data=None, height=5, width=10, dpi=50,
                    title='title', style='fivethirtyeight'):    
    '''return (PIL.ImageTk.PhotoImage) from matplotlib

    Args:
    data: information to be plotted, if not provided will use test data of (1,2)
    height (int): height of graph
    width (int): width of graph
    dpi (int): dpi of graph
    title: (str): title of graph
    style: (str): plot style to use, defaults to 'fivethirtyeight'
    '''
    if data is None:
        data = (1,2)
            
    rcParams['figure.figsize'] = width, height
    
    plt.style.use(style)
    plt.plot(data)
    plt.title(title)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=dpi, bbox_inches='tight')
    buf.seek(0)

    im = Image.open(buf)
    image = im.copy()
    buf.close()
    
    return ImageTk.PhotoImage(image)


if __name__ == '__main__':
    window = tkinter.Tk()
    test = get_graph_image()
    print(type(test))
