import tensorflow_datasets as tfds
import tensorflow as tf
import warnings
warnings.simplefilter('ignore')


class ClassificationModel:

    def __init__(self):
        self.modelPath = 'C:/Users/Lenovo/OneDrive/Documents/Github/SentimentAnalysis/cntCpModel' + '/ourModel'
        self.encoderPath = 'C:/Users/Lenovo/OneDrive/Documents/Github/SentimentAnalysis/cntCpModel' + '/text.text'
        self.encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file(self.encoderPath)
        self.encoder.vocab_size

        self.loadedModel = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.encoder.vocab_size, 64),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64,  return_sequences=True)),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        self.loadedModel.load_weights(self.modelPath)
        self.loadedModel.compile(loss='binary_crossentropy',
                            optimizer=tf.keras.optimizers.Adam(1e-4),
                            metrics=['accuracy'])

    def pad_to_size(self, vec, size):
        zeros = [0] * (size - len(vec))
        vec.extend(zeros)
        return vec

    def sample_predict(self, sample_pred_text, pad):
        encoded_sample_pred_text = self.encoder.encode(sample_pred_text)
        if pad:
            encoded_sample_pred_text = self.pad_to_size(encoded_sample_pred_text, 64)
        encoded_sample_pred_text = tf.cast(encoded_sample_pred_text, tf.float32)
        predictions = self.loadedModel.predict(tf.expand_dims(encoded_sample_pred_text, 0), steps=1)
        return (predictions)

    def getResult(self, text):
        sample_pred_text = text
        predictions = self.sample_predict(sample_pred_text, pad=False)
        return predictions[0]
