import os
from os import PathLike
from typing import Optional, Union
import numpy as np
import matplotlib.pyplot as plt
'''
Funj is a fungible token--the future is here (or is it there?) 
'''

#I was going to include support for arbitrary powers of ten, but if you're printing hundreds of
#thousands of these you probably have bigger problems than a lack of feedback from the Funj Printer.
BARK_VALS = np.array([5,10,20,50,100,1000,10000], dtype= int)
BARKS = ["Now we're getting funjy",
         "It's funjing time!",
         "There may be soon be some inflation in Funj Nation.",
         f"If you have {BARK_VALS[3]} friends, you can give each of them a Funj Token.\n"
         f"How generous!",
         "funjj",
         "funjjj",
         "funjjjj"]
class FunjToken:
    '''
    Token of inperceptible value.
    '''

    def __init__(self,size:int,colormap:Optional = None):
        '''
        :param size: int
            Size of edge of Funj token matrix
            Is bigger better? Only you can find out!
        :param colormap: Optional[str] (default: None, maps to "turbo")
            Colormap for printed token.
        '''

        self.size = size
        if colormap is None:
            colormap = "turbo"
        self.cmap = plt.get_cmap(colormap)
        self.matrix = np.random.rand(size,size)
        self.bytes = self.matrix.tobytes()
        self.fullname = hash(self.bytes)
    def create_image_token(self,savedir: PathLike)->None:
        '''
        Create Funj image token and saves JPEG image to save directory
        Name is given by shortened name of hash of Funj matrix
        :param savedir: PathLike
        :return: None
        '''
        fig, ax = plt.subplots(figsize = (4,4))
        img = ax.matshow(self.matrix,cmap = self.cmap)
        ax.set_axis_off()
        fig.savefig(os.path.join(savedir,f"{self.fullname}.jpeg"),dpi = 500)
    def create_binary(self,savedir: PathLike)->None:
        '''
        Create Funj binary token and saves file to save directory
        Name is given by shortened name of hash of Funj matrix
        :param savedir: PathLike
        :return: None
        '''
        with open(os.path.join(savedir,f"{self.fullname}.txt"),"wb") as funj_file:
            funj_file.write(self.bytes)

    def create_tokens(self,savedir:PathLike)->None:
        '''
        Creates Funj binary and image tokens in save_directory
        :param savedir: PathLike
        :return: None
        '''
        self.create_binary(savedir)
        self.create_image_token(savedir)

class FunjPrinter:
    '''
    Goes fjjjjjjjjjjjj
    '''
    def __init__(self,token_size:int,n_tokens:int,
                 base_dir:PathLike = ".",batch_size:int = 10,
                 colormap:Optional[str] = None):
        '''
        :param token_size: int
            Size of FunjToken 2D matrix side
        :param n_tokens: int
        :param base_dir: PathLike (default: ".")
            Base directory to save tokens to
        :param batch_size: int (default: 10)
            Number of tokens to save to directory
        :param colormap: Optional[str] (default: None)
            if not None, overwrites default FunjToken colormap
        '''
        self.token_size = token_size
        self.n_tokens = n_tokens
        self.base_dir = base_dir
        self.batch_size = batch_size
        self.cmap = colormap
        self.run()

    def run(self):
        "Runs the printer--goes upon initialization."
        dir_idx = 0
        cur_dir = self.base_dir
        for i in np.arange(self.n_tokens):
            if i % self.batch_size == 0: #directory this way starts at 1
                dir_idx= dir_idx+1
                cur_dir = self._update_dir(dir_idx)
            if i in BARK_VALS:
                bark_idx = np.argmin(np.abs(BARK_VALS-i))
                print(BARKS[bark_idx])
            token = FunjToken(size=self.token_size,colormap=self.cmap)
            token.create_tokens(cur_dir)

    def _update_dir(self,dir_idx:int):
        '''Makes and returns updated directory for Funj printing'''
        new_dir = os.path.join(self.base_dir,str(dir_idx))
        os.makedirs(new_dir,exist_ok=True)
        return new_dir


