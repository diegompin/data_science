from itertools import cycle
import matplotlib.pyplot as plt


class PlotBase(object):


    markers = ['D', 's', 'x', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8',
               '<', '>']
    colors = ['g', 'y', 'r', 'b', 'black']

    @staticmethod
    def configure_ax(ax, par_plot):
        # PlotBase.get_par_plot(par_plot)
        PlotBase.set_par(par_plot, 'x_label', ax.set_xlabel)
        PlotBase.set_par(par_plot, 'y_label', ax.set_ylabel)

        par_titles = PlotBase.get_par(par_plot, 'title', transform=cycle)
        if par_titles:
            ax.set_title(next(par_titles))

        par_loc = PlotBase.get_par(par_plot, 'legend.loc', default=4)
        par_fontsize = PlotBase.get_par(par_plot, 'legend.fontsize', default=8)
        ax.legend(loc=par_loc, fontsize=par_fontsize)
        # ax.set_title(par_plot['title'])
        # ax.grid(alpha=grid_alpha)

    @staticmethod
    def get_par_plot(par_plot):
        pass
        # PlotBase.__get_par__(par_plot, 'x_label', 'X')
        # PlotBase.__get_par__(par_plot, 'y_label', 'Y')
        # PlotBase.__get_par__(par_plot, 'title', 'title')

    @staticmethod
    def set_par(par_plot, name, func, default=None, transform=None):
        par = PlotBase.get_par(par_plot, name, default, transform)
        if par:
            func(par)

    @staticmethod
    def get_par(par_plot, name, default=None, transform=None):
        if not par_plot.keys().__contains__(name) and default is None:
            return None
        param = None
        if par_plot.keys().__contains__(name):
            param = par_plot[name]
        elif not par_plot.keys().__contains__(name) and default is not None:
            param = default

        if transform is not None:
            param = transform(param)

        return param
