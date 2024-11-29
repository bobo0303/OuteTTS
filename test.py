"""
EN (6 speakers):
  - male_1
  - male_2
  - male_3
  - male_4
  - female_1
  - female_2

JA (4 speakers):
  - male_1
  - female_1
  - female_2
  - female_3

KO (4 speakers):
  - male_1
  - male_2
  - female_1
  - female_2

ZH (2 speakers):
  - male_1
  - female_1
"""
import outetts
import time

#########################################################################################################
speaker_choose = "voice_clone" # "default" or "voice_clone"
voice = "female_1" # "default" or "voice_clone"
vc_audio = "pre_audio/en.wav"
vc_json_save_name = "speakers_json/bobo_en.json"
language = "en" # Supported languages in v0.2: en, zh, ja, ko
text = "Speech synthesis is the artificial production of human speech. A computer system used for this purpose is called a speech synthesizer, and it can be implemented in software or hardware products."
temperature = 0.1
#########################################################################################################

# Configure the model
model_config = outetts.HFModelConfig_v1(
    model_path="models/OuteTTS-0.2-500M",
    language=language,  # Supported languages in v0.2: en, zh, ja, ko
)

interface_s = time.time()
# Initialize the interface
interface = outetts.InterfaceHF(model_version="0.2", cfg=model_config)
interface_e = time.time()

create_speaker_s = time.time()
# Optional: Create a speaker profile (use a 10-15 second audio clip)
speaker = interface.create_speaker(
    audio_path=vc_audio,
    transcript="Transcription of the audio file."
)
create_speaker_e = time.time()

if speaker_choose == "voice_clone":
    # Optional: Save and load speaker profiles
    save_speaker_s = time.time()
    interface.save_speaker(speaker, vc_json_save_name)
    save_speaker_e = time.time()
    load_speaker_s = time.time()
    speaker = interface.load_speaker(vc_json_save_name)
    load_speaker_e = time.time()
elif speaker_choose == "default":
    # Optional: Load speaker from default presets
    load_default_speaker_s = time.time()
    interface.print_default_speakers()
    speaker = interface.load_default_speaker(name=voice) 
    load_default_speaker_e = time.time()
else: 
    speaker = None
    print("="*10+" random default " + "="*10)
    exit()
    
generate_s = time.time()
output = interface.generate(
    text=text,
    # Lower temperature values may result in a more stable tone,
    # while higher values can introduce varied and expressive speech
    temperature=temperature,
    repetition_penalty=1.1,
    max_length=4096,

    # Optional: Use a speaker profile for consistent voice characteristics
    # Without a speaker profile, the model will generate a voice with random characteristics
    speaker=speaker,
)
generate_e = time.time()

# Save the synthesized speech to a file
save_s = time.time()
if speaker_choose == "voice_clone":
    output.save("voice_clone_"+ vc_json_save_name.split("/")[-1][:-5]+".wav")
elif speaker_choose == "default":
    output.save(voice+".wav")
save_e = time.time()

# Optional: Play the synthesized speech
# output.play()

print("Initialize the interface: ", interface_e - interface_s)
print("create_speaker: ", create_speaker_e - create_speaker_s)
if speaker_choose == "voice_clone":
    print("save_speaker: ", save_speaker_e - save_speaker_s)
    print("load_speaker: ", load_speaker_e - load_speaker_s)
elif speaker_choose == "default":
    print("load_default_speaker: ", load_default_speaker_e - load_default_speaker_s)
print("generate: ", generate_e - generate_s)

