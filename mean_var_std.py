import numpy as np

def calculate(list):
    calculations = 0
    try:
        lst = np.array(list)
        
        mean = [
            [lst[[0,1,2]].mean(), lst[[3,4,5]].mean(), lst[[6,7,8]].mean()],
            [lst[[0,3,6]].mean(), lst[[1,4,7]].mean(), lst[[2,5,8]].mean()]
        ]

        var = [
            [lst[[0,1,2]].var(), lst[[3,4,5]].var(), lst[[6,7,8]].var()],
            [lst[[0,3,6]].var(), lst[[1,4,7]].var(), lst[[2,5,8]].var()]
        ]

        stand = [
            [lst[[0,1,2]].std(), lst[[3,4,5]].std(), lst[[6,7,8]].std()],
            [lst[[0,3,6]].std(), lst[[1,4,7]].std(), lst[[2,5,8]].std()]
        ]

        mx = [
            [lst[[0,1,2]].max(), lst[[3,4,5]].max(), lst[[6,7,8]].max()],
            [lst[[0,3,6]].max(), lst[[1,4,7]].max(), lst[[2,5,8]].max()]
        ]

        mn = [
            [lst[[0,1,2]].min(), lst[[3,4,5]].min(), lst[[6,7,8]].min()],
            [lst[[0,3,6]].min(), lst[[1,4,7]].min(), lst[[2,5,8]].min()]
        ]

        sm = [
            [lst[[0,1,2]].sum(), lst[[3,4,5]].sum(), lst[[6,7,8]].sum()],
            [lst[[0,3,6]].sum(), lst[[1,4,7]].sum(), lst[[2,5,8]].sum()]
        ]
        
        calculations = {
          'mean': [mean[1], mean[0], lst.mean()],
          'variance': [var[1], var[0], lst.var()],
          'standard deviation': [stand[1], stand[0], lst.std()],
          'max': [mx[1], mx[0], lst.max()],
          'min': [mn[1], mn[0], lst.min()],
          'sum': [sm[1], sm[0], lst.sum()]
        }

        return calculations
    except:
        raise ValueError("List must contain nine numbers.")