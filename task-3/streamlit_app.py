import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Dog Breed Image Classifier")
st.text("Provide URL of Dog Image for image classification")

@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model('./models')
  return model

with st.spinner('Loading Model Into Memory....'):
  model = load_model()

classes=['n02085620-chihuahua',
 'n02085782-japanese_spaniel',
 'n02085936-maltese_dog',
 'n02086079-pekinese',
 'n02086240-shih-tzu',
 'n02086646-blenheim_spaniel',
 'n02086910-papillon',
 'n02087046-toy_terrier',
 'n02087394-rhodesian_ridgeback',
 'n02088094-afghan_hound',
 'n02088238-basset',
 'n02088364-beagle',
 'n02088466-bloodhound',
 'n02088632-bluetick',
 'n02089078-black-and-tan_coonhound',
 'n02089867-walker_hound',
 'n02089973-english_foxhound',
 'n02090379-redbone',
 'n02090622-borzoi',
 'n02090721-irish_wolfhound',
 'n02091032-italian_greyhound',
 'n02091134-whippet',
 'n02091244-ibizan_hound',
 'n02091467-norwegian_elkhound',
 'n02091635-otterhound',
 'n02091831-saluki',
 'n02092002-scottish_deerhound',
 'n02092339-weimaraner',
 'n02093256-staffordshire_bullterrier',
 'n02093428-american_staffordshire_terrier',
 'n02093647-bedlington_terrier',
 'n02093754-border_terrier',
 'n02093859-kerry_blue_terrier',
 'n02093991-irish_terrier',
 'n02094114-norfolk_terrier',
 'n02094258-norwich_terrier',
 'n02094433-yorkshire_terrier',
 'n02095314-wire-haired_fox_terrier',
 'n02095570-lakeland_terrier',
 'n02095889-sealyham_terrier',
 'n02096051-airedale',
 'n02096177-cairn',
 'n02096294-australian_terrier',
 'n02096437-dandie_dinmont',
 'n02096585-boston_bull',
 'n02097047-miniature_schnauzer',
 'n02097130-giant_schnauzer',
 'n02097209-standard_schnauzer',
 'n02097298-scotch_terrier',
 'n02097474-tibetan_terrier',
 'n02097658-silky_terrier',
 'n02098105-soft-coated_wheaten_terrier',
 'n02098286-west_highland_white_terrier',
 'n02098413-lhasa',
 'n02099267-flat-coated_retriever',
 'n02099429-curly-coated_retriever',
 'n02099601-golden_retriever',
 'n02099712-labrador_retriever',
 'n02099849-chesapeake_bay_retriever',
 'n02100236-german_short-haired_pointer',
 'n02100583-vizsla',
 'n02100735-english_setter',
 'n02100877-irish_setter',
 'n02101006-gordon_setter',
 'n02101388-brittany_spaniel',
 'n02101556-clumber',
 'n02102040-english_springer',
 'n02102177-welsh_springer_spaniel',
 'n02102318-cocker_spaniel',
 'n02102480-sussex_spaniel',
 'n02102973-irish_water_spaniel',
 'n02104029-kuvasz',
 'n02104365-schipperke',
 'n02105056-groenendael',
 'n02105162-malinois',
 'n02105251-briard',
 'n02105412-kelpie',
 'n02105505-komondor',
 'n02105641-old_english_sheepdog',
 'n02105855-shetland_sheepdog',
 'n02106030-collie',
 'n02106166-border_collie',
 'n02106382-bouvier_des_flandres',
 'n02106550-rottweiler',
 'n02106662-german_shepherd',
 'n02107142-doberman',
 'n02107312-miniature_pinscher',
 'n02107574-greater_swiss_mountain_dog',
 'n02107683-bernese_mountain_dog',
 'n02107908-appenzeller',
 'n02108000-entlebucher',
 'n02108089-boxer',
 'n02108422-bull_mastiff',
 'n02108551-tibetan_mastiff',
 'n02108915-french_bulldog',
 'n02109047-great_dane',
 'n02109525-saint_bernard',
 'n02109961-eskimo_dog',
 'n02110063-malamute',
 'n02110185-siberian_husky',
 'n02110627-affenpinscher',
 'n02110806-basenji',
 'n02110958-pug',
 'n02111129-leonberg',
 'n02111277-newfoundland',
 'n02111500-great_pyrenees',
 'n02111889-samoyed',
 'n02112018-pomeranian',
 'n02112137-chow',
 'n02112350-keeshond',
 'n02112706-brabancon_griffon',
 'n02113023-pembroke',
 'n02113186-cardigan',
 'n02113624-toy_poodle',
 'n02113712-miniature_poodle',
 'n02113799-standard_poodle',
 'n02113978-mexican_hairless',
 'n02115641-dingo',
 'n02115913-dhole',
 'n02116738-african_hunting_dog']

def scale(image):
  image = tf.cast(image, tf.float32)
  image /= 255.0

  return tf.image.resize(image,[224,224])

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)
  img = scale(img)
  return np.expand_dims(img, axis=0)

#path = st.text_input('Enter Image URL to Classify.. ','http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02099601-golden_retriever/n02099601_3073.jpg')
img_file_buffer = st.file_uploader("Upload Dog Image to Classify....")

if img_file_buffer  is not None:
    image = img_file_buffer
    image_out = Image.open(img_file_buffer)
    image = image.getvalue()
else:
    test_image = 'http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02099601-golden_retriever/n02099601_3073.jpg'
    image = requests.get(test_image).content
    image_out = Image.open(BytesIO(image))

st.write("Predicted Class :")
with st.spinner('classifying.....'):
    label =np.argmax(model.predict(decode_img(image)),axis=1)
    st.write(classes[label[0]][10:])    
st.write("")
st.image(image_out, caption='Classifying Dog Image', use_column_width=True)
