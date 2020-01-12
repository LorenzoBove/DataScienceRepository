from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import MaxPooling1D, Conv1D
from keras.callbacks import EarlyStopping



def CNNclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------CNN-----------------------------------")
    #reshape the input for the Neural Network
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1],1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    model = Sequential()
    model.add(Conv1D(filters=200, kernel_size=2, padding='same', input_shape=( X_train.shape[1],1), activation='relu'))
    model.add(MaxPooling1D(pool_size=2,strides=2))
    model.add(Dropout(0.3))
    model.add(Conv1D(filters=100, kernel_size=2, padding='same',  activation='relu'))
    model.add(MaxPooling1D(pool_size=2,strides=2))
    model.add(Dropout(0.3))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam')

    # Display model architecture summary
    model.summary()
    #monitor=metric to evaluate, min_delta=minimum improvement, patience= number of epochs to wait to control

    earlystopping=EarlyStopping(monitor='val_loss',min_delta=0.001,patience=5)
    model.fit(X_train,Y_train,batch_size=2,validation_split=0.2,epochs=20,callbacks=[earlystopping])

    score_test=model.evaluate(X_test,Y_test)
    score_train=model.evaluate(X_train,Y_train)
    return score_test,score_train