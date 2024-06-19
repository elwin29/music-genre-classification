from keras import models, optimizers, callbacks, metrics
from keras.layers import *

def create_baseline(input_shape, num_classes):
    input_layer = Input(shape=input_shape)
    x = Dense(1024, activation='relu')(input_layer)
    x = Dense(512, activation='relu')(x)
    x = Dense(256, activation='relu')(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(64, activation='relu')(x)
    output_layer = Dense(num_classes, activation='softmax')(x)
    model = models.Model(inputs=input_layer, outputs=output_layer)

    return model
    
def create_regularized_model(input_shape, num_classes):
    input_layer = Input(shape=input_shape)
    x = Dense(1024, activation='relu')(input_layer)
    x = Dropout(0.3)(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.3)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.3)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.3)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.3)(x)
    output_layer = Dense(num_classes, activation='softmax')(x)
    model = models.Model(inputs=input_layer, outputs=output_layer)
    
    return model
    
def create_normalized_model(input_shape, num_classes):
    input_layer = Input(shape=input_shape)
    x = Dense(1024, activation='relu')(input_layer)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(512, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(256, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(128, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    x = Dense(64, activation='relu')(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)
    output_layer = Dense(num_classes, activation='softmax')(x)
    model = models.Model(inputs=input_layer, outputs=output_layer)
    
    return model