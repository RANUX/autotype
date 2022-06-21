import torch

language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
#speaker = 'kseniya'
speaker = 'baya'
#speaker = 'aidar'
device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu

# audio = model.apply_tts(text=example_text,
#                         speaker=speaker,
#                         sample_rate=sample_rate)

ssml_sample = """
              <speak>
              <p>
                  Пот+ом, если повезет – <prosody rate="fast">я могу говорить и довольно быстро.</prosody>
                  А еще я умею делать паузы любой длины, например, две секунды <break time="2000ms"/>.
                  <p>
                    Также я умею делать паузы между параграфами.
                  </p>
                  <p>
                    <s>И также я умею делать паузы между предложениями</s>
                    <s>Вот например как сейчас</s>
                  </p>
              </p>
              </speak>
              """

audio_paths = model.save_wav(ssml_text=ssml_sample,
                             speaker=speaker,
                             sample_rate=sample_rate,
                             save_path='example.wav')

