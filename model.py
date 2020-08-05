from tensorflow import keras
from tensorflow.keras import layers

def get_callbacks(model_filepath):

    #checkpoint_fp = model_filepath + '_Epoch-{epoch}'
    checkpoint_fp = model_filepath
    CheckPoint = keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_fp, verbose=1, monitor='val_loss',
        save_best_only=True, save_weights_only=True
    )

    logger_fp = model_filepath+'_history.csv'
    CSVLogger = keras.callbacks.CSVLogger(
        filename=logger_fp, append=False
    )

    EarlyStopping = keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=10, verbose=1, restore_best_weights=True
    )

    return [CheckPoint, CSVLogger, EarlyStopping]

def get_model(input_shape):
    model = keras.Sequential()
    model.add(keras.Input(shape=input_shape))
    model.add(layers.Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(layers.Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(layers.Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(layers.Dense(2, activation='softmax', kernel_initializer='he_uniform'))

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    model.summary()
    
    return model