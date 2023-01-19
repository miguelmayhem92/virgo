class data_configs:
    n_days = 950
    lags = 3
    window = 7
    std_column = 'Close_roll_std'
    ref_price = 'Close'
    logdif_column = 'Dif'
    split_config = {
        'train':0.65,
        'val':0.85
    }
    steps_to_predic = 4
    input_length = 14