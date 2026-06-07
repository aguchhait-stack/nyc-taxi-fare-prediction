import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_csv(filepath:str ='data.nosync/train.zip',nrows:int=10) -> pd.DataFrame: 
    
    if not os.path.exists(filepath):
        raise FileNotFoundError (f"file not found at {filepath}")
                                 
    df = pd.read_csv(filepath,nrows=nrows)

    logger.info(f"Successfully loaded {len(df)} rows")

    return df


        
    
