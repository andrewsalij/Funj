import os
import funj.funj as funj

if __name__ == "__main__":
    base_dir = os.path.join(os.getcwd(),"funj_vault")
    funj.FunjPrinter(token_size=5,n_tokens=10,base_dir= base_dir ,batch_size=5)





