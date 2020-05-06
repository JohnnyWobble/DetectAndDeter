import warnings

from fastai.text import load_learner

from timer import Timer

model = load_learner('models', 'finalv1.model')

timer = Timer()

warnings.filterwarnings('ignore')


def predict_text(text: str):
    text.replace(" %HESITATION", "")
    return str(model.predict(text)[0])


if __name__ == '__main__':
    while True:
        user_input = input("> ")
        timer.reset()
        prediction = predict_text(user_input)
        time_seconds = timer.get()
        print(prediction, end=' ')
        print(time_seconds, "s", sep="")