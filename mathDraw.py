from matplotlib.pyplot import (grid, title , pie , legend , show , xlim , ylim ,
                               plot , xlabel , ylabel , bar)

class Plot:
    def pieDraw(self , title_graph , data , labels , colors , angle , legend_graph , loc):
        title(title_graph)
        pie(data , labels = labels , startangle = angle , colors = colors)
        legend(title = legend_graph , loc = loc)
        show()

    def plotDraw(self , x , y , title_graph , limx , limy , labelx , labely , fontx , fonty):
        title(title_graph)
        xlim(0 , limx)
        ylim(0 , limy)
        plot(x , y)
        xlabel(labelx , fontdict = fontx)
        ylabel(labely, fontdict = fonty)
        show()
    
    def barDraw(self , title_graph , objects , values , data , colors, labelx, labely, size):
        bar(objects , values , data = data , color = colors)
        xlabel(labelx , fontsize = size)
        ylabel(labely , fontsize =  size)
        title(title_graph)
        grid(True)
        show()