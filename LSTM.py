from keras.layers import LSTM,Dense
from keras.models import Sequential
from keras.callbacks import EarlyStopping


def LSTMclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------LSTM---------------------------------")
    #here I reshape the input so that I have (number of samples) of arrays of dimension 1*number of features
    X_train=X_train.reshape(X_train.shape[0],1,X_train.shape[1])
    X_test=X_test.reshape(X_test.shape[0],1,X_test.shape[1])




    model=Sequential()
    #input type ia an array of dim (1,number of features)
    model.add(LSTM(200,activation='tanh',dropout=0.4,recurrent_dropout=0.2,
               return_sequences=True, input_shape=(1,X_train.shape[2])))

    model.add(LSTM(100,activation='tanh',dropout=0.4,recurrent_dropout=0.2,return_sequences=True))

    model.add(LSTM(50,activation='tanh',dropout=0.4,recurrent_dropout=0.2))

    model.add(Dense(1,activation='sigmoid'))
     # rmsprop is the best optimizer for avoiding overfitting for RNN (Keras Documentation)
    model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

    # Display model architecture summary
    model.summary()
    #monitor=metric to evaluate, min_delta=minimum improvement, patience= number of epochs to wait to control
    earlystopping=EarlyStopping(monitor='val_loss',min_delta=0.001,patience=5)
    model.fit(X_train,Y_train,batch_size=512,validation_split=0.2,epochs=20,callbacks=[earlystopping])

    score_test=model.evaluate(X_test,Y_test)
    score_train=model.evaluate(X_train,Y_train)
    return score_test,score_train