import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def split_pipe_list(s):
    if pd.isna(s) or s == '':
        return []
    return [x.strip() for x in str(s).split(',') if x.strip()]


def regression_metrics(y_true, y_pred):
    """MAE, RMSE e R² sem imprimir (útil para montar tabelas)."""
    mae = mean_absolute_error(y_true, y_pred)
    try:
        rmse_val = mean_squared_error(y_true, y_pred, squared=False)
    except TypeError:
        rmse_val = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return {'MAE': mae, 'RMSE': rmse_val, 'R2': r2}


def error_metrics(y_true, y_pred):
    """MAE, RMSE e R²; imprime no stdout e devolve a tupla."""
    m = regression_metrics(y_true, y_pred)
    print(f'MAE:  {m["MAE"]:.4f}')
    print(f'RMSE: {m["RMSE"]:.4f}')
    print(f'R²:   {m["R2"]:.4f}')
    return m['MAE'], m['RMSE'], m['R2']
